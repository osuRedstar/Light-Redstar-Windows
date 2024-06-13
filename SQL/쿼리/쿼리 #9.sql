SELECT scores_relax.score, scores_relax.completed, beatmaps.ranked
                               FROM scores_relax
                               LEFT JOIN beatmaps ON scores_relax.beatmap_md5 = beatmaps.beatmap_md5
                               WHERE
                                scores_relax.userid = 1000 AND
                                scores_relax.play_mode = 0