SELECT id, username, pp_std, pp_mania FROM rx_stats;
SELECT id, userid, beatmap_md5, play_mode, completed, pp FROM scores;
SELECT id, userid, beatmap_md5, play_mode, completed, pp FROM scores_relax;
SELECT * FROM beatmaps WHERE beatmap_id <= 0