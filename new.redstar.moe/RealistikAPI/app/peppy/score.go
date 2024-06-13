package peppy

import (
	"database/sql"
	"fmt"
	"strconv"
	"strings"

	"github.com/RealistikOsu/RealistikAPI/common"

	"github.com/jmoiron/sqlx"
	"github.com/valyala/fasthttp"
	"gopkg.in/thehowl/go-osuapi.v1"
	"zxq.co/x/getrank"
)

// GetScores retrieve information about the top 100 scores of a specified beatmap.
func GetScores(c *fasthttp.RequestCtx, db *sqlx.DB) {
	if query(c, "b") == "" {
		json(c, 200, defaultResponse)
		return
	}
	var beatmapMD5 string
	err := db.Get(&beatmapMD5, "SELECT beatmap_md5 FROM beatmaps WHERE beatmap_id = ? LIMIT 1", query(c, "b"))
	switch {
	case err == sql.ErrNoRows:
		json(c, 200, defaultResponse)
		return
	case err != nil:
		common.Err(c, err)
		json(c, 200, defaultResponse)
		return
	}
	// Table.
	mods := common.Int(query(c, "mods"))
	rx := common.Int(query(c, "rx"))
	var table = "scores"
	if mods&128 > 0 || rx == 1 {
		table = "scores_relax"
	}
	if mods&4096 > 0 || rx == 2 {
		table = "scores_ap"
	}

	var sb = "s.score"
	if rankable(query(c, "m")) {
		sb = "s.pp"
	}
	
	var completed = "3"
	if query(c, "u") != "" {
		completed = "2"
	}
	
	var (
		extraWhere  string
		extraParams []interface{}
	)
	if query(c, "u") != "" {
		w, p := genUser(c, db)
		extraWhere = "AND " + w
		extraParams = append(extraParams, p)
	}

	rows, err := db.Query(fmt.Sprintf(`
SELECT
	s.id, s.score, users.username, s.300_count, s.100_count,
	s.50_count, s.misses_count, s.gekis_count, s.katus_count,
	s.max_combo, s.full_combo, s.mods, users.id, s.time, s.pp,
	s.accuracy
FROM %s s
INNER JOIN users ON users.id = s.userid
WHERE s.completed >= ?
  AND users.privileges & 1 > 0
  AND s.beatmap_md5 = ?
  AND s.play_mode = ?
  AND s.mods & ? = ?
  `, table)+extraWhere+`
ORDER BY `+sb+` DESC LIMIT `+strconv.Itoa(common.InString(1, query(c, "limit"), 100, 50)),
		append([]interface{}{completed, beatmapMD5, genmodei(query(c, "m")), mods, mods}, extraParams...)...)
	if err != nil {
		common.Err(c, err)
		json(c, 200, defaultResponse)
		return
	}
	var results []osuapi.GSScore
	for rows.Next() {
		var (
			s         osuapi.GSScore
			fullcombo bool
			mods      int
			date      common.UnixTimestamp
			accuracy  float64
		)
		err := rows.Scan(
			&s.ScoreID, &s.Score.Score, &s.Username, &s.Count300, &s.Count100,
			&s.Count50, &s.CountMiss, &s.CountGeki, &s.CountKatu,
			&s.MaxCombo, &fullcombo, &mods, &s.UserID, &date, &s.PP,
			&accuracy,
		)
		if err != nil {
			if err != sql.ErrNoRows {
				common.Err(c, err)
			}
			continue
		}
		s.FullCombo = osuapi.OsuBool(fullcombo)
		s.Mods = osuapi.Mods(mods)
		s.Date = osuapi.MySQLDate(date)
		s.Rank = strings.ToUpper(getrank.GetRank(osuapi.Mode(genmodei(query(c, "m"))), s.Mods,
			accuracy, s.Count300, s.Count100, s.Count50, s.CountMiss))
		results = append(results, s)
	}
	json(c, 200, results)
	return
}
