-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.4.28-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 테이블 py_gull.beatmaps 구조 내보내기
CREATE TABLE IF NOT EXISTS `beatmaps` (
  `id` int(11) NOT NULL,
  `parent_set_id` int(11) NOT NULL,
  `diff_name` varchar(1000) DEFAULT NULL,
  `Filename` longtext DEFAULT NULL,
  `file_md5` char(32) DEFAULT NULL,
  `mode` int(11) DEFAULT NULL,
  `bpm` decimal(10,4) DEFAULT NULL,
  `ar` decimal(4,2) DEFAULT NULL,
  `od` decimal(4,2) DEFAULT NULL,
  `cs` decimal(4,2) DEFAULT NULL,
  `hp` decimal(4,2) DEFAULT NULL,
  `total_length` int(11) DEFAULT NULL,
  `hit_length` int(11) DEFAULT NULL,
  `playcount` int(11) DEFAULT NULL,
  `passcount` int(11) DEFAULT NULL,
  `max_combo` int(11) DEFAULT NULL,
  `difficulty_rating` decimal(20,15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_set_id` (`parent_set_id`),
  KEY `file_md5` (`file_md5`) USING BTREE,
  KEY `Filename` (`Filename`(768)) USING BTREE,
  FULLTEXT KEY `diff_name` (`diff_name`),
  CONSTRAINT `beatmaps_ibfk_1` FOREIGN KEY (`parent_set_id`) REFERENCES `sets` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 py_gull.db_version 구조 내보내기
CREATE TABLE IF NOT EXISTS `db_version` (
  `version` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 py_gull.download_status 구조 내보내기
CREATE TABLE IF NOT EXISTS `download_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bsid` int(11) DEFAULT NULL,
  `filename` longtext DEFAULT NULL,
  `http_statusCode` smallint(3) DEFAULT NULL,
  `Exception` longtext DEFAULT NULL,
  `update_time` bigint(20) DEFAULT unix_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111222 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 py_gull.sets 구조 내보내기
CREATE TABLE IF NOT EXISTS `sets` (
  `id` int(11) NOT NULL,
  `ranked_status` tinyint(4) DEFAULT NULL,
  `approved_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  `last_checked` datetime NOT NULL,
  `artist` varchar(1000) DEFAULT NULL,
  `artist_unicode` varchar(1000) DEFAULT NULL,
  `title` varchar(1000) DEFAULT NULL,
  `title_unicode` varchar(1000) DEFAULT NULL,
  `creator` varchar(1000) DEFAULT NULL,
  `source` varchar(1000) DEFAULT NULL,
  `tags` varchar(1000) DEFAULT NULL,
  `has_video` tinyint(4) DEFAULT NULL,
  `genre` tinyint(4) DEFAULT NULL,
  `language` tinyint(4) DEFAULT NULL,
  `favourites` int(11) DEFAULT NULL,
  `set_modes` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `artist` (`artist`,`title`,`creator`,`source`,`tags`,`artist_unicode`,`title_unicode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
