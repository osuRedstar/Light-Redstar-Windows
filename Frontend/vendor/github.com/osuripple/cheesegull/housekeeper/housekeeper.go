// Package housekeeper manages the local cache of CheeseGull, by always keeping
// track of the local state of the cache and keeping it to a low amount.
package housekeeper

import (
	"log"
	"os"
	"sort"
	"sync"

	raven "github.com/getsentry/raven-go"
)

// House manages the state of the cached beatmaps in the local filesystem.
type House struct {
	MaxSize     uint64
	state       []*CachedBeatmap
	stateMutex  sync.RWMutex
	requestChan chan struct{}
	// set to non-nil to avoid calling os.Remove on the files to remove, and
	// place them here instead.
	dryRun []*CachedBeatmap
}

// New creates a new house, initialised with the default values.
func New() *House {
	return &House{
		MaxSize:     1024 * 1024 * 1024 * 10, // 10 gigs
		requestChan: make(chan struct{}, 1),
	}
}

// scheduleCleanup enschedules a housekeeping request if one isn't already
// present.
func (h *House) scheduleCleanup() {
	select {
	case h.requestChan <- struct{}{}:
		// carry on
	default:
		// carry on
	}
}

// StartCleaner starts the process that will do the necessary housekeeping
// every time a cleanup is scheduled with scheduleCleanup.
func (h *House) StartCleaner() {
	go func() {
		for {
			<-h.requestChan
			h.cleanUp()
		}
	}()
}

func (h *House) cleanUp() {
	log.Println("[C] Running cleanup")

	toRemove := h.mapsToRemove()

	f, err := os.Create("cgbin.db")
	if err != nil {
		logError(err)
		return
	}

	// build new state by removing from it the beatmaps from toRemove
	h.stateMutex.Lock()
	newState := make([]*CachedBeatmap, 0, len(h.state))
StateLoop:
	for _, b := range h.state {
		for _, r := range toRemove {
			if r.ID == b.ID && r.NoVideo == b.NoVideo {
				continue StateLoop
			}
		}
		newState = append(newState, b)
	}
	h.state = newState
	err = writeBeatmaps(f, h.state)
	h.stateMutex.Unlock()

	f.Close()
	if err != nil {
		logError(err)
		return
	}

	if h.dryRun != nil {
		h.dryRun = toRemove
		return
	}

	for _, b := range toRemove {
		err := os.Remove(b.fileName())
		switch {
		case err == nil, os.IsNotExist(err):
			// silently ignore
		default:
			logError(err)
		}
	}
}

func (h *House) mapsToRemove() []*CachedBeatmap {
	totalSize, removable := h.stateSizeAndRemovableMaps()

	if totalSize <= h.MaxSize {
		// no clean up needed, our totalSize has still not gotten over the
		// threshold
		return nil
	}

	sortByLastRequested(removable)

	removeBytes := int(totalSize - h.MaxSize)
	var toRemove []*CachedBeatmap
	for _, b := range removable {
		toRemove = append(toRemove, b)
		fSize := b.FileSize()
		removeBytes -= int(fSize)
		if removeBytes <= 0 {
			break
		}
	}

	return toRemove
}

// i hate verbose names myself, but it was very hard to come up with something
// even as short as this.
func (h *House) stateSizeAndRemovableMaps() (totalSize uint64, removable []*CachedBeatmap) {
	h.stateMutex.RLock()
	for _, b := range h.state {
		if !b.IsDownloaded() {
			continue
		}
		fSize := b.FileSize()
		totalSize += fSize
		if fSize == 0 {
			continue
		}
		removable = append(removable, b)
	}
	h.stateMutex.RUnlock()
	return
}

func sortByLastRequested(b []*CachedBeatmap) {
	sort.Slice(b, func(i, j int) bool {
		b[i].mtx.RLock()
		b[j].mtx.RLock()
		r := b[i].lastRequested.Before(b[j].lastRequested)
		b[i].mtx.RUnlock()
		b[j].mtx.RUnlock()
		return r
	})
}

// LoadState attempts to load the state from cgbin.db
func (h *House) LoadState() error {
	f, err := os.Open("cgbin.db")
	switch {
	case os.IsNotExist(err):
		return nil
	case err != nil:
		return err
	}
	defer f.Close()

	h.stateMutex.Lock()
	h.state, err = readBeatmaps(f)
	h.stateMutex.Unlock()

	return err
}

var envSentryDSN = os.Getenv("SENTRY_DSN")

// logError attempts to log an error to Sentry, as well as stdout.
func logError(err error) {
	if err == nil {
		return
	}
	if envSentryDSN != "" {
		raven.CaptureError(err, nil)
	}
	log.Println(err)
}
