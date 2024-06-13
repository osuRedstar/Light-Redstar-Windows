-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- 생성 시간: 24-01-31 22:03
-- 서버 버전: 10.4.28-MariaDB
-- PHP 버전: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 데이터베이스: `redstar`
--

-- --------------------------------------------------------

--
-- 테이블 구조 `1_beatmap_deleted_by_bancho`
--

CREATE TABLE `1_beatmap_deleted_by_bancho` (
  `beatmap_id` int(11) DEFAULT NULL,
  `beatmapset_id` int(11) DEFAULT NULL,
  `beatmap_md5` varchar(32) DEFAULT NULL,
  `song_name` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 테이블의 덤프 데이터 `1_beatmap_deleted_by_bancho`
--

INSERT INTO `1_beatmap_deleted_by_bancho` (`beatmap_id`, `beatmapset_id`, `beatmap_md5`, `song_name`) VALUES
(2251881, 1076207, '450d01200f15a7f05d56ff5bc437bc56', 'Aqours - Thank you, FRIENDS!! (ginka*EX -Farewell Remix-) [Eternal Friends!]'),
(2160880, 1033468, '70dbb28a199429c470aabe22b188c38c', 'Aqours - Thank you, FRIENDS!! (ginka*EX -Farewell Remix-) [Thank you!!]'),
(3160717, 1522743, '067f5912c72932333d3b2c245c492482', 'Hoshimi Production - Sayonara Kara Hajimaru Monogatari [Normal]'),
(3420645, 1674503, '115bb57b134c48ddd4000fc4aee69316', 'Morishita Chisaki, Tanaka Minami, Kito Akari, Kurose Yuuko - Hitoribocchi no Monologue (nenpulse bootleg remix) [Mania]'),
(2544555, 1223333, 'b0011c90f03ec059e0fea4631899a237', 'Reol - -Interlude- [Pause]'),
(2544551, 1223333, 'e703752bca3036a7d49b5872d3827461', 'Reol - -Interlude- [Extra]'),
(2544553, 1223333, 'd5601d6e1a7a816b120ec68b0c199fad', 'Reol - -Interlude- [Insane]'),
(2544552, 1223333, '4a584cdcbd321efc41fb2245097bdc4f', 'Reol - -Interlude- [Hard]'),
(2544554, 1223333, 'd17b9bf3fcc9150f9e260cbe6519ed21', 'Reol - -Interlude- [Normal]'),
(2544550, 1223333, '2811a2fbe59fa0787b28dc075f51506e', 'Reol - -Interlude- [Easy]'),
(1821147, 871623, 'c63869b2073a801a6fd0c79823c5da8d', 'xi - over the top [Above the stars]'),
(2835543, 1371444, '87690c781c78108272e336bb410e3206', 'PinocchioP - sukisukisukisukisukisukisukisukisukisuki [Sukisuki Stream]'),
(2518796, 1209819, '3e6fa5c199d289481f15883946196975', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [Normal]'),
(2518795, 1209819, '5faf5972ba2d67090a25a424e1fbaf85', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [Hard]'),
(2518797, 1209819, 'bcf57fe84d57163fbdf38512187b0a74', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [Onlybiscuit\'s Insane]'),
(2521422, 1209819, 'eba5fd430fe3074085ed0abdb3801e38', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [Reform\'s Expert]'),
(2554640, 1209819, 'f91e7b92ea0dd057bcad23279063df6e', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [browiec\'s Extra]'),
(2518794, 1209819, '4d846b25d0c9d1f350644d492888873f', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [Extra]'),
(2518798, 1209819, '99ca05ef362b4f5e7bf796a8f423e46e', 'ONE OK ROCK - Skyfall (feat. Koie of Crossfaith, MAH of SiM and Masato Hayakawa of Coldrain) [Sotarks\' Collapse]'),
(2779880, 1342003, '7646a1631fd920c9967b5bb38cc58484', 't+pazolite - Tempestissimo (Uncut Edition) [ToTheFuture]'),
(2386572, 1111963, '3b0e0f31ab105528896eaedd06acea4c', 'mafumafu - I wanna be a girl [Easy]'),
(2386574, 1111963, 'e5c0672018b92e71da75b2d24195d999', 'mafumafu - I wanna be a girl [Normal]'),
(2323202, 1111963, 'e9172a83af80d89a8da0dd5e437fdc16', 'mafumafu - I wanna be a girl [Cinderella]'),
(1778043, 850425, '7b94cb02d8258f60d010cfa8e7488055', 'High Driver join. SELEN ft. Daler Mehndi - DADADADADADADADADADA (Indian Friendly ver.) [KurtDaWeeb]'),
(2493865, 1197242, '08b1b956dc4f6ae03cf62b8144be21f0', 'ke-ji feat. Nanahira - Ange du Blanc Pur (Short Ver.) [Forbidden Heaven]'),
(3873162, 1881274, 'f0a5a7ac97d489860681c24dd207d53f', 'OverNote\' (I will delete this map) - Hyperorbit (I will delete this map) [(I will delete this map)]'),
(3569232, 1745015, '59515ad46ba5723d76c69088b94201fd', 'Camellia - Hello (BPM) 2021 [Time Machine]'),
(2772701, 1275778, '7e562b958e942bb4810ce47000bef330', 'Theocracy - Mirror of Souls [I: The House of Mirrors]'),
(3520404, 1524066, 'f9c4735fcee7a289f06fe89cd55c6a9a', 'IOSYS - SCARLET KEISATSU no GHETTO PATROL 24-ji [PERFECT MATH LUNATIC]'),
(3522050, 1524066, 'a15106d6fdff1eb9290010e8bd4d2117', 'IOSYS - SCARLET KEISATSU no GHETTO PATROL 24-ji [MIN\'S HARD]'),
(1525892, 722837, '0f01a609ee79102ccdb9e55539142ea4', 'Nereidus - Top 5 Bad Words [Hard]'),
(3800865, 1850229, 'd04dbdbb263ddd3c73fb2147ee6b1a55', 'Various Artists - CS-0 Polish Jump Training [Psalm dla Ciebie [Yusomi\'s Pieczec na sercu] AR9]'),
(3763246, 1832963, '61b78f8529d07bf0b0605928930360e0', 'Turbo - PADORU / PADORU [Milles\' ULTIMATE X-MAS]'),
(3522617, 1529141, 'e9b77cb4a3716690786a136010765c63', 'Ata - I\'m Not Crazy [Hell Stream]'),
(3522618, 1529141, '92c02b835a2036328c498fa56885fccd', 'Ata - I\'m Not Crazy [Juggernaut]'),
(3800855, 1850229, '9bedb67a9eead118fdd04a362147d0cf', 'Various Artists - CS-0 Polish Jump Training [Gdzie Moja Wolnosc (Cut Ver.) [gdzie moja swoboda]]'),
(3800890, 1850233, '6564d11058f68bfff7445a28bfa72c56', 'Various Artists - CS-0 Polish Jump Training 2 [Zero Calorie Cookie [jumpy bez cukru ale z nebu]]'),
(2798390, 1263883, '67380669aef3df00d9a20b2a665c7339', 'Kobaryo - Theme for Psychopath Justice [araran\'s Extreme]'),
(2627024, 1263883, 'af4862af53317be74b0b68068d0a2aa1', 'Kobaryo - Theme for Psychopath Justice [-/-]'),
(2895234, 1263883, '967d441b1cb6d5571c7cb24fe5c4bc52', 'Kobaryo - Theme for Psychopath Justice [Normal]'),
(2787763, 1263883, '8abe355d5039af4176c0ceb09906206d', 'Kobaryo - Theme for Psychopath Justice [Hard]'),
(2660218, 1263883, 'f138febefff9c0000ae9b4ff2f95ff65', 'Kobaryo - Theme for Psychopath Justice [Kawa\'s Insane]'),
(2669504, 1263883, '5c0c720527e94d81610b5b8810d71615', 'Kobaryo - Theme for Psychopath Justice [milr_\'s Expert]'),
(2894007, 1263883, 'f1a0d4bcd6b553eb6892df131e754b73', 'Kobaryo - Theme for Psychopath Justice [Lulu\'s Dissociative Identity Extra]'),
(2627229, 1263883, 'daf9f77552033862c0cc1f42c2bd95be', 'Kobaryo - Theme for Psychopath Justice [s0m3guy\'s Psychotic Extreme]'),
(2901679, 1263883, '6ed4485a6a7ace115f5847598c3a42d3', 'Kobaryo - Theme for Psychopath Justice [Heilia\'s Extreme]'),
(3114456, 1263883, '1cddfd0d5ead5fe8d0709ec72ea5df34', 'Kobaryo - Theme for Psychopath Justice [Necho]'),
(2895995, 1263883, '1d94d0458b7e9dde5e70c0b2587e4c14', 'Kobaryo - Theme for Psychopath Justice [Extreme]'),
(2639872, 1263883, '44a42c5c7f195fe5c48835da58e45829', 'Kobaryo - Theme for Psychopath Justice [Atri\'s Unerasable Distortion Extreme]'),
(2658438, 1263883, 'f24567213bd32eaaf21f52d515a11dc2', 'Kobaryo - Theme for Psychopath Justice [R3m\'s Disillusionate Soul]'),
(3359920, 1221014, 'd10e3d0f71ee6c0b4fb4a49c2680740b', 'Inugami Korone & Nekomata Okayu - Hyadain\'s Jojo Yujo [iPhong\'s Friendly Extra]'),
(2611041, 1139182, '907caa0a83a7f1d041c0fe44acdcf5bc', 'Marmalade butcher - Amanita [Hard]'),
(3800847, 1850229, '30a42d91da94718d605eebec46c72e47', 'Various Artists - CS-0 Polish Jump Training [Czyszczenie Magazynow w Media Expert [RAFIS FCNIJ TO PLS NaM] AR9]'),
(1034416, 485018, 'f68c8e9fc990f3bde17d70a857bf4db8', 'IAHN - Transform (Original Mix) [Marathon]'),
(3051172, 1333715, 'ff2382bcca0e1d22f77e367f17baa09e', 'Plum - Mad Piano Party [Hyper]'),
(3796439, 1846585, '8af698313a1f209880a3e9cfc5af5ec6', 'Various Artists - Songs Compilation [hitsound]'),
(1686644, 803601, '7df9cd6cb43d2b7857812983b40bc13d', 'Various Artists - -Mystic\'s Megapack Side C [#Marathon]'),
(3814580, 1856222, '25e9f32522f34dc110ca4daa6e1deac3', 'Various Artists - Dan  ~ REFORM ~ Missing Finalmaps Pack [# STAMINA ~ Image -MATERIAL- ~ Zeta]'),
(3867289, 1878701, 'b166fde01274c2aa58042a305bbdaf7a', 'Eve - Last Dance [p]'),
(3515344, 1718137, '39e2dc0e17635a9825860be5e3145a32', 'Flypie743 - Jackhammer Madness [220 BPM 1/4 Hanbun MugenxD Ura Muzukashii]'),
(3876741, 1882945, 'a599b691225ccadec0fa12f24ccf75a9', 'C418 - Subwoofer Lullaby [Cocoamallows\' Kantan]'),
(3386826, 1659103, 'a94972c1e223f2d541fccb212fbd8b09', 'Gwen Stefani - The Sweet Escape (Speed up) [Fast rap bit or somethin]'),
(3515390, 1718137, '5b8d711befcfb89a62d2ea4fc0c4ec9f', 'Flypie743 - Jackhammer Madness [240 BPM 1/4 Hanbun MugenxD Ura Muzukashii]'),
(3694783, 1797744, '533d5d22e3f5106a0a568ab9baf3ad5a', 'CHiCO with HoneyWorks - Himitsu Koigokoro (TV Size) [Sebas\' Girlfriend]'),
(2636233, 1265919, 'f29fe914d9abb8cd93d3a9d5a92425d5', 'Iyaz - Replay (Speed Up Ver.) [hhjkl\'s bunny]'),
(2632260, 1265919, '4d19dff51220543d9a3c547f5ae6e7b0', 'Iyaz - Replay (Speed Up Ver.) [Strawberric Melody]'),
(2631034, 1265919, 'fb157813f6f2f6f87712a86b5b91e542', 'Iyaz - Replay (Speed Up Ver.) [Repeating Memories]'),
(3800866, 1850229, '3d3cfd3ab20ee9b6b3724d14cf69ff50', 'Various Artists - CS-0 Polish Jump Training [Reklama T-Mobile [Jestes w T-Mobile?]]'),
(3800883, 1850233, '3147cad8b9b97df69989e7d884b7cee2', 'Various Artists - CS-0 Polish Jump Training 2 [Szpital [Dlugosc telewizyjna] [DominiGG\'s Pielegniarka]]'),
(1242420, 586710, '50c8a622f1fc75bd114949d2762e3827', 'Meramipop - Shinkirou [Mask]'),
(2661497, 1281361, '6d9f258b31e407d1be9fcae53a9fafe9', 'Laur - Alteregoism [Alter Ego]'),
(2661854, 1281361, '62069ec837cd22161fece7b8d391f8d3', 'Laur - Alteregoism [Easy]'),
(2661503, 1281361, '3ac82f41c1d5858d711f7c5202bb3ec4', 'Laur - Alteregoism [Normal]'),
(2661501, 1281361, 'f677e21915a071e697f17f4427dedcb7', 'Laur - Alteregoism [Hard]'),
(2661502, 1281361, 'af8e94fbd3c916c3da6936ea14fa697f', 'Laur - Alteregoism [Insane]'),
(2661498, 1281361, '76745a3461141a70466b376ea91c0523', 'Laur - Alteregoism [Another]'),
(2661500, 1281361, '1b3462851113d68c43b6db096fd30bfb', 'Laur - Alteregoism [Extra]'),
(2661499, 1281361, 'a7b6d04c3dde279738ec9fa4496b8d38', 'Laur - Alteregoism [Doppelganger]'),
(2996098, 1457848, '1b7fae76323f4ac65f4bcb2081ad04c5', 'Laur - alteregoism [3rd]'),
(3033989, 1457848, '83a9e42839d8ad5415114ad3d6a149a6', 'Laur - alteregoism [nerfed for me]'),
(2290222, 1095816, 'e31a2c140ce896d415140def18a679cc', '3R2 - Spring Carnival [Happycore Holiday]'),
(3942173, 1910726, '5a73c527d3c3a0d695219b7a1a86d06b', 'Enako feat. Pmarusama. - Iden Tei Tei Meltdown (TV Size) [hs]'),
(3821685, 1859134, '018322921f8568d6d96d9b4706aaf2a4', 'MIMI feat. wanko - Minimum [Hitsounds (DO NOT PLAY)]'),
(1425688, 673693, 'c26ceb082b7e56ecb356338224c5c70d', 'Sithu Aye - Solstice [Dawn of a New Day]'),
(2239999, 1070111, '3eb33789248b07c33bfbba1303a2e0ca', 'Sound Horizon - Rein no Sekai [Zelly\'s Sekai]'),
(3018465, 1470151, '07f0384ae92568db64a46645c1fceaa3', 'KAMELOT - Kevlar Skin [Insane 1.65x (270bpm) AR9.8]'),
(1907733, 913261, '2a4e20f0c04c026e5aee2f88bc142333', 'Minami - Kawaki wo Ameku (TV Size) [The one thing I don\'t want is ambiguousness]'),
(2449723, 1174468, 'f817e903ab2cc18ccb6737f39562bc8b', 'Wakeshima Kanon - fragment ornament [panda WIP]'),
(2379651, 1139182, 'ee8e1c31b395447f58f88f2f13576cce', 'Marmalade butcher - Amanita [Collab Expert]'),
(3033226, 1478500, 'eb09d17eb74f7ad5e7fffa7e529bf5ba', '$44,000 - PISSCORD [pisscord crown goes to pekora]'),
(1704941, 812906, 'fda3b9c9f06d1b0999c7ee775f041099', 'LOONA/Go Won - One & Only [Crunchy]'),
(2374704, 1135214, 'a844be0a4f7ded3291ec8ea526a2d1ce', 'kaneko chiharu - poxei*DOON [Blue Ocean]');

-- --------------------------------------------------------

--
-- 테이블 구조 `2fa`
--

CREATE TABLE `2fa` (
  `userid` int(11) NOT NULL,
  `ip` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `2fa_telegram`
--

CREATE TABLE `2fa_telegram` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `2fa_totp`
--

CREATE TABLE `2fa_totp` (
  `enabled` tinyint(1) NOT NULL DEFAULT 0,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `achievements`
--

CREATE TABLE `achievements` (
  `id` int(11) NOT NULL,
  `name` mediumtext NOT NULL,
  `description` mediumtext NOT NULL,
  `icon` mediumtext NOT NULL,
  `version` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `achievements`
--

INSERT INTO `achievements` (`id`, `name`, `description`, `icon`, `version`) VALUES
(1, '500 Combo (osu!std)', '500 big ones! You\'re moving up in the world!', 'osu-combo-500', 1),
(2, '750 Combo (osu!std)', '750 big ones! You\'re moving up in the world!', 'osu-combo-750', 1),
(3, '1000 Combo (osu!std)', '1000 big ones! You\'re moving up in the world!', 'osu-combo-1000', 1),
(4, '2000 Combo (osu!std)', '2000 big ones! You\'re moving up in the world!', 'osu-combo-2000', 1),
(5, '500 Combo (osu!taiko)', '500 big ones! You\'re moving up in the world!', 'osu-combo-500', 1),
(6, '750 Combo (osu!taiko)', '750 big ones! You\'re moving up in the world!', 'osu-combo-750', 1),
(7, '1000 Combo (osu!taiko)', '1000 big ones! You\'re moving up in the world!', 'osu-combo-1000', 1),
(8, '2000 Combo (osu!taiko)', '2000 big ones! You\'re moving up in the world!', 'osu-combo-2000', 1),
(9, '500 Combo (osu!ctb)', '500 big ones! You\'re moving up in the world!', 'osu-combo-500', 1),
(10, '750 Combo (osu!ctb)', '750 big ones! You\'re moving up in the world!', 'osu-combo-750', 1),
(11, '1000 Combo (osu!ctb)', '1000 big ones! You\'re moving up in the world!', 'osu-combo-1000', 1),
(12, '2000 Combo (osu!ctb)', '2000 big ones! You\'re moving up in the world!', 'osu-combo-2000', 1),
(13, '500 Combo (osu!mania)', '500 big ones! You\'re moving up in the world!', 'osu-combo-500', 1),
(14, '750 Combo (osu!mania)', '750 big ones! You\'re moving up in the world!', 'osu-combo-750', 1),
(15, '1000 Combo (osu!mania)', '1000 big ones! You\'re moving up in the world!', 'osu-combo-1000', 1),
(16, '2000 Combo (osu!mania)', '2000 big ones! You\'re moving up in the world!', 'osu-combo-2000', 1),
(17, 'Rising Star', 'Can\'t go forward without the first steps.', 'osu-skill-pass-1', 2),
(18, 'My First Don', 'Can\'t go forward without the first steps.', 'taiko-skill-pass-1', 2),
(19, 'A Slice Of Life', 'Can\'t go forward without the first steps.', 'fruits-skill-pass-1', 2),
(20, 'First Steps', 'Can\'t go forward without the first steps.', 'mania-skill-pass-1', 2),
(21, 'Constellation Prize', 'Definitely not a consolation prize. Now things start getting hard!', 'osu-skill-pass-2', 2),
(22, 'Katsu Katsu Katsu', 'Definitely not a consolation prize. Now things start getting hard!', 'taiko-skill-pass-2', 2),
(23, 'Dashing Ever Forward', 'Definitely not a consolation prize. Now things start getting hard!', 'fruits-skill-pass-2', 2),
(24, 'No Normal Player', 'Definitely not a consolation prize. Now things start getting hard!', 'mania-skill-pass-2', 2),
(25, 'Building Confidence', 'Oh, you\'ve SO got this.', 'osu-skill-pass-3', 2),
(26, 'Not Even Trying', 'Oh, you\'ve SO got this.', 'taiko-skill-pass-3', 2),
(27, 'Zesty Disposition', 'Oh, you\'ve SO got this.', 'fruits-skill-pass-3', 2),
(28, 'Impulse Drive', 'Oh, you\'ve SO got this.', 'mania-skill-pass-3', 2),
(29, 'Insanity Approaches', 'You\'re not twitching, you\'re just ready.', 'osu-skill-pass-4', 2),
(30, 'Face Your Demons', 'You\'re not twitching, you\'re just ready.', 'taiko-skill-pass-4', 2),
(31, 'Hyperdash ON!', 'You\'re not twitching, you\'re just ready.', 'fruits-skill-pass-4', 2),
(32, 'Hyperspeed', 'You\'re not twitching, you\'re just ready.', 'mania-skill-pass-4', 2),
(33, 'These Clarion Skies', 'Everything seems so clear now.', 'osu-skill-pass-5', 2),
(34, 'The Demon Within', 'Everything seems so clear now.', 'taiko-skill-pass-5', 2),
(35, 'It\'s Raining Fruit', 'Everything seems so clear now.', 'fruits-skill-pass-5', 2),
(36, 'Ever Onwards', 'Everything seems so clear now.', 'mania-skill-pass-5', 2),
(37, 'Above and Beyond', 'A cut above the rest.', 'osu-skill-pass-6', 2),
(38, 'Drumbreaker', 'A cut above the rest.', 'taiko-skill-pass-6', 2),
(39, 'Fruit Ninja', 'A cut above the rest.', 'fruits-skill-pass-6', 2),
(40, 'Another Surpassed', 'A cut above the rest.', 'mania-skill-pass-6', 2),
(41, 'Supremacy', 'All marvel before your prowess.', 'osu-skill-pass-7', 2),
(42, 'The Godfather', 'All marvel before your prowess.', 'taiko-skill-pass-7', 2),
(43, 'Dreamcatcher', 'All marvel before your prowess.', 'fruits-skill-pass-7', 2),
(44, 'Extra Credit', 'All marvel before your prowess.', 'mania-skill-pass-7', 2),
(45, 'Absolution', 'My god, you\'re full of stars!', 'osu-skill-pass-8', 2),
(46, 'Rhythm Incarnate', 'My god, you\'re full of stars!', 'taiko-skill-pass-8', 2),
(47, 'Lord of the Catch', 'My god, you\'re full of stars!', 'fruits-skill-pass-8', 2),
(48, 'Maniac', 'My god, you\'re full of stars!', 'mania-skill-pass-8', 2),
(49, 'Totality', 'All the notes. Every single one.', 'osu-skill-fc-1', 3),
(50, 'Keeping Time', 'All the notes. Every single one.', 'taiko-skill-fc-1', 3),
(51, 'Sweet And Sour', 'All the notes. Every single one.', 'fruits-skill-fc-1', 3),
(52, 'Keystruck', 'All the notes. Every single one.', 'mania-skill-fc-1', 3),
(53, 'Business As Usual', 'Two to go, please.', 'osu-skill-fc-2', 3),
(54, 'To Your Own Beat', 'Two to go, please.', 'taiko-skill-fc-2', 3),
(55, 'Reaching The Core', 'Two to go, please.', 'fruits-skill-fc-2', 3),
(56, 'Keying In', 'Two to go, please.', 'mania-skill-fc-2', 3),
(57, 'Building Steam', 'Hey, this isn\'t so bad.', 'osu-skill-fc-3', 3),
(58, 'Big Drums', 'Hey, this isn\'t so bad.', 'taiko-skill-fc-3', 3),
(59, 'Clean Platter', 'Hey, this isn\'t so bad.', 'fruits-skill-fc-3', 3),
(60, 'Hyperflow', 'Hey, this isn\'t so bad.', 'mania-skill-fc-3', 3),
(61, 'Moving Forward', 'Bet you feel good about that.', 'osu-skill-fc-4', 3),
(62, 'Adversity Overcome', 'Bet you feel good about that.', 'taiko-skill-fc-4', 3),
(63, 'Between The Rain', 'Bet you feel good about that.', 'fruits-skill-fc-4', 3),
(64, 'Breakthrough', 'Bet you feel good about that.', 'mania-skill-fc-4', 3),
(65, 'Paradigm Shift', 'Surprisingly difficult.', 'osu-skill-fc-5', 3),
(66, 'Demonslayer', 'Surprisingly difficult.', 'taiko-skill-fc-5', 3),
(67, 'Addicted', 'Surprisingly difficult.', 'fruits-skill-fc-5', 3),
(68, 'Everything Extra', 'Surprisingly difficult.', 'mania-skill-fc-5', 3),
(69, 'Anguish Quelled', 'Don\'t choke.', 'osu-skill-fc-6', 3),
(70, 'Rhythm\'s Call', 'Don\'t choke.', 'taiko-skill-fc-6', 3),
(71, 'Quickening', 'Don\'t choke.', 'fruits-skill-fc-6', 3),
(72, 'Level Breaker', 'Don\'t choke.', 'mania-skill-fc-6', 3),
(73, 'Never Give Up', 'Excellence is its own reward.', 'osu-skill-fc-7', 3),
(74, 'Time Everlasting', 'Excellence is its own reward.', 'taiko-skill-fc-7', 3),
(75, 'Supersonic', 'Excellence is its own reward.', 'fruits-skill-fc-7', 3),
(76, 'Step Up', 'Excellence is its own reward.', 'mania-skill-fc-7', 3),
(77, 'Aberration', 'They said it couldn\'t be done. They were wrong.', 'osu-skill-fc-8', 3),
(78, 'The Drummer\'s Throne', 'They said it couldn\'t be done. They were wrong.', 'taiko-skill-fc-8', 3),
(79, 'Dashing Scarlet', 'They said it couldn\'t be done. They were wrong.', 'fruits-skill-fc-8', 3),
(80, 'Behind The Veil', 'They said it couldn\'t be done. They were wrong.', 'mania-skill-fc-8', 3),
(81, 'Finality', 'High stakes, no regrets.', 'all-intro-suddendeath', 4),
(82, 'Perfectionist', 'Accept nothing but the best.', 'all-intro-perfect', 4),
(83, 'Rock Around The Clock', 'You can\'t stop the rock.', 'all-intro-hardrock', 4),
(84, 'Time And A Half', 'Having a right ol\' time. One and a half of them, almost.', 'all-intro-doubletime', 4),
(85, 'Sweet Rave Party', 'Founded in the fine tradition of changing things that were just fine as they were.', 'all-intro-nightcore', 4),
(86, 'Blindsight', 'I can see just perfectly.', 'all-intro-hidden', 4),
(87, 'Are You Afraid Of The Dark?', 'Harder than it looks, probably because it\'s hard to look.', 'all-intro-flashlight', 4),
(88, 'Dial It Right Back', 'Sometimes you just want to take it easy.', 'all-intro-easy', 4),
(89, 'Risk Averse', 'Safety nets are fun!', 'all-intro-nofail', 4),
(90, 'Slowboat', 'You got there. Eventually.', 'all-intro-halftime', 4),
(91, 'Burned Out', 'One cannot always spin to win.', 'all-intro-spunout', 4),
(92, '5,000 Plays', 'There\'s a lot more where that came from.', 'osu-plays-5000', 5),
(93, '15,000 Plays', 'Must.. click.. circles..', 'osu-plays-15000', 5),
(94, '25,000 Plays', 'There\'s no going back.', 'osu-plays-25000', 5),
(95, '50,000 Plays', 'You\'re here forever.', 'osu-plays-50000', 5),
(96, 'A meganekko approaches', 'Congratulations, you met Maria!', 'mania-secret-meganekko', 6),
(97, 'Don\'t let the bunny distract you!', 'The order was indeed, not a rabbit.', 'all-secret-bunny', 6);

-- --------------------------------------------------------

--
-- 테이블 구조 `anticheat_reports`
--

CREATE TABLE `anticheat_reports` (
  `id` int(11) NOT NULL,
  `anticheat_id` int(11) NOT NULL,
  `score_id` int(11) NOT NULL,
  `severity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `ap_beatmap_playcount`
--

CREATE TABLE `ap_beatmap_playcount` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `beatmap_id` int(11) DEFAULT NULL,
  `game_mode` int(11) DEFAULT NULL,
  `playcount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- 테이블 구조 `ap_stats`
--

CREATE TABLE `ap_stats` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `username_aka` varchar(100) NOT NULL DEFAULT '',
  `user_color` varchar(16) NOT NULL DEFAULT 'black',
  `user_style` varchar(128) NOT NULL DEFAULT '',
  `favourite_mode` int(11) NOT NULL DEFAULT 0,
  `level_std` int(11) NOT NULL DEFAULT 1,
  `level_taiko` int(11) NOT NULL DEFAULT 1,
  `level_mania` int(11) NOT NULL DEFAULT 1,
  `level_ctb` int(11) NOT NULL DEFAULT 1,
  `total_score_std` int(11) NOT NULL DEFAULT 0,
  `total_score_taiko` int(11) NOT NULL DEFAULT 0,
  `total_score_mania` int(11) NOT NULL DEFAULT 0,
  `total_score_ctb` int(11) NOT NULL DEFAULT 0,
  `total_hits_std` int(11) NOT NULL DEFAULT 0,
  `total_hits_taiko` int(11) NOT NULL DEFAULT 0,
  `total_hits_ctb` int(11) NOT NULL DEFAULT 0,
  `total_hits_mania` int(11) NOT NULL DEFAULT 0,
  `playtime_std` int(11) NOT NULL DEFAULT 0,
  `playtime_taiko` int(11) NOT NULL DEFAULT 0,
  `playtime_mania` int(11) NOT NULL DEFAULT 0,
  `playtime_ctb` int(11) NOT NULL DEFAULT 0,
  `ranked_score_std` bigint(11) NOT NULL DEFAULT 0,
  `ranked_score_taiko` int(11) NOT NULL DEFAULT 0,
  `ranked_score_mania` int(11) NOT NULL DEFAULT 0,
  `ranked_score_ctb` int(11) NOT NULL DEFAULT 0,
  `avg_accuracy_std` double NOT NULL DEFAULT 0,
  `avg_accuracy_taiko` double NOT NULL DEFAULT 0,
  `avg_accuracy_mania` double NOT NULL DEFAULT 0,
  `avg_accuracy_ctb` double NOT NULL DEFAULT 0,
  `playcount_std` int(11) NOT NULL DEFAULT 0,
  `playcount_taiko` int(11) NOT NULL DEFAULT 0,
  `playcount_mania` int(11) NOT NULL DEFAULT 0,
  `playcount_ctb` int(11) NOT NULL DEFAULT 0,
  `pp_std` int(11) NOT NULL DEFAULT 0,
  `pp_mania` int(11) NOT NULL DEFAULT 0,
  `pp_ctb` int(11) NOT NULL DEFAULT 0,
  `pp_taiko` int(11) NOT NULL DEFAULT 0,
  `country` char(2) NOT NULL DEFAULT 'XX',
  `unrestricted_pp` int(11) NOT NULL DEFAULT 0,
  `ppboard` int(11) NOT NULL DEFAULT 1,
  `replays_watched_std` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `replays_watched_taiko` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `replays_watched_ctb` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `replays_watched_mania` int(11) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci ROW_FORMAT=DYNAMIC;

--
-- 테이블의 덤프 데이터 `ap_stats`
--

INSERT INTO `ap_stats` (`id`, `username`, `username_aka`, `user_color`, `user_style`, `favourite_mode`, `level_std`, `level_taiko`, `level_mania`, `level_ctb`, `total_score_std`, `total_score_taiko`, `total_score_mania`, `total_score_ctb`, `total_hits_std`, `total_hits_taiko`, `total_hits_ctb`, `total_hits_mania`, `playtime_std`, `playtime_taiko`, `playtime_mania`, `playtime_ctb`, `ranked_score_std`, `ranked_score_taiko`, `ranked_score_mania`, `ranked_score_ctb`, `avg_accuracy_std`, `avg_accuracy_taiko`, `avg_accuracy_mania`, `avg_accuracy_ctb`, `playcount_std`, `playcount_taiko`, `playcount_mania`, `playcount_ctb`, `pp_std`, `pp_mania`, `pp_ctb`, `pp_taiko`, `country`, `unrestricted_pp`, `ppboard`, `replays_watched_std`, `replays_watched_taiko`, `replays_watched_ctb`, `replays_watched_mania`) VALUES
(999, 'Devlant', 'BOT', 'black', '', 0, 1, 1, 1, 1, 731057828, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 731057828, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'JP', 1, 1, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- 테이블 구조 `badges`
--

CREATE TABLE `badges` (
  `id` int(11) NOT NULL,
  `name` varchar(21485) NOT NULL,
  `icon` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `badges`
--

INSERT INTO `badges` (`id`, `name`, `icon`) VALUES
(1, '', ''),
(2, 'Developers', 'teal blind'),
(3, 'Bug Hunter', 'red bug'),
(4, 'Community Manager', 'orange comments'),
(5, 'Beatmap Nominators', 'blue angle double up'),
(10, 'SUSPICIOUS - WAITING FOR CHECK', 'red window close outline'),
(30, 'Chat Moderators', 'envelope outline'),
(999, 'FP', 'fa-plane'),
(1000, 'Thumbnail Maker', 'fa-thumbs-o-up'),
(1001, 'Marathon Runner', 'green recycle'),
(1002, '☆ Supporter ☆', 'red star'),
(1003, 'UA', 'universal access'),
(1005, 'Bot', 'blue shield alternate'),
(1006, '#1 Relax #Weekly (osu!)', 'fa-fighter-jet'),
(1007, '#1 Relax #Weekly (Catch The Beat)', 'fa-fighter-jet'),
(1009, '#1 Relax #Weekly (Taiko)', 'fa-fighter-jet'),
(1010, '#1 Vanilla #Weekly (osu!)', 'fa-fighter-jet'),
(1011, '#1 Vanilla #Weekly (Mania)', 'fa-fighter-jet'),
(1012, '#1 Vanilla #Weekly (Catch The Beat)', 'fa-fighter-jet'),
(1013, '#1 Vanilla #Weekly (Taiko)', 'fa-fighter-jet'),
(1014, 'Debian User!!', 'purple heart'),
(1015, 'Alpha Tester', 'yellow amazon'),
(1016, 'Beta Tester', 'purple btc'),
(1017, 'Approved Nominator', 'red fire'),
(1018, 'osu! Standard Champion', 'flag checkered'),
(1019, 'osu! Taiko Champion', 'flag checkered'),
(1020, 'osu! CTB Champion', 'flag checkered'),
(1021, 'osu! Mania Champion', 'flag checkered'),
(1022, 'Relax! Standard Champion', 'flag checkered'),
(1023, 'Relax! Taiko Champion', 'flag checkered'),
(1024, 'Relax! CTB Champion', 'flag checkered'),
(1025, 'TUTORIAL ENDS™', 'brown child'),
(1026, 'Marathon Walker', 'recycle'),
(1027, 'verified', 'yellow check'),
(8016, 'Your ID is 8016!!', 'purple trophy');

-- --------------------------------------------------------

--
-- 테이블 구조 `bancho_channels`
--

CREATE TABLE `bancho_channels` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `description` varchar(127) NOT NULL,
  `public_read` tinyint(4) NOT NULL,
  `public_write` tinyint(4) NOT NULL,
  `status` tinyint(4) NOT NULL,
  `temp` tinyint(1) NOT NULL DEFAULT 0,
  `hidden` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `bancho_channels`
--

INSERT INTO `bancho_channels` (`id`, `name`, `description`, `public_read`, `public_write`, `status`, `temp`, `hidden`) VALUES
(1, '#osu', 'Windows global chat', 1, 1, 1, 0, 0),
(2, '#debian', 'Debian was Dead :(', 1, 1, 1, 0, 0),
(3, '#announce', 'Announce channel', 1, 0, 1, 0, 0),
(4, '#leaderboard', 'Leaderboard channel', 1, 0, 1, 0, 0),
(5, '#score-submit', 'score submit', 1, 1, 1, 0, 0),
(6, '#ranked', 'Rank requests maps will be posted here! (If it\'s ranked.)', 1, 0, 1, 0, 0),
(7, '#admin', 'Are you admin?', 0, 0, 1, 0, 1),
(8, '#Korean', 'Korean community', 1, 1, 1, 0, 0),
(9, '#english', 'English community', 1, 1, 1, 0, 0),
(10, '#lobby', 'This is the lobby where you find games to play with others!', 1, 1, 1, 0, 1);

-- --------------------------------------------------------

--
-- 테이블 구조 `bancho_messages`
--

CREATE TABLE `bancho_messages` (
  `id` int(11) NOT NULL,
  `msg_from_userid` int(11) NOT NULL,
  `msg_from_username` varchar(40) NOT NULL,
  `msg_to` varchar(32) NOT NULL,
  `msg` varchar(127) NOT NULL,
  `time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `bancho_private_messages`
--

CREATE TABLE `bancho_private_messages` (
  `id` int(11) NOT NULL,
  `msg_from_userid` int(11) NOT NULL,
  `msg_from_username` varchar(40) NOT NULL,
  `msg_to` varchar(32) NOT NULL,
  `msg` varchar(127) NOT NULL,
  `time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `bancho_settings`
--

CREATE TABLE `bancho_settings` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `value_int` int(11) NOT NULL DEFAULT 0,
  `value_string` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `bancho_settings`
--

INSERT INTO `bancho_settings` (`id`, `name`, `value_int`, `value_string`) VALUES
(1, 'bancho_maintenance', 0, ''),
(2, 'free_direct', 1, ''),
(3, 'menu_icon', 1, 'https://redstar.moe/static/logos/main_menu_icons.png'),
(4, 'login_messages', 1, ''),
(5, 'restricted_joke', 0, 'You\'re banned from the server. Check Your Email'),
(6, 'login_notification', 1, 'Welcome to Redstar (Beta)!'),
(7, 'osu_versions', 0, ''),
(8, 'osu_md5s', 0, '');

-- --------------------------------------------------------

--
-- 테이블 구조 `bancho_tokens`
--

CREATE TABLE `bancho_tokens` (
  `id` int(11) NOT NULL,
  `token` varchar(16) NOT NULL,
  `osu_id` int(11) NOT NULL,
  `latest_message_id` int(11) NOT NULL,
  `latest_private_message_id` int(11) NOT NULL,
  `latest_packet_time` int(11) NOT NULL,
  `latest_heavy_packet_time` int(11) NOT NULL,
  `joined_channels` varchar(512) NOT NULL,
  `game_mode` tinyint(4) NOT NULL,
  `action` int(11) NOT NULL,
  `action_text` varchar(128) NOT NULL,
  `kicked` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `beatmaps`
--

CREATE TABLE `beatmaps` (
  `id` int(11) NOT NULL,
  `rankedby` varchar(40) NOT NULL DEFAULT 'Bancho',
  `beatmap_id` int(11) NOT NULL DEFAULT 0,
  `beatmapset_id` int(11) NOT NULL DEFAULT 0,
  `beatmap_md5` varchar(32) NOT NULL DEFAULT '',
  `song_name` longtext NOT NULL,
  `file_name` text DEFAULT NULL,
  `ar` float NOT NULL DEFAULT 0,
  `od` float NOT NULL DEFAULT 0,
  `mode` int(11) NOT NULL DEFAULT 0,
  `rating` int(11) NOT NULL DEFAULT 10,
  `difficulty_std` float NOT NULL DEFAULT 0,
  `difficulty_taiko` float NOT NULL DEFAULT 0,
  `difficulty_ctb` float NOT NULL DEFAULT 0,
  `difficulty_mania` float NOT NULL DEFAULT 0,
  `max_combo` int(11) NOT NULL DEFAULT 0,
  `hit_length` int(11) NOT NULL DEFAULT 0,
  `bpm` bigint(11) NOT NULL DEFAULT 0,
  `playcount` int(11) NOT NULL DEFAULT 0,
  `passcount` int(11) NOT NULL DEFAULT 0,
  `ranked` tinyint(4) NOT NULL DEFAULT 0,
  `latest_update` int(11) NOT NULL DEFAULT 0,
  `ranked_status_freezed` tinyint(1) NOT NULL DEFAULT 0,
  `pp_100` int(11) NOT NULL DEFAULT 0,
  `pp_99` int(11) NOT NULL DEFAULT 0,
  `pp_98` int(11) NOT NULL DEFAULT 0,
  `pp_95` int(11) NOT NULL DEFAULT 0,
  `disable_pp` tinyint(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `beatmaps`
--

INSERT INTO `beatmaps` (`id`, `rankedby`, `beatmap_id`, `beatmapset_id`, `beatmap_md5`, `song_name`, `file_name`, `ar`, `od`, `mode`, `rating`, `difficulty_std`, `difficulty_taiko`, `difficulty_ctb`, `difficulty_mania`, `max_combo`, `hit_length`, `bpm`, `playcount`, `passcount`, `ranked`, `latest_update`, `ranked_status_freezed`, `pp_100`, `pp_99`, `pp_98`, `pp_95`, `disable_pp`) VALUES
(1, '1000', -1, 919187, '4a195cce8b18145cdb78747c48c8effd', '765 MILLION ALLSTARS - UNION!! [We are all MILLION!! CS0]', NULL, 9.2, 9.3, 0, 10, 5.37, 5.19, 4.31, 2.88, 1812, 302, 172, 101, 8, 4, 1651742565, 2, 291, 246, 215, 174, 0),
(2, '1000', -2, 1101197, '8eec990e4f38938b70d834c3dd5e99ad', '765 MILLION ALLSTARS - UNION!!(Speed Up Ver.) [Million CS0]', NULL, 9.5, 9.5, 0, 10, 5.92, 3.72, 4.48, 2.9, 1720, 240, 215, 12, 0, 4, 1639643113, 1, 375, 326, 294, 249, 0),
(3, '1000', -3, 1134282, '5de8cae575d875c8cd180e0d0ae42328', '765 MILLION ALLSTARS - UNION!! [Castle of Dreams CS0]', NULL, 9.2, 8.7, 0, 10, 4.91, 5.13, 3.98, 2.84, 1956, 305, 172, 0, 0, 4, 1651754346, 1, 252, 217, 192, 156, 0),
(4, '1000', -4, 1058213, '5e70f90dfe79c24053592c24f758dc5c', '765 MILLION ALLSTARS - UNION!! [Million Power CS0]', NULL, 9.2, 9, 0, 10, 5.02, 5.23, 3.85, 2.76, 1929, 304, 172, 3, 1, 4, 1651754294, 1, 260, 219, 192, 154, 0),
(5, '1000', -5, 12483, '60d729883ea9ef56d3b4990ab8aff46f', 'Hommarju feat. Latte - masterpiece [Insane CS0]', NULL, 8, 8, 0, 10, 4.43, 3.7, 2.73, 2.72, 871, 183, 180, 64, 2, 4, 1652288458, 1, 151, 131, 116, 96, 0),
(6, '1000', -6, 12483, '3fc0979cf06c64ea7a952fa41071b804', 'Hommarju feat. Latte - masterpiece [Insane AR9]', NULL, 9, 8, 0, 10, 5.39, 3.7, 3.51, 2.78, 871, 183, 180, 2, 0, 4, 1652288458, 1, 207, 187, 172, 152, 0),
(7, '1000', -7, 12483, 'f3e95832ae1630b099fc9a6227f29001', 'Hommarju feat. Latte - masterpiece [Insane AR10]', NULL, 10, 8, 0, 10, 5.39, 3.7, 3.51, 2.74, 871, 183, 180, 2, 0, 4, 1652288458, 1, 207, 187, 172, 152, 0),
(8, '1000', -8, 1193588, '1cc6dfa5464cbc803a4e169d80c4272b', 'Yamajet feat. Hiura Masako - Sunglow [Harmony CS0]', NULL, 9.3, 9.3, 0, 10, 5.34, 4.31, 4.09, 2.67, 1646, 301, 180, 36, 0, 4, 1652289071, 1, 285, 241, 210, 170, 0),
(9, '1000', -9, 1002271, 'f0986d45e947bf5c3cdd539842cf7c8c', 'Bliitzit - Team Magma & Aqua Leader Battle Theme (Unofficial) [Catastrophe CS0]', NULL, 9.2, 9.2, 0, 10, 5.48, 3.6, 4.2, 2.78, 428, 74, 200, 9, 1, 4, 1652289288, 1, 234, 206, 190, 159, 0),
(10, '1000', -10, 1002271, '6ebf29e7b89f7903d5806f9645af6e7e', 'Bliitzit - Team Magma & Aqua Leader Battle Theme (Unofficial) [Catastrophe AR10]', NULL, 10, 9.2, 0, 10, 6.42, 3.6, 5.34, 2.77, 428, 74, 200, 0, 0, 4, 1652289288, 1, 314, 286, 270, 239, 0),
(11, '1000', -11, 782318, '5d72826f592accc29bb252de1bf4346f', 'WISEMAN - The Theme of WISEMAN [Expert CS0]', NULL, 9.6, 8.5, 0, 10, 5.26, 3.1, 3.91, 3.87, 789, 87, 154, 4, 0, 4, 1652289552, 1, 208, 180, 164, 144, 0),
(12, '1000', -12, 871623, '406c97b95441d9156137361cc5891c7a', 'xi - over the top [Above the stars CS0]', NULL, 9.5, 10, 0, 10, 6.81, 3.84, 3.25, 3.33, 1325, 115, 202, 124, 10, 4, 1651799396, 1, 553, 506, 469, 400, 0),
(13, '1000', -13, 595163, '14deaedc2b9f468e717d3d59efb4451e', 'Yamajet feat. Hiura Masako - Sunglow [Melody CS0]', NULL, 9.3, 9, 0, 10, 5.03, 4.32, 4.52, 2.81, 1721, 301, 180, 0, 0, 4, 1652292011, 1, 257, 217, 192, 153, 0),
(14, '1000', -14, 48498, '55d1d64983b2f95e1dbdf28527816080', 'Hommarju feat. Latte - masterpiece [SQUARES]', NULL, 8, 8, 0, 10, 5.42, 3.34, 3.24, 3.79, 1252, 211, 180, 0, 0, 4, 0, 1, 252, 233, 216, 186, 0),
(15, '1000', -2160333, 1027900, '08d928047d5be504f2e088cc6e4b6e4f', 't+pazolite - Party in the HOLLOWood feat. Nanahira (HOLLOWeen Sitchaka Metchaka Remix) [Rabbit Lude\'s Hard]', NULL, 0, 8.3, 0, 10, 0, 0, 0, 3.54, 0, 195, 200, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0),
(16, '1000', -1645802, 780250, '707ecd7e32b4b17b5fd3cd6e337ad21e', 'Alfakyun. - Teo [Collab Light Insane]', NULL, 8.8, 7, 0, 10, 4.64741, 5.10979, 2.91151, 2.60899, 1137, 193, 185, 1, 1, 3, 0, 1, 125, 110, 100, 89, 0),
(17, '1000', -1648943, 780250, 'efdfbb02094c6ddbee8aad9f175546cb', 'Alfakyun. - Teo [waji\'s Normal]', NULL, 4.3, 3, 0, 10, 2.29277, 2.87193, 1.44752, 1.80017, 576, 173, 185, 0, 0, 3, 0, 1, 15, 12, 11, 10, 0),
(18, '1000', -1655703, 780250, 'c45a206bbfd3550062127ca23db7a601', 'Alfakyun. - Teo [Hard]', NULL, 8, 6, 0, 10, 3.66436, 4.68365, 2.01664, 2.68392, 1095, 189, 185, 0, 0, 3, 0, 1, 68, 57, 51, 45, 0),
(19, '1000', -1639687, 780250, '2697d9ce593a95b23b7721f311134ecb', 'Alfakyun. - Teo [Insane]', NULL, 9, 8, 0, 10, 5.23866, 5.53844, 4.01371, 2.8474, 1299, 189, 185, 10, 0, 3, 0, 1, 204, 181, 165, 142, 0),
(20, '1000', -1653038, 780250, 'ef772374bbd27319c550e3f4365789e8', 'Alfakyun. - Teo [Koume\'s Extra]', NULL, 9.4, 8.5, 0, 10, 6.16845, 5.5329, 5.74299, 3.03929, 1279, 188, 185, 0, 0, 3, 0, 1, 323, 296, 276, 244, 0),
(21, '1000', -1639118, 780250, 'bd7be54e98810120eae718383892e8ed', 'Alfakyun. - Teo [Nothing will stop us]', NULL, 9.7, 9, 0, 10, 6.68087, 5.57224, 5.30813, 3.69815, 1350, 189, 185, 0, 0, 3, 0, 1, 434, 400, 376, 335, 0),
(22, '1000', -15, 811908, '5ef5d9927903e2da29c4409622734e6d', 'Hana - Sakura no Uta (Sped Up Ver.) [Sakura Seed CS0]', NULL, 9.8, 8.8, 0, 10, 6.83944, 3.52021, 6.52474, 3.05474, 1336, 181, 207, 119, 7, 4, 1662047540, 1, 326, 295, 272, 238, 0),
(23, '1000', -16, 811908, '4733b8c5d32514750124da24da511195', 'Hana - Sakura no Uta (Sped Up Ver.) [Triangle-chan\'s Sakura Tree CS0]', NULL, 9.8, 9, 0, 10, 7.74496, 3.79172, 7.0015, 4.15597, 1506, 200, 207, 0, 0, 4, 1662047544, 1, 440, 404, 379, 340, 0),
(24, '1000', -17, 811908, '1fdaad4c2b3b6622b1ffa84e9cf7ba68', 'Hana - Sakura no Uta (Sped Up Ver.) [quantumvortex\'s Thousand Cherry Blossoms CS0]', NULL, 9.9, 9.8, 0, 10, 7.82071, 4.98568, 7.4242, 3.47644, 1355, 200, 207, 0, 0, 4, 1662047547, 1, 502, 455, 420, 366, 0),
(25, '1000', -18, 811908, 'f2de95b0c33633453dcb79b85944e851', 'Hana - Sakura no Uta (Sped Up Ver.) [This Final Verse of the Sakura Tree will last Forever... CS0]', NULL, 10, 9.2, 0, 10, 7.97992, 3.67351, 6.81315, 4.13879, 1543, 200, 207, 6, 0, 4, 1662047550, 1, 472, 433, 405, 362, 0),
(26, '1000', -3917272, 1900394, '64ce780a48fe717ab454008452d78fec', 'katagiri - STRONG 280 [TURBULENT~!]', NULL, 10, 9, 0, 10, 8.20301, 5.10509, 6.36902, 4.86084, 1322, 127, 280, 15, 1, 3, 0, 1, 648, 613, 588, 545, 0),
(27, '1000', -19, -10000000, '1cd28651e85cf135ba991259bed7158d', 'Nomizu Iori - Black + White (TV Size) [ULTIMATE STAR BURST!!!]', NULL, 0, 0, 0, 10, 0, 0, 0, 40.52, 2520, 0, 192, 17, 7, 4, 1679680595, 1, 0, 0, 0, 0, 0),
(28, '1000', -20, 119103, '0f28be881f56ad92d026fbb1c6470e55', 'goreshit - fly, heart!  fly! [vs ELY Over Stream CS0]', NULL, 9, 7, 0, 10, 5.65, 3.94, 3.54, 3.52, 1377, 170, 201, 4, 0, 4, 1670966605, 1, 236, 222, 211, 193, 0),
(29, '1000', -21, 119103, '4b5eb6b6eade7d77e9f3c34451ae295d', 'goreshit - fly, heart!  fly! [vs ELY Over Stream (AR10) CS0]', NULL, 10, 7, 0, 10, 5.65, 3.94, 3.54, 3.53, 1377, 170, 201, 16, 2, 4, 1670966603, 1, 236, 222, 211, 193, 0),
(30, '1000', -22, 12483, '87690e37e0e2fd39c9b0d9b872ce8d64', 'Hommarju feat. Latte - masterpiece [ignore\'s Chaos AR10]', NULL, 10, 8, 0, 10, 4.5, 3.83, 3.6, 2.63, 730, 157, 180, 4, 0, 4, 1693719551, 1, 144, 125, 112, 93, 0),
(31, '1000', -23, 940322, '0ac0c334dca3cbb3d38fa0567309b56d', 'Komichi Aya (CV: Taneda Risa) - Koiiro Iris (brz_bootleg_remix) [Inner Oni Kiai1]', NULL, 5, 7, 0, 10, 0, 6.4, 0, 0, 281, 208, 310, 30, 2, 5, 1702152306, 1, 275, 261, 250, 223, 0),
(32, '1000', -24, 940322, 'cd39c5796c8a0f894522f00db62c6270', 'Komichi Aya (CV: Taneda Risa) - Koiiro Iris (brz_bootleg_remix) [Inner Oni Kiai2]', NULL, 5, 7, 0, 10, 0, 6.37, 0, 0, 282, 208, 310, 38, 2, 5, 1702152306, 1, 284, 270, 260, 233, 0),
(33, '1000', -25, 940322, '8739c130d92e523bd08344fb644b7a9d', 'Komichi Aya (CV: Taneda Risa) - Koiiro Iris (brz_bootleg_remix) [Inner Oni Kiai3]', NULL, 5, 7, 0, 10, 0, 6.69, 0, 0, 298, 208, 310, 32, 2, 5, 1702152306, 1, 283, 270, 258, 230, 0);

-- --------------------------------------------------------

--
-- 테이블 구조 `beatmaps_names`
--

CREATE TABLE `beatmaps_names` (
  `id` int(11) NOT NULL,
  `beatmap_md5` varchar(32) NOT NULL DEFAULT '',
  `beatmap_name` varchar(256) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `beatmaps_rating`
--

CREATE TABLE `beatmaps_rating` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `beatmap_md5` varchar(32) NOT NULL,
  `rating` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `clans`
--

CREATE TABLE `clans` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL,
  `icon` text NOT NULL,
  `tag` varchar(10) NOT NULL,
  `mlimit` int(11) NOT NULL DEFAULT 16
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `clans_invites`
--

CREATE TABLE `clans_invites` (
  `id` int(11) NOT NULL,
  `clan` int(11) NOT NULL,
  `invite` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `beatmap_id` int(11) NOT NULL DEFAULT 0,
  `beatmapset_id` int(11) NOT NULL DEFAULT 0,
  `score_id` int(11) NOT NULL DEFAULT 0,
  `mode` int(11) NOT NULL,
  `comment` varchar(128) NOT NULL,
  `time` int(11) NOT NULL,
  `who` varchar(11) NOT NULL,
  `special_format` varchar(2556) DEFAULT 'FFFFFF'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `docs`
--

CREATE TABLE `docs` (
  `id` int(11) UNSIGNED NOT NULL,
  `doc_name` varchar(255) NOT NULL DEFAULT 'New Documentation File',
  `doc_contents` longtext NOT NULL,
  `public` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `old_name` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `hw_user`
--

CREATE TABLE `hw_user` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `mac` varchar(32) NOT NULL,
  `unique_id` varchar(32) NOT NULL,
  `disk_id` varchar(32) NOT NULL,
  `occurencies` int(11) NOT NULL DEFAULT 0,
  `activated` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `identity_tokens`
--

CREATE TABLE `identity_tokens` (
  `userid` int(11) NOT NULL,
  `token` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `ip_user`
--

CREATE TABLE `ip_user` (
  `userid` int(11) NOT NULL,
  `ip` mediumtext NOT NULL,
  `occurencies` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `irc_tokens`
--

CREATE TABLE `irc_tokens` (
  `userid` int(11) NOT NULL DEFAULT 0,
  `token` varchar(32) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `leaderboard_ctb`
--

CREATE TABLE `leaderboard_ctb` (
  `position` int(10) UNSIGNED NOT NULL,
  `user` int(11) NOT NULL,
  `v` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `leaderboard_mania`
--

CREATE TABLE `leaderboard_mania` (
  `position` int(10) UNSIGNED NOT NULL,
  `user` int(11) NOT NULL,
  `v` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `leaderboard_std`
--

CREATE TABLE `leaderboard_std` (
  `position` int(10) UNSIGNED NOT NULL,
  `user` int(11) NOT NULL,
  `v` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `leaderboard_taiko`
--

CREATE TABLE `leaderboard_taiko` (
  `position` int(10) UNSIGNED NOT NULL,
  `user` int(11) NOT NULL,
  `v` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `main_menu_icons`
--

CREATE TABLE `main_menu_icons` (
  `id` int(11) NOT NULL,
  `is_current` int(11) NOT NULL,
  `file_id` varchar(128) NOT NULL,
  `name` varchar(256) NOT NULL,
  `url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `main_menu_icons`
--

INSERT INTO `main_menu_icons` (`id`, `is_current`, `file_id`, `name`, `url`) VALUES
(1, 1, 'logo', 'Redstar!', 'https://redstar.moe');

-- --------------------------------------------------------

--
-- 테이블 구조 `mapsuggest`
--

CREATE TABLE `mapsuggest` (
  `id` int(11) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `beatmap_id` int(11) DEFAULT NULL,
  `song_name` longtext DEFAULT NULL,
  `ppMsg` longtext DEFAULT '100%: NULL | 99%: NULL | 98%: NULL | 95%: NULL',
  `datetime` int(11) DEFAULT unix_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 테이블의 덤프 데이터 `mapsuggest`
--

INSERT INTO `mapsuggest` (`id`, `type`, `beatmap_id`, `song_name`, `ppMsg`, `datetime`) VALUES
(1, 'stream', 1821147, 'xi - over the top [Above the stars]', '100%: 934pp | 99%: 886pp | 98%: 848pp | 95%: 773pp', 1697946695),
(2, 'stream', 1685606, 'LeaF - Paraclete [543543]', '100%: 537pp | 99%: 502pp | 98%: 479pp | 95%: 425pp', 1697946702),
(3, 'stream', 2659368, 'technoplanet - Juvenile [Ataraxis]', '100%: 627pp | 99%: 588pp | 98%: 557pp | 95%: 502pp', 1697946706),
(4, 'stream', 2615748, 'Tatsh - Xevel [Extreme]', '100%: 320pp | 99%: 295pp | 98%: 278pp | 95%: 248pp', 1697946710),
(5, 'stream', 2852853, 'Mutsuhiko Izumi - Snow Goose [unko\'s Wiz Khalifa Insane]', '100%: 376pp | 99%: 372pp | 98%: 368pp | 95%: 358pp', 1697946714),
(6, 'stream', 2880427, 'Mutsuhiko Izumi - Snow Goose [End Stream {Easy}]', '100%: 559pp | 99%: 528pp | 98%: 512pp | 95%: 467pp', 1697946718),
(7, 'stream', 2316176, 'GYZE - HONESTY [HEART OF SORROW]', '100%: 307pp | 99%: 268pp | 98%: 239pp | 95%: 195pp', 1697946721),
(8, 'stream', 1241370, 'GYZE - HONESTY [DISHONEST]', '100%: 650pp | 99%: 606pp | 98%: 571pp | 95%: 506pp', 1697946724),
(9, 'stream', 1728346, 'GYZE - Honesty (Bass String Size) [ok this is epic]', '100%: 514pp | 99%: 484pp | 98%: 462pp | 95%: 418pp', 1697946728),
(10, 'stream', 2879904, 'GYZE - HONESTY (Cut Ver.) [ok this is pog]', '100%: 614pp | 99%: 579pp | 98%: 548pp | 95%: 493pp', 1697946732),
(11, 'stream', 1730316, 'GYZE - Honesty (Guitar String Size) [Pudge EXTRA]', '100%: 506pp | 99%: 464pp | 98%: 429pp | 95%: 365pp', 1697946735),
(12, 'stream', 1801204, 'Will Stetson - Honesty (Swing Arrangement) [ThatTromboneGuy Edit] [CONVICTION]', '100%: 369pp | 99%: 327pp | 98%: 297pp | 95%: 228pp', 1697946739),
(13, 'stream', 135880, 'xi - Akasha [BMax]', '100%: 261pp | 99%: 239pp | 98%: 221pp | 95%: 191pp', 1697946742),
(14, 'stream', 1192807, 'ke-ji feat. Nanahira - Ange du Blanc Pur [ABSOLUTION]', '100%: 419pp | 99%: 372pp | 98%: 331pp | 95%: 255pp', 1697946745),
(15, 'stream', 2493865, 'ke-ji feat. Nanahira - Ange du Blanc Pur (Short Ver.) [Forbidden Heaven]', '100%: 411pp | 99%: 382pp | 98%: 358pp | 95%: 319pp', 1697946748),
(16, 'stream', 111680, 'xi - Ascension to Heaven [Death]', '100%: 280pp | 99%: 260pp | 98%: 245pp | 95%: 217pp', 1697946751),
(17, 'stream', 658127, 'xi - Blue Zenith [FOUR DIMENSIONS]', '100%: 603pp | 99%: 566pp | 98%: 539pp | 95%: 486pp', 1697946755),
(18, 'stream', 383536, 'a_hisa - Cheshire,s dance [Another]', '100%: 393pp | 99%: 359pp | 98%: 333pp | 95%: 289pp', 1697946758),
(19, 'stream', 1983024, 'Suzuki Konomi - CHOIR JAIL (TV Size) [Yukiyo\'s Phantasm]', '100%: 345pp | 99%: 316pp | 98%: 293pp | 95%: 253pp', 1697946761),
(20, 'stream', 2330482, 'Saint Snow - DROPOUT!? [Curse]', '100%: 458pp | 99%: 419pp | 98%: 389pp | 95%: 338pp', 1697946765),
(21, 'stream', 2228709, 'Ito Kanako - fake me (samfree\'s Science Adventure Dance Remix) (Sped Up Ver.) [stream me]', '100%: 380pp | 99%: 333pp | 98%: 294pp | 95%: 227pp', 1697946769),
(22, 'stream', 668662, 'Yooh - Ice Angel [Saint]', '100%: 353pp | 99%: 320pp | 98%: 295pp | 95%: 250pp', 1697946772),
(23, 'stream', 252238, 'Tatsh - IMAGE -MATERIAL- <Version 0> [Scorpiour]', '100%: 604pp | 99%: 575pp | 98%: 554pp | 95%: 520pp', 1697946775),
(24, 'stream', 495651, 'Ice - L (Lost, Loneliness, & Liberation) [Ascension]', '100%: 407pp | 99%: 379pp | 98%: 358pp | 95%: 323pp', 1697946779),
(25, 'stream', 1912276, 'Erabareshi - Motto, Nee Motto (TV Size) [Fanservice]', '100%: 496pp | 99%: 470pp | 98%: 449pp | 95%: 409pp', 1697946782),
(26, 'stream', 1695382, 'THE ORAL CIGARETTES - Mou Ii kai? [Rain]', '100%: 442pp | 99%: 410pp | 98%: 384pp | 95%: 340pp', 1697946786),
(27, 'stream', 116128, '07th Expansion - rog-unlimitation [AngelHoney]', '100%: 285pp | 99%: 272pp | 98%: 262pp | 95%: 245pp', 1697946789),
(28, 'stream', 2156842, 'VINXIS - Sidetracked Day [Daydream]', '100%: 247pp | 99%: 220pp | 98%: 203pp | 95%: 177pp', 1697946792),
(29, 'stream', 789765, 'antiPLUR - Speed of Link [299 792 458m/s]', '100%: 749pp | 99%: 698pp | 98%: 661pp | 95%: 593pp', 1697946796),
(30, 'stream', 2722803, 'PinocchioP - sukisukisukisukisukisukisukisukisukisuki [Kokoro-Chan]', '100%: 305pp | 99%: 277pp| 98%: 254pp | 95%: 218pp', 1697946798),
(31, 'stream', 1997307, 'PinocchioP - sukisukisukisukisukisukisukisukisukisuki [<3 <3 <3 <3 <3 <3 <3 <3 <3]', '100%: 751pp | 99%: 711pp | 98%: 681pp | 95%: 627pp', 1697946801),
(32, 'stream', 729138, 'UNDEAD CORPORATION - The Empress [STARBOW BREAK!]', '100%: 1675928pp | 99%: 1664237pp | 98%: 1652586pp | 95%: 1617563pp', 1697946805),
(33, 'stream', 3632759, 'EPICA - Wings of Freedom [Alis Libertatis]', '100%: 251pp | 99%: 226pp | 98%: 207pp | 95%: 174pp', 1697946809),
(34, 'stream', 1816113, 'Imperial Circus Dead Decadence - Yomi yori Kikoyu, Koukoku no Tou to Honoo no Shoujo. [Kurushimi]', '100%: 1007pp | 99%: 949pp | 98%: 906pp | 95%: 830pp', 1697946811),
(35, 'stream', 2097957, 'DJ Sharpnel - WE LUV LAMA [1025 stream]', '100%: 644pp | 99%: 609pp | 98%: 579pp | 95%: 522pp', 1697946814),
(36, 'stream', 1895569, 'Hoshi Syoko (CV: Matsuda Satsumi) - Zettai Tokken Shuchou Shimasu! Hoshi Syoko Solo Remix [Yui\'s Expert!]', '100%: 186pp | 99%: 165pp | 98%: 154pp | 95%: 127pp', 1697946818),
(37, 'stream', 3959036, 'SYU (from GALNERYUS) - Mikansei no Tsubasa [Wings of Liberty]', '100%: 738pp | 99%: 690pp | 98%: 654pp | 95%: 589pp', 1697946822),
(38, 'stream', 3632631, 'Hoshimachi Suisei - TALALALALALALALALALALALAAAAA LALAAAAAAAAAAAAA [Mahiru\'s Sounds Piercing The Heavenly Skies]', '100%: 492pp | 99%: 460pp | 98%: 436pp | 95%: 393pp', 1697946826),
(39, 'stream', 845391, 'Feint - Tower Of Heaven (You Are Slaves) [Heaven]', '100%: 316pp | 99%: 281pp | 98%: 257pp | 95%: 220pp', 1697946830),
(40, 'stream', 1990449, 'Our Stolen Theory - United (L.A.O.S Remix) [Eternity]', '100%: 395pp | 99%: 355pp | 98%: 325pp | 95%: 281pp', 1697946834),
(41, 'stream', 3669201, 'Our Stolen Theory - United (L.A.O.S Remix) [Everlasting]', '100%: 281pp | 99%: 243pp | 98%: 219pp | 95%: 181pp', 1697946837),
(42, 'stream', 1389624, 'SOUND HOLIC Vs. T.Kakuta feat. YURiCa - TOXIC VIBRATION (extend ver.) [NiNo\'s Extra]', '100%: 473pp | 99%: 436pp | 98%: 407pp | 95%: 358pp', 1697946841),
(43, 'stream', 3018109, 'Mage - The Words I Never Said [Regret]', '100%: 386pp | 99%: 344pp | 98%: 313pp | 95%: 260pp', 1697946844),
(44, 'stream', 1754266, 'Nanahoshi Kangengakudan - Rubik\'s Cube [43,252,003,274,489,856,000]', '100%: 819pp | 99%: 765pp | 98%: 722pp | 95%: 647pp', 1697946847),
(45, 'stream', 2069999, 'SYU (from GALNERYUS) - REASON [A THOUSAND SWORDS]', '100%: 796pp | 99%: 751pp | 98%: 715pp | 95%: 648pp', 1697946850),
(46, 'stream', 3385971, 'DragonForce - My Heart Will Go On [Titanic]', '100%: 819pp | 99%: 765pp | 98%: 725pp | 95%: 648pp', 1697946853),
(47, 'stream', 1216297, 'Deathstream Training #2 - Marathon Stream Training [Marathon]', '100%: 1234pp | 99%: 1201pp | 98%: 1174pp | 95%: 1114pp', 1697946856),
(48, 'stream', 3206402, 'Serenity - Lionheart [Sh4rq_\'s Heart of the Wilderness]', '100%: 541pp | 99%: 499pp | 98%: 467pp | 95%: 409pp', 1697946860),
(49, 'stream', 3837137, 'TEARS OF TRAGEDY - Epitaph [Learning to Thrive Through Loss, Tragedy, and Heartache]', '100%: 685pp | 99%: 638pp | 98%: 603pp | 95%: 537pp', 1701633618),
(50, 'stream', 3881559, 'TEARS OF TRAGEDY - Epitaph [Elegy]', '100%: 761pp | 99%: 706pp | 98%: 665pp | 95%: 591pp', 1701633689),
(52, 'stream', 4259693, 'TEARS OF TRAGEDY - Epitaph [Daestrophe]', '100%: 821pp | 99%: 764pp | 98%: 719pp | 95%: 639pp', 1701636567),
(53, 'stream', 3817010, 'TEARS OF TRAGEDY - Epitaph [Poem]', '100%: 733pp | 99%: 680pp | 98%: 640pp | 95%: 569pp', 1702070373);

-- --------------------------------------------------------

--
-- 테이블 구조 `osin_access`
--

CREATE TABLE `osin_access` (
  `scope` int(11) NOT NULL DEFAULT 0,
  `created_at` int(11) NOT NULL DEFAULT 0,
  `client` int(11) NOT NULL DEFAULT 0,
  `extra` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `osin_client`
--

CREATE TABLE `osin_client` (
  `id` int(11) NOT NULL,
  `secret` varchar(64) NOT NULL DEFAULT '',
  `extra` varchar(127) NOT NULL DEFAULT '',
  `redirect_uri` varchar(127) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `osin_client_user`
--

CREATE TABLE `osin_client_user` (
  `client_id` int(11) NOT NULL DEFAULT 0,
  `user` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `password_recovery`
--

CREATE TABLE `password_recovery` (
  `id` int(11) NOT NULL,
  `k` varchar(80) NOT NULL,
  `u` varchar(40) NOT NULL,
  `t` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `privileges_groups`
--

CREATE TABLE `privileges_groups` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `privileges` int(11) NOT NULL,
  `color` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `privileges_groups`
--

INSERT INTO `privileges_groups` (`id`, `name`, `privileges`, `color`) VALUES
(1, 'Banned', 0, 'orange'),
(2, 'BAT', 267, 'success'),
(3, 'Chat Moderators', 2883911, 'success'),
(4, 'Admin', 1048575, 'danger'),
(5, 'Developer', 1043995, 'info'),
(6, 'Donor', 7, 'default'),
(7, 'God', 1048575, 'info'),
(8, 'Normal User', 3, 'primary'),
(9, 'Pending', 1048576, 'orange'),
(10, 'Restricted', 2, ''),
(11, 'Beatmap Nominator', 267, 'primary'),
(12, 'Full Perms', 3145727, 'info'),
(13, 'Community Manager', 918015, 'success'),
(14, 'Admin (Without Doner)', 1048571, 'danger');

-- --------------------------------------------------------

--
-- 테이블 구조 `profile_backgrounds`
--

CREATE TABLE `profile_backgrounds` (
  `uid` int(11) NOT NULL,
  `time` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `value` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `rank_requests`
--

CREATE TABLE `rank_requests` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `type` varchar(8) NOT NULL,
  `time` int(11) NOT NULL,
  `blacklisted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `rap_logs`
--

CREATE TABLE `rap_logs` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `text` text NOT NULL,
  `datetime` int(11) NOT NULL,
  `through` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `remember`
--

CREATE TABLE `remember` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `series_identifier` int(11) DEFAULT NULL,
  `token_sha` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `reports`
--

CREATE TABLE `reports` (
  `id` int(11) NOT NULL,
  `from_uid` int(11) NOT NULL,
  `to_uid` int(11) NOT NULL,
  `reason` text NOT NULL,
  `chatlog` text NOT NULL,
  `time` int(11) NOT NULL,
  `assigned` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `rx_beatmap_playcount`
--

CREATE TABLE `rx_beatmap_playcount` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `beatmap_id` int(11) DEFAULT NULL,
  `game_mode` int(11) DEFAULT NULL,
  `playcount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `rx_stats`
--

CREATE TABLE `rx_stats` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `username_aka` varchar(100) NOT NULL DEFAULT '',
  `user_color` varchar(16) NOT NULL DEFAULT 'black',
  `user_style` varchar(128) NOT NULL DEFAULT '',
  `favourite_mode` int(11) NOT NULL DEFAULT 0,
  `level_std` int(11) NOT NULL DEFAULT 1,
  `level_taiko` int(11) NOT NULL DEFAULT 1,
  `level_mania` int(11) NOT NULL DEFAULT 1,
  `level_ctb` int(11) NOT NULL DEFAULT 1,
  `total_score_std` int(11) NOT NULL DEFAULT 0,
  `total_score_taiko` int(11) NOT NULL DEFAULT 0,
  `total_score_mania` int(11) NOT NULL DEFAULT 0,
  `total_score_ctb` int(11) NOT NULL DEFAULT 0,
  `total_hits_std` int(11) NOT NULL DEFAULT 0,
  `total_hits_taiko` int(11) NOT NULL DEFAULT 0,
  `total_hits_ctb` int(11) NOT NULL DEFAULT 0,
  `total_hits_mania` int(11) NOT NULL DEFAULT 0,
  `playtime_std` int(11) NOT NULL DEFAULT 0,
  `playtime_taiko` int(11) NOT NULL DEFAULT 0,
  `playtime_mania` int(11) NOT NULL DEFAULT 0,
  `playtime_ctb` int(11) NOT NULL DEFAULT 0,
  `ranked_score_std` bigint(11) NOT NULL DEFAULT 0,
  `ranked_score_taiko` int(11) NOT NULL DEFAULT 0,
  `ranked_score_mania` int(11) NOT NULL DEFAULT 0,
  `ranked_score_ctb` int(11) NOT NULL DEFAULT 0,
  `avg_accuracy_std` double NOT NULL DEFAULT 0,
  `avg_accuracy_taiko` double NOT NULL DEFAULT 0,
  `avg_accuracy_mania` double NOT NULL DEFAULT 0,
  `avg_accuracy_ctb` double NOT NULL DEFAULT 0,
  `playcount_std` int(11) NOT NULL DEFAULT 0,
  `playcount_taiko` int(11) NOT NULL DEFAULT 0,
  `playcount_mania` int(11) NOT NULL DEFAULT 0,
  `playcount_ctb` int(11) NOT NULL DEFAULT 0,
  `pp_std` int(11) NOT NULL DEFAULT 0,
  `pp_mania` int(11) NOT NULL DEFAULT 0,
  `pp_ctb` int(11) NOT NULL DEFAULT 0,
  `pp_taiko` int(11) NOT NULL DEFAULT 0,
  `country` char(2) NOT NULL DEFAULT 'XX',
  `unrestricted_pp` int(11) NOT NULL DEFAULT 0,
  `ppboard` int(11) NOT NULL DEFAULT 1,
  `replays_watched_std` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `replays_watched_taiko` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `replays_watched_ctb` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `replays_watched_mania` int(11) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `rx_stats`
--

INSERT INTO `rx_stats` (`id`, `username`, `username_aka`, `user_color`, `user_style`, `favourite_mode`, `level_std`, `level_taiko`, `level_mania`, `level_ctb`, `total_score_std`, `total_score_taiko`, `total_score_mania`, `total_score_ctb`, `total_hits_std`, `total_hits_taiko`, `total_hits_ctb`, `total_hits_mania`, `playtime_std`, `playtime_taiko`, `playtime_mania`, `playtime_ctb`, `ranked_score_std`, `ranked_score_taiko`, `ranked_score_mania`, `ranked_score_ctb`, `avg_accuracy_std`, `avg_accuracy_taiko`, `avg_accuracy_mania`, `avg_accuracy_ctb`, `playcount_std`, `playcount_taiko`, `playcount_mania`, `playcount_ctb`, `pp_std`, `pp_mania`, `pp_ctb`, `pp_taiko`, `country`, `unrestricted_pp`, `ppboard`, `replays_watched_std`, `replays_watched_taiko`, `replays_watched_ctb`, `replays_watched_mania`) VALUES
(999, 'Devlant', 'BOT', 'black', '', 0, 1, 1, 1, 1, 731057828, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 731057828, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'JP', 1, 1, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- 테이블 구조 `scores`
--

CREATE TABLE `scores` (
  `id` int(11) NOT NULL,
  `beatmap_md5` varchar(32) NOT NULL DEFAULT '',
  `userid` int(11) NOT NULL,
  `score` bigint(20) DEFAULT NULL,
  `max_combo` int(11) NOT NULL DEFAULT 0,
  `full_combo` tinyint(1) NOT NULL DEFAULT 0,
  `mods` int(11) NOT NULL DEFAULT 0,
  `300_count` int(11) NOT NULL DEFAULT 0,
  `100_count` int(11) NOT NULL DEFAULT 0,
  `50_count` int(11) NOT NULL DEFAULT 0,
  `katus_count` int(11) NOT NULL DEFAULT 0,
  `gekis_count` int(11) NOT NULL DEFAULT 0,
  `misses_count` int(11) NOT NULL DEFAULT 0,
  `time` varchar(18) NOT NULL DEFAULT '',
  `play_mode` tinyint(4) NOT NULL DEFAULT 0,
  `completed` tinyint(11) NOT NULL DEFAULT 0,
  `accuracy` float(15,12) DEFAULT NULL,
  `pp` double DEFAULT 0,
  `playtime` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `scores_ap`
--

CREATE TABLE `scores_ap` (
  `id` int(11) NOT NULL,
  `beatmap_md5` varchar(32) NOT NULL DEFAULT '',
  `userid` int(11) NOT NULL,
  `score` bigint(20) DEFAULT NULL,
  `max_combo` int(11) NOT NULL DEFAULT 0,
  `full_combo` tinyint(1) NOT NULL DEFAULT 0,
  `mods` int(11) NOT NULL DEFAULT 0,
  `300_count` int(11) NOT NULL DEFAULT 0,
  `100_count` int(11) NOT NULL DEFAULT 0,
  `50_count` int(11) NOT NULL DEFAULT 0,
  `katus_count` int(11) NOT NULL DEFAULT 0,
  `gekis_count` int(11) NOT NULL DEFAULT 0,
  `misses_count` int(11) NOT NULL DEFAULT 0,
  `time` varchar(18) NOT NULL DEFAULT '',
  `play_mode` tinyint(4) NOT NULL DEFAULT 0,
  `completed` tinyint(11) NOT NULL DEFAULT 0,
  `accuracy` float(15,12) DEFAULT NULL,
  `pp` double DEFAULT 0,
  `playtime` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- 테이블 구조 `scores_relax`
--

CREATE TABLE `scores_relax` (
  `id` int(11) NOT NULL,
  `beatmap_md5` varchar(32) NOT NULL DEFAULT '',
  `userid` int(11) NOT NULL,
  `score` bigint(20) DEFAULT NULL,
  `max_combo` int(11) NOT NULL DEFAULT 0,
  `full_combo` tinyint(1) NOT NULL DEFAULT 0,
  `mods` int(11) NOT NULL DEFAULT 0,
  `300_count` int(11) NOT NULL DEFAULT 0,
  `100_count` int(11) NOT NULL DEFAULT 0,
  `50_count` int(11) NOT NULL DEFAULT 0,
  `katus_count` int(11) NOT NULL DEFAULT 0,
  `gekis_count` int(11) NOT NULL DEFAULT 0,
  `misses_count` int(11) NOT NULL DEFAULT 0,
  `time` varchar(18) NOT NULL DEFAULT '',
  `play_mode` tinyint(4) NOT NULL DEFAULT 0,
  `completed` tinyint(11) NOT NULL DEFAULT 0,
  `accuracy` float(15,12) DEFAULT NULL,
  `pp` double DEFAULT 0,
  `playtime` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `system_settings`
--

CREATE TABLE `system_settings` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `value_int` int(11) NOT NULL DEFAULT 0,
  `value_string` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `system_settings`
--

INSERT INTO `system_settings` (`id`, `name`, `value_int`, `value_string`) VALUES
(1, 'website_maintenance', 0, ''),
(2, 'game_maintenance', 0, ''),
(3, 'website_global_alert', 1, '\"만약 오스 데비안 유저시라면 꼭 어드민에게 말해주세요! If you were a \'osu! Debian user\', please tell admin!!\"'),
(4, 'website_home_alert', 0, ''),
(5, 'registrations_enabled', 1, ''),
(6, 'ccreation_enabled', 1, ''),
(7, 'view_banneduser_record_ingame', 0, 'default = 0');

-- --------------------------------------------------------

--
-- 테이블 구조 `tokens`
--

CREATE TABLE `tokens` (
  `id` int(11) NOT NULL,
  `user` varchar(31) NOT NULL,
  `privileges` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `token` varchar(127) NOT NULL,
  `private` tinyint(4) NOT NULL,
  `last_updated` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `users`
--

CREATE TABLE `users` (
  `id` int(15) NOT NULL,
  `osuver` varchar(256) DEFAULT NULL,
  `username` varchar(40) NOT NULL,
  `username_safe` varchar(40) NOT NULL,
  `ban_datetime` varchar(30) NOT NULL DEFAULT '0',
  `password_md5` varchar(127) NOT NULL,
  `salt` varchar(32) NOT NULL,
  `email` varchar(254) NOT NULL,
  `register_datetime` int(10) NOT NULL,
  `rank` tinyint(1) NOT NULL DEFAULT 1,
  `allowed` tinyint(1) NOT NULL DEFAULT 1,
  `latest_activity` int(10) NOT NULL DEFAULT 0,
  `silence_end` int(11) NOT NULL DEFAULT 0,
  `silence_reason` varchar(127) NOT NULL DEFAULT '',
  `password_version` tinyint(4) NOT NULL DEFAULT 1,
  `privileges` bigint(11) NOT NULL,
  `donor_expire` int(11) NOT NULL DEFAULT 0,
  `flags` int(11) NOT NULL DEFAULT 0,
  `achievements_version` int(11) NOT NULL DEFAULT 4,
  `achievements_0` int(11) NOT NULL DEFAULT 1,
  `achievements_1` int(11) NOT NULL DEFAULT 1,
  `notes` mediumtext DEFAULT NULL,
  `last_session` varchar(1024) NOT NULL DEFAULT 'check'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `users`
--

INSERT INTO `users` (`id`, `osuver`, `username`, `username_safe`, `ban_datetime`, `password_md5`, `salt`, `email`, `register_datetime`, `rank`, `allowed`, `latest_activity`, `silence_end`, `silence_reason`, `password_version`, `privileges`, `donor_expire`, `flags`, `achievements_version`, `achievements_0`, `achievements_1`, `notes`, `last_session`) VALUES
(999, NULL, 'Devlant', 'devlant', '0', '*0', '5e/AceVLS7jJtxTJA1U6rmVqrWREYg==', 'fo@kab.ot', 1566228790, 4, 1, 1569775752, 0, '', 1, 3145727, 2147483647, 0, 0, 1, 1, '', 'check');

-- --------------------------------------------------------

--
-- 테이블 구조 `users_achievements`
--

CREATE TABLE `users_achievements` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `achievement_id` int(11) NOT NULL,
  `time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `users_beatmap_playcount`
--

CREATE TABLE `users_beatmap_playcount` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `beatmap_id` int(11) DEFAULT NULL,
  `game_mode` int(11) DEFAULT NULL,
  `playcount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `users_relationships`
--

CREATE TABLE `users_relationships` (
  `id` int(11) NOT NULL,
  `user1` int(11) NOT NULL,
  `user2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `users_stats`
--

CREATE TABLE `users_stats` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `username_aka` varchar(100) NOT NULL DEFAULT '',
  `user_color` varchar(16) NOT NULL DEFAULT 'black',
  `user_style` varchar(128) NOT NULL DEFAULT '',
  `ranked_score_std` bigint(20) DEFAULT 0,
  `playcount_std` int(11) NOT NULL DEFAULT 0,
  `total_score_std` bigint(20) DEFAULT 0,
  `replays_watched_std` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `ranked_score_taiko` bigint(20) DEFAULT 0,
  `playcount_taiko` int(11) NOT NULL DEFAULT 0,
  `total_score_taiko` bigint(20) DEFAULT 0,
  `replays_watched_taiko` int(11) NOT NULL DEFAULT 0,
  `ranked_score_ctb` bigint(20) DEFAULT 0,
  `playcount_ctb` int(11) NOT NULL DEFAULT 0,
  `total_score_ctb` bigint(20) DEFAULT 0,
  `replays_watched_ctb` int(11) NOT NULL DEFAULT 0,
  `ranked_score_mania` bigint(20) DEFAULT 0,
  `playcount_mania` int(11) NOT NULL DEFAULT 0,
  `total_score_mania` bigint(20) DEFAULT 0,
  `replays_watched_mania` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `total_hits_std` int(11) NOT NULL DEFAULT 0,
  `total_hits_taiko` int(11) NOT NULL DEFAULT 0,
  `total_hits_ctb` int(11) NOT NULL DEFAULT 0,
  `total_hits_mania` int(11) NOT NULL DEFAULT 0,
  `country` char(2) NOT NULL DEFAULT 'XX',
  `unrestricted_pp` int(11) NOT NULL DEFAULT 0,
  `ppboard` int(11) NOT NULL DEFAULT 0,
  `show_country` tinyint(4) NOT NULL DEFAULT 1,
  `level_std` int(11) NOT NULL DEFAULT 1,
  `level_taiko` int(11) NOT NULL DEFAULT 1,
  `level_ctb` int(11) NOT NULL DEFAULT 1,
  `level_mania` int(11) NOT NULL DEFAULT 1,
  `playtime_std` int(11) NOT NULL DEFAULT 0,
  `playtime_taiko` int(11) NOT NULL DEFAULT 0,
  `playtime_ctb` int(11) NOT NULL DEFAULT 0,
  `playtime_mania` int(11) NOT NULL DEFAULT 0,
  `avg_accuracy_std` float(15,12) NOT NULL DEFAULT 0.000000000000,
  `avg_accuracy_taiko` float(15,12) NOT NULL DEFAULT 0.000000000000,
  `avg_accuracy_ctb` float(15,12) NOT NULL DEFAULT 0.000000000000,
  `avg_accuracy_mania` float(15,12) NOT NULL DEFAULT 0.000000000000,
  `pp_std` int(11) NOT NULL DEFAULT 0,
  `pp_taiko` int(11) NOT NULL DEFAULT 0,
  `pp_ctb` int(11) NOT NULL DEFAULT 0,
  `pp_mania` int(11) NOT NULL DEFAULT 0,
  `badges_shown` varchar(24) NOT NULL DEFAULT '1,0,0,0,0,0',
  `safe_title` tinyint(4) NOT NULL DEFAULT 0,
  `userpage_content` longtext DEFAULT NULL,
  `play_style` smallint(6) NOT NULL DEFAULT 0,
  `favourite_mode` tinyint(4) NOT NULL DEFAULT 0,
  `prefer_relax` int(11) NOT NULL DEFAULT 0,
  `custom_badge_icon` varchar(32) NOT NULL DEFAULT '',
  `custom_badge_name` varchar(256) NOT NULL DEFAULT '',
  `can_custom_badge` tinyint(1) NOT NULL DEFAULT 1,
  `show_custom_badge` tinyint(1) NOT NULL DEFAULT 1,
  `current_status` varchar(20000) NOT NULL DEFAULT 'Offline'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 테이블의 덤프 데이터 `users_stats`
--

INSERT INTO `users_stats` (`id`, `username`, `username_aka`, `user_color`, `user_style`, `ranked_score_std`, `playcount_std`, `total_score_std`, `replays_watched_std`, `ranked_score_taiko`, `playcount_taiko`, `total_score_taiko`, `replays_watched_taiko`, `ranked_score_ctb`, `playcount_ctb`, `total_score_ctb`, `replays_watched_ctb`, `ranked_score_mania`, `playcount_mania`, `total_score_mania`, `replays_watched_mania`, `total_hits_std`, `total_hits_taiko`, `total_hits_ctb`, `total_hits_mania`, `country`, `unrestricted_pp`, `ppboard`, `show_country`, `level_std`, `level_taiko`, `level_ctb`, `level_mania`, `playtime_std`, `playtime_taiko`, `playtime_ctb`, `playtime_mania`, `avg_accuracy_std`, `avg_accuracy_taiko`, `avg_accuracy_ctb`, `avg_accuracy_mania`, `pp_std`, `pp_taiko`, `pp_ctb`, `pp_mania`, `badges_shown`, `safe_title`, `userpage_content`, `play_style`, `favourite_mode`, `prefer_relax`, `custom_badge_icon`, `custom_badge_name`, `can_custom_badge`, `show_custom_badge`, `current_status`) VALUES
(999, 'Devlant', 'BOT', 'black', '', 731261768, 0, 731261768, 6228539, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65443, 0, 0, 0, 0, 0, 'JP', 1, 0, 1, 102, 1, 1, 1, 0, 0, 0, 0, 0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000, 0, 0, 0, 0, '3,4,11,0,0,0', 0, NULL, 0, 0, 0, '', '', 1, 1, '');

-- --------------------------------------------------------

--
-- 테이블 구조 `user_badges`
--

CREATE TABLE `user_badges` (
  `id` int(11) NOT NULL,
  `user` int(11) NOT NULL,
  `badge` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `user_clans`
--

CREATE TABLE `user_clans` (
  `id` int(11) NOT NULL,
  `user` int(11) NOT NULL,
  `clan` int(11) NOT NULL,
  `perms` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 덤프된 테이블의 인덱스
--

--
-- 테이블의 인덱스 `2fa`
--
ALTER TABLE `2fa`
  ADD PRIMARY KEY (`userid`);

--
-- 테이블의 인덱스 `2fa_telegram`
--
ALTER TABLE `2fa_telegram`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `2fa_totp`
--
ALTER TABLE `2fa_totp`
  ADD PRIMARY KEY (`userid`);

--
-- 테이블의 인덱스 `achievements`
--
ALTER TABLE `achievements`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `anticheat_reports`
--
ALTER TABLE `anticheat_reports`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `ap_beatmap_playcount`
--
ALTER TABLE `ap_beatmap_playcount`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- 테이블의 인덱스 `ap_stats`
--
ALTER TABLE `ap_stats`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- 테이블의 인덱스 `badges`
--
ALTER TABLE `badges`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `bancho_channels`
--
ALTER TABLE `bancho_channels`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `bancho_messages`
--
ALTER TABLE `bancho_messages`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `bancho_private_messages`
--
ALTER TABLE `bancho_private_messages`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `bancho_settings`
--
ALTER TABLE `bancho_settings`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `bancho_tokens`
--
ALTER TABLE `bancho_tokens`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `beatmaps`
--
ALTER TABLE `beatmaps`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `beatmaps_names`
--
ALTER TABLE `beatmaps_names`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `beatmaps_rating`
--
ALTER TABLE `beatmaps_rating`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `clans`
--
ALTER TABLE `clans`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `clans_invites`
--
ALTER TABLE `clans_invites`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `docs`
--
ALTER TABLE `docs`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `hw_user`
--
ALTER TABLE `hw_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `userid` (`userid`);

--
-- 테이블의 인덱스 `identity_tokens`
--
ALTER TABLE `identity_tokens`
  ADD UNIQUE KEY `userid` (`userid`);

--
-- 테이블의 인덱스 `ip_user`
--
ALTER TABLE `ip_user`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `userid` (`userid`);

--
-- 테이블의 인덱스 `irc_tokens`
--
ALTER TABLE `irc_tokens`
  ADD UNIQUE KEY `userid` (`userid`);

--
-- 테이블의 인덱스 `leaderboard_ctb`
--
ALTER TABLE `leaderboard_ctb`
  ADD PRIMARY KEY (`position`);

--
-- 테이블의 인덱스 `leaderboard_mania`
--
ALTER TABLE `leaderboard_mania`
  ADD PRIMARY KEY (`position`);

--
-- 테이블의 인덱스 `leaderboard_std`
--
ALTER TABLE `leaderboard_std`
  ADD PRIMARY KEY (`position`);

--
-- 테이블의 인덱스 `leaderboard_taiko`
--
ALTER TABLE `leaderboard_taiko`
  ADD PRIMARY KEY (`position`);

--
-- 테이블의 인덱스 `main_menu_icons`
--
ALTER TABLE `main_menu_icons`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `mapsuggest`
--
ALTER TABLE `mapsuggest`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `beatmap_id` (`beatmap_id`);

--
-- 테이블의 인덱스 `osin_client`
--
ALTER TABLE `osin_client`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `password_recovery`
--
ALTER TABLE `password_recovery`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `privileges_groups`
--
ALTER TABLE `privileges_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 테이블의 인덱스 `profile_backgrounds`
--
ALTER TABLE `profile_backgrounds`
  ADD PRIMARY KEY (`uid`);

--
-- 테이블의 인덱스 `rank_requests`
--
ALTER TABLE `rank_requests`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `bid` (`bid`);

--
-- 테이블의 인덱스 `rap_logs`
--
ALTER TABLE `rap_logs`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `remember`
--
ALTER TABLE `remember`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `rx_beatmap_playcount`
--
ALTER TABLE `rx_beatmap_playcount`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `rx_stats`
--
ALTER TABLE `rx_stats`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `scores_ap`
--
ALTER TABLE `scores_ap`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- 테이블의 인덱스 `scores_relax`
--
ALTER TABLE `scores_relax`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `system_settings`
--
ALTER TABLE `system_settings`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `tokens`
--
ALTER TABLE `tokens`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `users_achievements`
--
ALTER TABLE `users_achievements`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `users_beatmap_playcount`
--
ALTER TABLE `users_beatmap_playcount`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `users_relationships`
--
ALTER TABLE `users_relationships`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `users_stats`
--
ALTER TABLE `users_stats`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `user_badges`
--
ALTER TABLE `user_badges`
  ADD PRIMARY KEY (`id`);

--
-- 테이블의 인덱스 `user_clans`
--
ALTER TABLE `user_clans`
  ADD PRIMARY KEY (`id`);

--
-- 덤프된 테이블의 AUTO_INCREMENT
--

--
-- 테이블의 AUTO_INCREMENT `2fa_telegram`
--
ALTER TABLE `2fa_telegram`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `anticheat_reports`
--
ALTER TABLE `anticheat_reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `ap_beatmap_playcount`
--
ALTER TABLE `ap_beatmap_playcount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `ap_stats`
--
ALTER TABLE `ap_stats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;

--
-- 테이블의 AUTO_INCREMENT `badges`
--
ALTER TABLE `badges`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8033;

--
-- 테이블의 AUTO_INCREMENT `bancho_channels`
--
ALTER TABLE `bancho_channels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- 테이블의 AUTO_INCREMENT `bancho_messages`
--
ALTER TABLE `bancho_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `bancho_private_messages`
--
ALTER TABLE `bancho_private_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `bancho_settings`
--
ALTER TABLE `bancho_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- 테이블의 AUTO_INCREMENT `bancho_tokens`
--
ALTER TABLE `bancho_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `beatmaps`
--
ALTER TABLE `beatmaps`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- 테이블의 AUTO_INCREMENT `beatmaps_names`
--
ALTER TABLE `beatmaps_names`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `beatmaps_rating`
--
ALTER TABLE `beatmaps_rating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `clans`
--
ALTER TABLE `clans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `clans_invites`
--
ALTER TABLE `clans_invites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `docs`
--
ALTER TABLE `docs`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `hw_user`
--
ALTER TABLE `hw_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `main_menu_icons`
--
ALTER TABLE `main_menu_icons`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 테이블의 AUTO_INCREMENT `mapsuggest`
--
ALTER TABLE `mapsuggest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- 테이블의 AUTO_INCREMENT `osin_client`
--
ALTER TABLE `osin_client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `password_recovery`
--
ALTER TABLE `password_recovery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `privileges_groups`
--
ALTER TABLE `privileges_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- 테이블의 AUTO_INCREMENT `rank_requests`
--
ALTER TABLE `rank_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `rap_logs`
--
ALTER TABLE `rap_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `remember`
--
ALTER TABLE `remember`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `reports`
--
ALTER TABLE `reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `rx_beatmap_playcount`
--
ALTER TABLE `rx_beatmap_playcount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `rx_stats`
--
ALTER TABLE `rx_stats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;

--
-- 테이블의 AUTO_INCREMENT `scores`
--
ALTER TABLE `scores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `scores_ap`
--
ALTER TABLE `scores_ap`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `scores_relax`
--
ALTER TABLE `scores_relax`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `system_settings`
--
ALTER TABLE `system_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- 테이블의 AUTO_INCREMENT `tokens`
--
ALTER TABLE `tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;

--
-- 테이블의 AUTO_INCREMENT `users_achievements`
--
ALTER TABLE `users_achievements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `users_beatmap_playcount`
--
ALTER TABLE `users_beatmap_playcount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `users_relationships`
--
ALTER TABLE `users_relationships`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `users_stats`
--
ALTER TABLE `users_stats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;

--
-- 테이블의 AUTO_INCREMENT `user_badges`
--
ALTER TABLE `user_badges`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 테이블의 AUTO_INCREMENT `user_clans`
--
ALTER TABLE `user_clans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
