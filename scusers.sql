-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2016 at 12:36 AM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scusers`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `permalink` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `uri` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `avatar_url` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `full_name` varchar(200) CHARACTER SET utf32 COLLATE utf32_unicode_ci DEFAULT NULL,
  `city` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8_unicode_ci,
  `discogs_name` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `myspace_name` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website_title` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `online` tinyint(1) NOT NULL,
  `track_count` int(11) NOT NULL,
  `playlist_count` int(11) NOT NULL,
  `followers_count` int(11) NOT NULL,
  `followings_count` int(11) NOT NULL,
  `public_favorites_count` int(11) NOT NULL,
  `permalink_url` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `permalink`, `username`, `uri`, `avatar_url`, `country`, `full_name`, `city`, `description`, `discogs_name`, `myspace_name`, `website`, `website_title`, `online`, `track_count`, `playlist_count`, `followers_count`, `followings_count`, `public_favorites_count`, `permalink_url`) VALUES
(261157969, 'omar-flores-778306823', 'Omar Flores', 'https://api.soundcloud.com/users/261157969', 'https://i1.sndcdn.com/avatars-000271135364-iwf83d-large.jpg', NULL, 'Omar Flores', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 2, 'http://soundcloud.com/omar-flores-778306823'),
(261157970, 'zubeyda-farah', 'Zubeyda Farah', 'https://api.soundcloud.com/users/261157970', 'https://i1.sndcdn.com/avatars-000271135360-wpsvpt-large.jpg', NULL, 'Zubeyda Farah', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/zubeyda-farah'),
(261157971, 'user-740991858', 'User 740991858', 'https://api.soundcloud.com/users/261157971', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-740991858'),
(261157972, 'pande-putra-532430473', 'Pande Putra', 'https://api.soundcloud.com/users/261157972', 'https://i1.sndcdn.com/avatars-000271135365-arcj7o-large.jpg', NULL, 'Pande Putra', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/pande-putra-532430473'),
(261157973, 'noellehoward59150', 'NoelleHoward59150', 'https://api.soundcloud.com/users/261157973', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/noellehoward59150'),
(261157974, 'james-hocking-618227906', 'James Hocking', 'https://api.soundcloud.com/users/261157974', 'https://i1.sndcdn.com/avatars-000271135367-whh8p9-large.jpg', NULL, 'James Hocking', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 1, 1, 0, 'http://soundcloud.com/james-hocking-618227906'),
(261157975, 'matas-sutkus', 'Matas Sutkus', 'https://api.soundcloud.com/users/261157975', 'https://i1.sndcdn.com/avatars-000271135372-4y12yy-large.jpg', NULL, 'Matas Sutkus', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/matas-sutkus'),
(261157976, 'viridiana-ramirez-237897113', 'Viridiana Ramirez', 'https://api.soundcloud.com/users/261157976', 'https://i1.sndcdn.com/avatars-000271135374-m7xx5r-large.jpg', NULL, 'Viridiana Ramirez', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/viridiana-ramirez-237897113'),
(261157977, 'deni-rusdiana', 'Deni Rusdiana', 'https://api.soundcloud.com/users/261157977', 'https://i1.sndcdn.com/avatars-000271135375-jiued1-large.jpg', NULL, 'Deni Rusdiana', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 1, 0, 'http://soundcloud.com/deni-rusdiana'),
(261157979, 'user-400296535', 'mersilous_hot_head', 'https://api.soundcloud.com/users/261157979', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 1, 0, 0, 0, 'http://soundcloud.com/user-400296535'),
(261157980, 'user-283004352', 'Natascha', 'https://api.soundcloud.com/users/261157980', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 1, 'http://soundcloud.com/user-283004352'),
(261157981, 'user-643159012', 'User 643159012', 'https://api.soundcloud.com/users/261157981', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-643159012'),
(261157982, 'user-129365849', 'User 129365849', 'https://api.soundcloud.com/users/261157982', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-129365849'),
(261157983, 'user-542130632', 'User 542130632', 'https://api.soundcloud.com/users/261157983', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-542130632'),
(261157984, 'gabriel-vasquez-855634737', 'Gabriel Vasquez', 'https://api.soundcloud.com/users/261157984', 'https://i1.sndcdn.com/avatars-000271135378-o2kxc9-large.jpg', NULL, 'Gabriel Vasquez', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/gabriel-vasquez-855634737'),
(261157985, 'eitann-mallin', 'Eitann Mallin', 'https://api.soundcloud.com/users/261157985', 'https://i1.sndcdn.com/avatars-000271135379-gzk9kr-large.jpg', NULL, 'Eitann Mallin', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/eitann-mallin'),
(261157986, 'user-167656798', 'Suzann Schwartz', 'https://api.soundcloud.com/users/261157986', 'https://i1.sndcdn.com/avatars-000271135561-zna1ts-large.jpg', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-167656798'),
(261157987, 'user-286209941', 'User 286209941', 'https://api.soundcloud.com/users/261157987', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 1, 0, 'http://soundcloud.com/user-286209941'),
(261157988, 'anneli-hagel', 'Anneli Hagel', 'https://api.soundcloud.com/users/261157988', 'https://i1.sndcdn.com/avatars-000271135381-wkcwso-large.jpg', NULL, 'Anneli Hagel', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/anneli-hagel'),
(261157989, 'user-368802328', 'User 368802328', 'https://api.soundcloud.com/users/261157989', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 1, 'http://soundcloud.com/user-368802328'),
(261157990, 'user-636760216', 'User 636760216', 'https://api.soundcloud.com/users/261157990', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 1, 'http://soundcloud.com/user-636760216'),
(261157991, 'user-235981348', 'Otha Flynn', 'https://api.soundcloud.com/users/261157991', 'https://i1.sndcdn.com/avatars-000271135876-gwbwy5-large.jpg', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-235981348'),
(261157992, 'user-218921177', 'Keith Lethal', 'https://api.soundcloud.com/users/261157992', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-218921177'),
(261157993, 'user-379820923', 'lauren', 'https://api.soundcloud.com/users/261157993', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-379820923'),
(261157994, 'jorge-luis-tarazona', 'Jorge Luis Tarazona', 'https://api.soundcloud.com/users/261157994', 'https://i1.sndcdn.com/avatars-000271135383-2ufznm-large.jpg', NULL, 'Jorge Tarazona', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/jorge-luis-tarazona'),
(261157995, 'user-182754120', 'niyahh', 'https://api.soundcloud.com/users/261157995', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 44, 'http://soundcloud.com/user-182754120'),
(261157996, 'user-94669484', 'louie', 'https://api.soundcloud.com/users/261157996', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-94669484'),
(261157998, 'kayshann-sphann', 'Kayshann Sphann', 'https://api.soundcloud.com/users/261157998', 'https://i1.sndcdn.com/avatars-000271135385-1pw6bt-large.jpg', NULL, 'Kayshann Sphann', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/kayshann-sphann'),
(261158000, 'squirtle-squad-192412799', 'Squirtle Squad', 'https://api.soundcloud.com/users/261158000', 'https://i1.sndcdn.com/avatars-000271135386-noxqgn-large.jpg', NULL, 'Squirtle Squad', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/squirtle-squad-192412799'),
(261158001, 'pemba-lama-665211288', 'Pemba Lama', 'https://api.soundcloud.com/users/261158001', 'https://i1.sndcdn.com/avatars-000271135388-tjzgok-large.jpg', NULL, 'Pemba Lama', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/pemba-lama-665211288'),
(261158003, 'luis-quintana-ruiz', 'Luis Quintana Ruiz', 'https://api.soundcloud.com/users/261158003', 'https://i1.sndcdn.com/avatars-000271135390-3yyth3-large.jpg', NULL, 'Luis Quintana Ruiz', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/luis-quintana-ruiz'),
(261158004, 'yamileth-alvarex', 'Yamileth Alvarex', 'https://api.soundcloud.com/users/261158004', 'https://i1.sndcdn.com/avatars-000271135391-umdie5-large.jpg', NULL, 'Yamileth Alvarex', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 6, 'http://soundcloud.com/yamileth-alvarex'),
(261158005, 'user-692377762', 'User 692377762', 'https://api.soundcloud.com/users/261158005', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-692377762'),
(261158006, 'jeison-rivera-54645346', 'Jeison Rivera', 'https://api.soundcloud.com/users/261158006', 'https://i1.sndcdn.com/avatars-000271135392-yhi6x9-large.jpg', NULL, 'Jeison Rivera', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/jeison-rivera-54645346'),
(261158007, 'user-324679746', 'CarlosLTorres', 'https://api.soundcloud.com/users/261158007', 'https://a1.sndcdn.com/images/default_avatar_large.png', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/user-324679746'),
(261158008, 'kathleen-la-spina', 'Kathleen La Spina', 'https://api.soundcloud.com/users/261158008', 'https://i1.sndcdn.com/avatars-000271135393-m42q45-large.jpg', NULL, 'Kathleen La Spina', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/kathleen-la-spina'),
(261158009, 'tj-howell-725280808', 'TJ Howell', 'https://api.soundcloud.com/users/261158009', 'https://i1.sndcdn.com/avatars-000271135394-w598su-large.jpg', NULL, 'TJ Howell', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 'http://soundcloud.com/tj-howell-725280808'),
(261158010, 'pia-hugo', 'Pia Hugo', 'https://api.soundcloud.com/users/261158010', 'https://i1.sndcdn.com/avatars-000271135396-q0dovo-large.jpg', NULL, 'Pia Hugo', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 1, 'http://soundcloud.com/pia-hugo');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
