SELECT id, username, total_score_std, ranked_score_std, pp_std, avg_accuracy_std FROM rx_stats;
SELECT id, username, total_score_taiko, ranked_score_taiko, pp_taiko, avg_accuracy_taiko FROM rx_stats;
SELECT id, username, total_score_std, ranked_score_std, pp_std, avg_accuracy_std FROM users_stats;
SELECT * FROM scores_relax WHERE userid = 1000;
SELECT SUM(score) FROM scores_relax WHERE userid = 1078;
SELECT SUM(accuracy)as AllAccuracy, COUNT(accuracy) as CountAccuracy FROM scores_relax WHERE userid = 1078 AND play_mode = 0 AND completed = 3;
SELECT SUM(pp) FROM scores_relax WHERE userid = 1078 AND completed = 3;