select sum(ROUND(ROUND(DD.pp) * pow(0.95,  (DD.RANKING-1)))) as pp from(SELECT ROW_NUMBER() OVER(ORDER BY pp DESC) AS RANKING, userid,pp FROM scores_relax WHERE beatmap_md5 in (select beatmap_md5 from beatmaps where ranked = 2 OR ranked = 3) AND userid = 1000 AND play_mode = 0 AND completed = 3 LIMIT 500) as DD;
SELECT SUM(playcount) FROM rx_beatmap_playcount WHERE user_id = 1000 AND game_mode = 0;
SELECT rx_stats.* FROM rx_stats LEFT JOIN users ON users.id = rx_stats.id WHERE users.privileges NOT IN (0) AND users.privileges NOT IN (2) ORDER BY pp_std DESC;
