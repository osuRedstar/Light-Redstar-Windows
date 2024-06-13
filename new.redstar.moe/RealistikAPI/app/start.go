package app

import (
	"fmt"
	"time"

	"github.com/DataDog/datadog-go/statsd"
	"github.com/RealistikOsu/RealistikAPI/app/internals"
	"github.com/RealistikOsu/RealistikAPI/app/peppy"
	v1 "github.com/RealistikOsu/RealistikAPI/app/v1"
	"github.com/RealistikOsu/RealistikAPI/app/websockets"
	"github.com/RealistikOsu/RealistikAPI/common"
	fhr "github.com/buaazp/fasthttprouter"
	"github.com/getsentry/raven-go"
	"github.com/jmoiron/sqlx"
	"gopkg.in/redis.v5"

	//Add-on
	"github.com/RealistikOsu/RealistikAPI/app/hmrapi"
	"github.com/RealistikOsu/RealistikAPI/app/mitsuha"
)

var (
	db    *sqlx.DB
	cf    common.Conf
	doggo *statsd.Client
	red   *redis.Client
)

// Start begins taking HTTP connections.
func Start(conf common.Conf, dbO *sqlx.DB) *fhr.Router {
	db = dbO
	cf = conf

	rawRouter := fhr.New()
	r := router{rawRouter}
	// TODO: add back gzip
	// TODO: add logging
	// TODO: add sentry panic recovering

	// sentry
	if conf.SentryDSN != "" {
		ravenClient, err := raven.New(conf.SentryDSN)
		ravenClient.SetRelease(common.Version)
		if err != nil {
			fmt.Println(err)
		} else {
			// r.Use(Recovery(ravenClient, false))
			common.RavenClient = ravenClient
		}
	}

	// datadog
	var err error
	doggo, err = statsd.New("127.0.0.1:8125")
	if err != nil {
		fmt.Println(err)
	}
	doggo.Namespace = "api."

	// redis
	red = redis.NewClient(&redis.Options{
		Addr:     conf.RedisAddr,
		Password: conf.RedisPassword,
		DB:       conf.RedisDB,
	})
	peppy.R = red

	// token updater
	go tokenUpdater(db)

	// start websocket
	websockets.Start(red, db)

	// start load achievements
	go v1.LoadAchievementsEvery(db, time.Minute*10)

	// peppyapi
	{
		r.Peppy("/api/get_user", peppy.GetUser)
		r.Peppy("/api/get_match", peppy.GetMatch)
		r.Peppy("/api/get_user_recent", peppy.GetUserRecent)
		r.Peppy("/api/get_user_best", peppy.GetUserBest)
		r.Peppy("/api/get_scores", peppy.GetScores)
		r.Peppy("/api/get_beatmaps", peppy.GetBeatmap)
	}

	// v1 API
	{
		r.POSTMethod("/api/v1/tokens/self/delete", v1.TokenSelfDeletePOST)

		// Auth-free API endpoints (public data)
		r.Method("/api/v1/ping", v1.PingGET)
		r.Method("/api/v1/surprise_me", v1.SurpriseMeGET)
		r.Method("/api/v1/users", v1.UsersGET)
		r.Method("/api/v1/users/whatid", v1.UserWhatsTheIDGET)
		r.Method("/api/v1/users/full", v1.UserFullGET)
		r.Method("/api/v1/users/achievements", v1.UserAchievementsGET)
		r.Method("/api/v1/users/most_played", v1.UserMostPlayedGET)
		r.Method("/api/v1/users/userpage", v1.UserUserpageGET)
		r.Method("/api/v1/users/lookup", v1.UserLookupGET)
		r.Method("/api/v1/users/scores/best", v1.UserScoresBestGET)
		r.Method("/api/v1/users/scores/recent", v1.UserScoresRecentGET)
		r.Method("/api/v1/users/scores/first", v1.UserFirstGET) // Thanks Akatsuki!
		r.Method("/api/v1/first/oldest", v1.OldestFirstGET)
		r.Method("/api/v1/users/scores/pinned", v1.UserPinnedGET)
		r.Method("/api/v1/users/scores/pinned/info", v1.PinnedScoreGET)
		r.Method("/api/v1/users/comments", v1.CommentGET)
		r.Method("/api/v1/users/comments/info", v1.CommentInfoGET)
		r.Method("/api/v1/badges", v1.BadgesGET)
		r.Method("/api/v1/badges/members", v1.BadgeMembersGET)
		r.Method("/api/v1/beatmaps", v1.BeatmapGET)
		r.Method("/api/v1/leaderboard", v1.LeaderboardGET)
		r.Method("/api/v1/tokens", v1.TokenGET)
		r.Method("/api/v1/users/self", v1.UserSelfGET)
		r.Method("/api/v1/tokens/self", v1.TokenSelfGET)
		r.Method("/api/v1/blog/posts", v1.BlogPostsGET)
		r.Method("/api/v1/scores", v1.ScoresGET)

		r.Method("/api/beatmaps/scores", v1.ScoresGET)

		r.Method("/api/v1/beatmaps/rank_requests/status", v1.BeatmapRankRequestsStatusGET)

		// ReadConfidential privilege required
		r.Method("/api/v1/friends", v1.FriendsGET, common.PrivilegeReadConfidential)
		r.Method("/api/v1/friends/with", v1.FriendsWithGET, common.PrivilegeReadConfidential)
		r.Method("/api/v1/users/self/donor_info", v1.UsersSelfDonorInfoGET, common.PrivilegeReadConfidential)
		r.Method("/api/v1/users/self/favourite_mode", v1.UsersSelfFavouriteModeGET, common.PrivilegeReadConfidential)
		r.Method("/api/v1/users/self/settings", v1.UsersSelfSettingsGET, common.PrivilegeReadConfidential)

		// Write privilege required
		r.POSTMethod("/api/v1/users/scores/pinned", v1.UserPinnedPOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/users/scores/pinned/delete", v1.UserPinnedDeletePOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/friends/add", v1.FriendsAddPOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/friends/del", v1.FriendsDelPOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/users/self/settings", v1.UsersSelfSettingsPOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/users/self/userpage", v1.UserSelfUserpagePOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/beatmaps/rank_requests", v1.BeatmapRankRequestsSubmitPOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/users/comments", v1.CommentPOST, common.PrivilegeWrite)
		r.POSTMethod("/api/v1/users/comments/delete", v1.CommentDELETE, common.PrivilegeWrite)

		// Admin: RAP
		r.POSTMethod("/api/v1/rap/log", v1.RAPLogPOST)

		// Admin: beatmap
		r.POSTMethod("/api/v1/beatmaps/set_status", v1.BeatmapSetStatusPOST, common.PrivilegeBeatmap)
		r.Method("/api/v1/beatmaps/ranked_frozen_full", v1.BeatmapRankedFrozenFullGET, common.PrivilegeBeatmap)

		// Admin: user managing
		r.POSTMethod("/api/v1/users/manage/set_allowed", v1.UserManageSetAllowedPOST, common.PrivilegeManageUser)
		r.POSTMethod("/api/v1/users/edit", v1.UserEditPOST, common.PrivilegeManageUser)
		r.POSTMethod("/api/v1/users/wipe", v1.WipeUserPOST, common.PrivilegeManageUser)
		r.POSTMethod("/api/v1/scores/reports", v1.ScoreReportPOST, common.PrivilegeManageUser)

		// M E T A
		// E     T    "wow thats so meta"
		// T     E                  -- the one who said "wow thats so meta"
		// A T E M
		r.Method("/api/v1/meta/restart", v1.MetaRestartGET, common.PrivilegeAPIMeta)
		r.Method("/api/v1/meta/up_since", v1.MetaUpSinceGET, common.PrivilegeAPIMeta)
		r.Method("/api/v1/meta/update", v1.MetaUpdateGET, common.PrivilegeAPIMeta)

		// User Managing + meta
		r.POSTMethod("/api/v1/tokens/fix_privileges", v1.TokenFixPrivilegesPOST,
			common.PrivilegeManageUser, common.PrivilegeAPIMeta)
	}
	{
		r.Method("/api/v1/users/followers", mitsuha.FollowersGetResponse)
		r.Method("/api/v1/clans", v1.ClansGET)
		r.Method("/api/v1/clans/members", v1.ClanMembersGET)
		r.Method("/api/v1/clans/stats", v1.TotalClanStatsGET)

		r.Method("/api/v1/clans/stats/first", v1.ClansGET)

		r.Method("/api/v1/clans/stats/all", v1.AllClanStatsGET)
		r.Method("/api/v1/clans/getinvite", v1.ClanInviteGET)
		r.Method("/api/v1/clans/isclan", v1.IsInClanGET)
		r.Method("/api/v1/hmrapi/topdonors", hmrapi.TopDonorsGET)
		r.Method("/api/v1/hmrapi/top_beatmaps", hmrapi.Beatmaps5GET)
		r.Method("/api/v1/hmrapi/top_plays", hmrapi.TopPlaysGET)
		r.Method("/api/v1/users/get_activity", hmrapi.LogsGET)
		r.Method("/api/v1/mitsuha/followers_friends", mitsuha.FollowersGET)
	}

	// Websocket API
	{
		r.PlainGET("/api/v1/ws", websockets.WebsocketV1Entry)
	}

	// in the new osu-web, the old endpoints are also in /v1 it seems. So /shrug
	{
		r.Peppy("/api/v1/get_user", peppy.GetUser)
		r.Peppy("/api/v1/get_match", peppy.GetMatch)
		r.Peppy("/api/v1/get_user_recent", peppy.GetUserRecent)
		r.Peppy("/api/v1/get_user_best", peppy.GetUserBest)
		r.Peppy("/api/v1/get_scores", peppy.GetScores)
		r.Peppy("/api/v1/get_beatmaps", peppy.GetBeatmap)
	}

	r.GET("/api/status", internals.Status)

	rawRouter.NotFound = v1.Handle404

	return rawRouter
}
