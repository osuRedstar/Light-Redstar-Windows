SELECT * FROM beatmaps WHERE beatmaps.beatmapset_id=1777613;
SELECT * FROM beatmaps WHERE beatmaps.beatmap_id=3640352;
SELECT playcount, passcount, id, beatmap_id, beatmapset_id, beatmap_md5, song_name FROM beatmaps WHERE beatmaps.playcount NOT IN (0);
SELECT * FROM beatmaps WHERE beatmaps.beatmap_md5='d40e655e59488e056272d947df2f62fd';
SELECT beatmap_id FROM beatmaps WHERE beatmap_md5='8999bab2aed4bce24a03288db629133b';
SELECT beatmap_id, id FROM beatmaps WHERE beatmap_id NOT IN (0);
SELECT beatmap_id, id FROM beatmaps WHERE beatmap_id NOT IN (0) AND difficulty_ctb NOT IN (0) AND	difficulty_mania NOT	IN	(0);