-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 18, 2025 at 02:55 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `merchco`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

DROP TABLE IF EXISTS `adminapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_district` (
  `district_id` int(11) NOT NULL AUTO_INCREMENT,
  `districtname` varchar(50) NOT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`district_id`, `districtname`) VALUES
(8, 'Pathanamthitta'),
(7, 'Kollam'),
(6, 'Thiruvanathapuram'),
(9, 'Alappuzha'),
(10, 'Idukki'),
(11, 'Eranakulam'),
(12, 'Thrissur'),
(13, 'Palakkad'),
(14, 'Kozhikode'),
(16, 'Malappuram');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

DROP TABLE IF EXISTS `adminapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `locationname` varchar(50) NOT NULL,
  `district_id_id` int(11) NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `adminapp_tbl_ocation_district_id_id_1a3eca0b` (`district_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`location_id`, `locationname`, `district_id_id`) VALUES
(12, 'Karunagapally', 7),
(11, 'Neyyanttinkara', 6),
(10, 'Varkala', 6),
(9, 'Kovalam', 6),
(13, 'Kottakakkara', 7),
(14, 'Paravur', 7),
(15, 'Adoor', 8),
(16, 'Thiruvalla', 8),
(17, 'Cherthala', 9),
(18, 'Kayamkulam', 9),
(19, 'Thodupuzha', 10),
(20, 'Cheruthoni', 10),
(21, 'Kakkanad', 11),
(22, 'Kochi', 11),
(23, 'Painav', 10),
(24, 'batheri', 14),
(26, 'Muvattupuzha', 11);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_member`
--

DROP TABLE IF EXISTS `adminapp_tbl_member`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_member` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `membername` varchar(50) NOT NULL,
  `memberphoto` varchar(100) NOT NULL,
  `licensephoto` varchar(100) NOT NULL,
  `mobile_no` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `login_id_id` int(11) NOT NULL,
  `unit_id_id` int(11) NOT NULL,
  `memberclass` varchar(50) NOT NULL,
  `membercode` int(11) NOT NULL,
  PRIMARY KEY (`member_id`),
  KEY `adminapp_tbl_member_login_id_id_f1de750d` (`login_id_id`),
  KEY `adminapp_tbl_member_unit_id_id_5c7ba68e` (`unit_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_member`
--

INSERT INTO `adminapp_tbl_member` (`member_id`, `membername`, `memberphoto`, `licensephoto`, `mobile_no`, `email`, `designation`, `login_id_id`, `unit_id_id`, `memberclass`, `membercode`) VALUES
(11, 'Ajmal', 'man1_HzUAXu7.png', 'lisence1_kqiwc36.jpeg', 6574215986, 'ajmal@gmail.com', 'member', 35, 9, 'A-class', 6541000),
(12, 'Ajay', 'man1_CK6Itk1.png', 'lisence1_jlX8M1r.jpeg', 9544019435, 'ajaymanoj977@gmail.com', 'member', 37, 17, 'A-class', 2255),
(13, 'Abhijith s', 'person4_r4cNvtA.jpg', 'lisence2.jpeg', 9854213654, 'abhijith@gmail.com', 'member', 38, 10, 'C-class', 78546),
(14, 'Anandhu', 'person2.jpg', 'lisence1_mrynRjd.jpeg', 9654125487, 'anandhubabu90722@gmail.com', 'member', 40, 16, 'C-class', 97854),
(15, 'Ameeshh', 'person4_kCMsWua.jpg', 'lisence2_R5TMSym.jpeg', 9875463254, 'meeraaziz963@gmail.com', 'member', 41, 20, 'A-class', 2255),
(16, 'Akash', 'person2_VYk4OEy.jpg', 'lisence1_kqiwc36_F6vC2g1.jpeg', 6541236598, 'akash@gmail.com', 'member', 42, 17, 'A-class', 63542),
(17, 'Anandhu', 'bridatmakeup_6bTqdBb_LSsuo1e.jpg', 'baptism_photo_ex2Ya0R.jpg', 9654125487, 'anandhubabu9072@gmail.com', 'member', 43, 20, 'A-class', 97854),
(18, 'Ajay Manoj', 'man1_wjyQ0ry_E81QQwF.png', 'Screenshot_1_h1Is4C5.png', 9544019435, 'ajaymanoj977@gmail.com', 'member', 44, 12, 'A-class', 9546),
(19, 'Siva', 'person4_BdGrCgm.jpg', 'lisence1_mrynRjd_CHNA5mI.jpeg', 9564125498, 'sivaprasadc342@gmail.com', 'User', 45, 16, 'C-class', 5469),
(20, 'Alan Tomy', 'man1_CK6Itk1_HlmbmxZ.png', 'lisence1_mrynRjd_d3n7ZQR.jpeg', 8754625458, 'alantomy2309@gmail.com', 'member', 46, 7, 'A-class', 9854),
(21, 'Anamika', 'person2_VYk4OEy_jMYwAVn.jpg', 'lisence1_mrynRjd_K0NNcvu.jpeg', 8654754532, 'anamikark2023@gmail.com', 'member', 47, 14, 'A-class', 8546),
(24, 'meera', 'person4_kWcgwDo.jpg', 'lisence1_GjiUeEA.jpeg', 7890345679, 'meeraaziz963@gmail.com', 'member', 50, 20, 'A-class', 3456),
(26, 'Anuja', 'photoshoot_pfIqvys.jpg', 'camera_cAM9syx.png', 9854231456, 'meeraaziz963@gmail.com', 'member', 52, 15, 'C-class', 564),
(27, 'nija', 'free-images_knd3U0K.png', 'bird-8788491_1280_Gd6lMDJ.webp', 7890345679, 'meeraaziz963@gmail.com', 'dfg', 53, 17, 'A-class', 10003),
(28, 'sajini', 'free-images_ENSY0nR.png', 'cater_PrNUoLc.png', 9544019435, 'ajaymanoj977@gmail.com', 'member', 54, 19, 'C-class', 6541);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_notification`
--

DROP TABLE IF EXISTS `adminapp_tbl_notification`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notificationtitle` varchar(100) NOT NULL,
  `notificationdescription` varchar(500) NOT NULL,
  `expirydate` date NOT NULL,
  `notificationstatus` varchar(50) NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_notification`
--

INSERT INTO `adminapp_tbl_notification` (`notification_id`, `notificationtitle`, `notificationdescription`, `expirydate`, `notificationstatus`, `date`) VALUES
(7, 'notification', 'meetings', '2025-03-26', 'created', '2025-03-13'),
(8, 'sdfg', 'fgh', '2025-03-22', 'cancelled', '2025-03-13');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_unit`
--

DROP TABLE IF EXISTS `adminapp_tbl_unit`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_unit` (
  `unit_id` int(11) NOT NULL AUTO_INCREMENT,
  `unitname` varchar(50) NOT NULL,
  `district_id_id` int(11) NOT NULL,
  PRIMARY KEY (`unit_id`),
  KEY `adminapp_tbl_unit_district_id_id_5b216920` (`district_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_unit`
--

INSERT INTO `adminapp_tbl_unit` (`unit_id`, `unitname`, `district_id_id`) VALUES
(10, 'Karunagapalli', 7),
(9, 'Kovalam', 6),
(8, 'Varkala', 6),
(7, 'Neyyatinkara', 6),
(11, 'Kottarakkara', 7),
(12, 'Paravur', 7),
(13, 'Adoor', 8),
(14, 'Thiruvalla', 8),
(15, 'Cherthala', 9),
(16, 'Kayamkulam', 9),
(17, 'Thodupuzha', 10),
(18, 'Cheruthoni', 10),
(19, 'Kakkanad', 11),
(20, 'Kochi', 11),
(21, 'Batheri', 14);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_welfare`
--

DROP TABLE IF EXISTS `adminapp_tbl_welfare`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_welfare` (
  `welfare_id` int(11) NOT NULL AUTO_INCREMENT,
  `welfaretitle` varchar(50) NOT NULL,
  `welfarepurpose` varchar(250) NOT NULL,
  `welfare` varchar(500) NOT NULL,
  `welfaredate` date NOT NULL,
  `amount` double NOT NULL,
  `creditedby` varchar(50) NOT NULL,
  `welfarestatus` varchar(50) NOT NULL,
  PRIMARY KEY (`welfare_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_welfare`
--

INSERT INTO `adminapp_tbl_welfare` (`welfare_id`, `welfaretitle`, `welfarepurpose`, `welfare`, `welfaredate`, `amount`, `creditedby`, `welfarestatus`) VALUES
(10, 'Death Welfare', 'A member from unit Thodupuzha passed away. This welfare is to support his family.', '', '2025-02-13', 700, 'admin', 'published'),
(11, 'Death of a member', 'For the family of the late member', '', '2025-02-15', 300, 'admin', 'inactivated'),
(9, 'Donation', 'Donation for the family of a member', '', '2025-02-21', 500, 'admin', 'published'),
(12, 'Member died', 'member from unit varkala is passed away', '', '2025-02-21', 400, 'admin', 'published'),
(13, 'Donation', 'Donation for family.', '', '2025-02-18', 350, 'admin', 'published'),
(14, 'Welfare', 'This is a welfare', '', '2025-02-28', 450, 'admin', 'inactivated'),
(15, 'Donation', 'aaaaaaa', '', '2025-02-28', 20000, 'admin', 'inactivated'),
(16, 'Death Welfare', 'Donation', '', '2025-02-28', 200, 'admin', 'inactivated'),
(17, 'Death of a member', 'purpose', '', '2025-03-08', 240, 'admin', 'inactivated'),
(18, 'abcd', 'dfg', '', '2025-03-20', 500, 'admin', 'inactivated');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_welfarepublish`
--

DROP TABLE IF EXISTS `adminapp_tbl_welfarepublish`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_welfarepublish` (
  `welfarepublish_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id_id` int(11) NOT NULL,
  `welfare_id_id` int(11) NOT NULL,
  PRIMARY KEY (`welfarepublish_id`),
  KEY `adminapp_tbl_welfarepublish_member_id_id_d9f66cc7` (`member_id_id`),
  KEY `adminapp_tbl_welfarepublish_welfare_id_id_9bf1bfb6` (`welfare_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_welfarepublish`
--

INSERT INTO `adminapp_tbl_welfarepublish` (`welfarepublish_id`, `member_id_id`, `welfare_id_id`) VALUES
(11, 12, 14),
(10, 13, 12),
(9, 15, 13),
(8, 11, 9),
(7, 11, 10),
(12, 16, 14),
(13, 15, 18),
(14, 15, 17);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add login', 7, 'add_login'),
(26, 'Can change login', 7, 'change_login'),
(27, 'Can delete login', 7, 'delete_login'),
(28, 'Can view login', 7, 'view_login'),
(29, 'Can add tbl_district', 8, 'add_tbl_district'),
(30, 'Can change tbl_district', 8, 'change_tbl_district'),
(31, 'Can delete tbl_district', 8, 'delete_tbl_district'),
(32, 'Can view tbl_district', 8, 'view_tbl_district'),
(33, 'Can add tbl_ocation', 9, 'add_tbl_ocation'),
(34, 'Can change tbl_ocation', 9, 'change_tbl_ocation'),
(35, 'Can delete tbl_ocation', 9, 'delete_tbl_ocation'),
(36, 'Can view tbl_ocation', 9, 'view_tbl_ocation'),
(37, 'Can add tbl_location', 9, 'add_tbl_location'),
(38, 'Can change tbl_location', 9, 'change_tbl_location'),
(39, 'Can delete tbl_location', 9, 'delete_tbl_location'),
(40, 'Can view tbl_location', 9, 'view_tbl_location'),
(41, 'Can add tbl_unit', 10, 'add_tbl_unit'),
(42, 'Can change tbl_unit', 10, 'change_tbl_unit'),
(43, 'Can delete tbl_unit', 10, 'delete_tbl_unit'),
(44, 'Can view tbl_unit', 10, 'view_tbl_unit'),
(45, 'Can add tbl_member', 11, 'add_tbl_member'),
(46, 'Can change tbl_member', 11, 'change_tbl_member'),
(47, 'Can delete tbl_member', 11, 'delete_tbl_member'),
(48, 'Can view tbl_member', 11, 'view_tbl_member'),
(49, 'Can add tbl_welfare', 12, 'add_tbl_welfare'),
(50, 'Can change tbl_welfare', 12, 'change_tbl_welfare'),
(51, 'Can delete tbl_welfare', 12, 'delete_tbl_welfare'),
(52, 'Can view tbl_welfare', 12, 'view_tbl_welfare'),
(53, 'Can add tbl_deposite', 13, 'add_tbl_deposite'),
(54, 'Can change tbl_deposite', 13, 'change_tbl_deposite'),
(55, 'Can delete tbl_deposite', 13, 'delete_tbl_deposite'),
(56, 'Can view tbl_deposite', 13, 'view_tbl_deposite'),
(57, 'Can add tbl_loan', 14, 'add_tbl_loan'),
(58, 'Can change tbl_loan', 14, 'change_tbl_loan'),
(59, 'Can delete tbl_loan', 14, 'delete_tbl_loan'),
(60, 'Can view tbl_loan', 14, 'view_tbl_loan'),
(61, 'Can add tbl_notification', 15, 'add_tbl_notification'),
(62, 'Can change tbl_notification', 15, 'change_tbl_notification'),
(63, 'Can delete tbl_notification', 15, 'delete_tbl_notification'),
(64, 'Can view tbl_notification', 15, 'view_tbl_notification'),
(65, 'Can add tbl_welfarepublish', 16, 'add_tbl_welfarepublish'),
(66, 'Can change tbl_welfarepublish', 16, 'change_tbl_welfarepublish'),
(67, 'Can delete tbl_welfarepublish', 16, 'delete_tbl_welfarepublish'),
(68, 'Can view tbl_welfarepublish', 16, 'view_tbl_welfarepublish'),
(69, 'Can add tbl_welfaretransaction', 17, 'add_tbl_welfaretransaction'),
(70, 'Can change tbl_welfaretransaction', 17, 'change_tbl_welfaretransaction'),
(71, 'Can delete tbl_welfaretransaction', 17, 'delete_tbl_welfaretransaction'),
(72, 'Can view tbl_welfaretransaction', 17, 'view_tbl_welfaretransaction'),
(73, 'Can add tbl_loantransaction', 18, 'add_tbl_loantransaction'),
(74, 'Can change tbl_loantransaction', 18, 'change_tbl_loantransaction'),
(75, 'Can delete tbl_loantransaction', 18, 'delete_tbl_loantransaction'),
(76, 'Can view tbl_loantransaction', 18, 'view_tbl_loantransaction');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'guestapp', 'login'),
(8, 'adminapp', 'tbl_district'),
(9, 'adminapp', 'tbl_location'),
(10, 'adminapp', 'tbl_unit'),
(11, 'adminapp', 'tbl_member'),
(12, 'adminapp', 'tbl_welfare'),
(13, 'memberapp', 'tbl_deposite'),
(14, 'memberapp', 'tbl_loan'),
(15, 'adminapp', 'tbl_notification'),
(16, 'adminapp', 'tbl_welfarepublish'),
(17, 'memberapp', 'tbl_welfaretransaction'),
(18, 'memberapp', 'tbl_loantransaction');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-01-14 05:24:34.836868'),
(2, 'auth', '0001_initial', '2025-01-14 05:24:34.989053'),
(3, 'admin', '0001_initial', '2025-01-14 05:24:35.038728'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-01-14 05:24:35.045357'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-14 05:24:35.053186'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-01-14 05:24:35.076520'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-01-14 05:24:35.093611'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-01-14 05:24:35.106912'),
(9, 'auth', '0004_alter_user_username_opts', '2025-01-14 05:24:35.113659'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-01-14 05:24:35.126130'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-01-14 05:24:35.128540'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-01-14 05:24:35.137576'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-01-14 05:24:35.155786'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-01-14 05:24:35.173612'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-01-14 05:24:35.188323'),
(16, 'auth', '0011_update_proxy_permissions', '2025-01-14 05:24:35.194240'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-01-14 05:24:35.206738'),
(18, 'guestapp', '0001_initial', '2025-01-14 05:24:35.212123'),
(19, 'sessions', '0001_initial', '2025-01-14 05:24:35.223403'),
(20, 'adminapp', '0001_initial', '2025-01-14 06:41:41.874132'),
(21, 'adminapp', '0002_tbl_ocation', '2025-01-14 11:53:45.642421'),
(22, 'adminapp', '0003_rename_tbl_ocation_tbl_location', '2025-01-14 11:55:07.964646'),
(23, 'adminapp', '0004_tbl_unit', '2025-01-14 13:20:02.882730'),
(27, 'adminapp', '0006_alter_tbl_member_mobile_no', '2025-01-20 10:27:13.576877'),
(26, 'adminapp', '0005_tbl_member', '2025-01-17 10:11:23.007647'),
(28, 'adminapp', '0007_tbl_welfare', '2025-01-21 10:29:14.316091'),
(29, 'adminapp', '0008_tbl_member_memberclass_alter_tbl_welfare_welfare', '2025-01-25 08:54:48.962183'),
(30, 'memberapp', '0001_initial', '2025-01-25 08:54:48.993776'),
(31, 'memberapp', '0002_tbl_deposite_deposite', '2025-01-25 09:19:45.160502'),
(32, 'memberapp', '0003_alter_tbl_deposite_deposite_tbl_loan', '2025-01-27 06:45:39.354316'),
(33, 'adminapp', '0009_tbl_notification', '2025-01-27 06:48:45.871699'),
(34, 'memberapp', '0004_alter_tbl_deposite_depositedate', '2025-01-29 07:22:14.490621'),
(35, 'memberapp', '0005_tbl_loan_installmentpolicy_alter_tbl_loan_date', '2025-01-30 05:33:56.748675'),
(36, 'memberapp', '0006_rename_installmentpolicy_tbl_loan_installmentmonths', '2025-01-30 05:36:58.374831'),
(37, 'memberapp', '0007_tbl_loan_memberclass', '2025-02-03 09:06:49.096092'),
(38, 'memberapp', '0008_remove_tbl_loan_memberclass', '2025-02-03 09:20:36.907110'),
(39, 'adminapp', '0010_tbl_member_membercode', '2025-02-05 14:45:15.725405'),
(40, 'adminapp', '0011_tbl_welfarepublish', '2025-02-12 08:55:49.118851'),
(41, 'memberapp', '0009_tbl_welfaretransaction', '2025-02-14 06:40:49.275230'),
(42, 'memberapp', '0010_tbl_loan_approveddate', '2025-02-19 08:26:25.670504'),
(43, 'memberapp', '0011_tbl_loantransaction', '2025-02-21 05:53:54.997402'),
(44, 'adminapp', '0012_remove_tbl_notification_data_tbl_notification_date', '2025-02-27 07:08:27.198166'),
(45, 'memberapp', '0012_tbl_loantransaction_status', '2025-02-28 09:57:32.681975'),
(46, 'memberapp', '0013_tbl_loan_balanceamount', '2025-03-04 05:38:16.675074'),
(47, 'memberapp', '0014_tbl_loantransaction_fine_and_more', '2025-03-18 04:25:23.605213'),
(48, 'memberapp', '0015_alter_tbl_deposite_interestrate_and_more', '2025-03-18 14:49:54.373355');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('pqe0v9a54igmvp329ygxyj6fla4dzwwk', 'eyJsb2dpbmlkIjozMn0:1tesFF:pLcWzJDLwA34bwUgEmNYVC_Mpa_psTFBxhCNj2fgIAY', '2025-02-17 08:55:53.264750'),
('nn35tz5fjwrh7hl1uuz3gf3cxklzvvh0', 'eyJsb2dpbmlkIjozOCwid2VsZmFyZWlkIjoiNiJ9:1tfz20:nEkEgYqMC635d81JNb8KGrMn8VaqFF3Oo397PcZWpOQ', '2025-02-20 10:22:48.101769'),
('unxw1qrnynjwuhepd72ycorwrks0xaya', 'eyJsb2dpbmlkIjo1NH0:1tuYKl:v_jUCWGEUG2iinyQLU4fV7jAxYRsM70-VvNteNw_EsE', '2025-04-01 14:54:23.719599');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_login`
--

DROP TABLE IF EXISTS `guestapp_login`;
CREATE TABLE IF NOT EXISTS `guestapp_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `role` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_login`
--

INSERT INTO `guestapp_login` (`login_id`, `username`, `password`, `role`, `status`) VALUES
(53, 'nija', 'nija', 'customer', 'Accepted'),
(52, 'anuja', 'anuja', 'customer', 'Accepted'),
(51, 'anuja', 'anuja', 'customer', 'requested'),
(50, 'meera', 'meera', 'customer', 'Accepted'),
(47, 'anamika', 'anamika', 'customer', 'Rejected'),
(46, 'alan', 'alan', 'customer', 'Accepted'),
(45, 'siva', 'siva', 'customer', 'Accepted'),
(44, 'ajay', 'ajay', 'customer', 'Accepted'),
(43, 'anandhu', 'anandhu123', 'customer', 'Accepted'),
(41, 'ameesh', 'ameesh', 'customer', 'Accepted'),
(40, 'anandhu', 'anandhy', 'customer', 'Accepted'),
(38, 'abhijith', 'abhijith', 'customer', 'Accepted'),
(39, 'admin', 'admin', 'admin', ''),
(35, 'ajmal', 'ajmal', 'customer', ''),
(42, 'akash', 'akash', 'customer', 'Accepted'),
(54, 'sajini', 'sajini', 'customer', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `memberapp_tbl_deposite`
--

DROP TABLE IF EXISTS `memberapp_tbl_deposite`;
CREATE TABLE IF NOT EXISTS `memberapp_tbl_deposite` (
  `deposite_id` int(11) NOT NULL AUTO_INCREMENT,
  `depositedate` date NOT NULL,
  `matureddate` date DEFAULT NULL,
  `interestrate` double DEFAULT NULL,
  `matuedamount` double DEFAULT NULL,
  `member_id_id` int(11) NOT NULL,
  `deposite` double NOT NULL,
  PRIMARY KEY (`deposite_id`),
  KEY `memberapp_tbl_deposite_member_id_id_f42046c0` (`member_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `memberapp_tbl_deposite`
--

INSERT INTO `memberapp_tbl_deposite` (`deposite_id`, `depositedate`, `matureddate`, `interestrate`, `matuedamount`, `member_id_id`, `deposite`) VALUES
(4, '2025-02-25', '2030-02-25', 5, 62500, 16, 50000),
(3, '2026-02-06', '2027-02-06', 5, 10500, 13, 10000),
(5, '2025-03-10', '2027-03-10', 5, 48632.1, 18, 44211),
(6, '2025-03-10', '2027-03-10', 5, 60500, 15, 55000),
(7, '2025-03-12', '2026-03-12', 5, 1050, 15, 1000),
(9, '2025-03-13', '2027-03-13', 5, 220000, 15, 200000),
(10, '2025-03-17', '2026-03-17', 5, 52500, 15, 50000),
(11, '2025-03-17', '2028-03-17', 5, 115, 27, 100),
(13, '2025-03-18', NULL, NULL, NULL, 28, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `memberapp_tbl_loan`
--

DROP TABLE IF EXISTS `memberapp_tbl_loan`;
CREATE TABLE IF NOT EXISTS `memberapp_tbl_loan` (
  `loan_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `amount` double NOT NULL,
  `monthlyinterest` double NOT NULL,
  `monthlyamount` double NOT NULL,
  `loanstatus` varchar(20) NOT NULL,
  `member_id_id` int(11) NOT NULL,
  `installmentmonths` int(11) NOT NULL,
  `approveddate` date DEFAULT NULL,
  `balanceamount` double DEFAULT NULL,
  PRIMARY KEY (`loan_id`),
  KEY `memberapp_tbl_loan_member_id_id_ef32861e` (`member_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `memberapp_tbl_loan`
--

INSERT INTO `memberapp_tbl_loan` (`loan_id`, `date`, `amount`, `monthlyinterest`, `monthlyamount`, `loanstatus`, `member_id_id`, `installmentmonths`, `approveddate`, `balanceamount`) VALUES
(13, '2025-02-25', 100000, 833.33, 8791.59, 'Accepted', 13, 12, '2025-02-25', 91208.41),
(12, '2025-02-19', 500000, 4166.67, 23072.46, 'Accepted', 15, 24, '2025-01-01', NULL),
(14, '2025-02-25', 1000000, 8333.33, 46144.93, 'requested', 16, 24, NULL, NULL),
(15, '2025-03-04', 150000, 1250, 13187.38, 'Accepted', 16, 12, '2025-03-04', 136812.62),
(16, '2025-03-10', 250000, 2083.33, 11536.23, 'Accepted', 19, 24, '2025-03-17', 250000),
(17, '2025-03-10', 250000, 2083.33, 21978.97, 'Accepted', 18, 12, '2025-03-10', 250000),
(18, '2025-03-10', 100000000, 833333.33, 4614492.63, 'Rejected', 18, 24, NULL, 100000000),
(19, '2025-03-10', 421023, 3508.53, 37014.61, 'Accepted', 18, 12, '2025-03-10', 421023),
(20, '2025-03-10', 500000, 4166.67, 43957.94, 'Rejected', 18, 12, NULL, 500000),
(22, '2025-02-01', 100000, 833.33, 8791.59, 'Rejected', 15, 12, '2025-02-01', 100000),
(23, '2025-03-17', 100000, 833.33, 8791.59, 'Accepted', 24, 12, '2025-02-14', 56042.05000000002),
(24, '2025-03-17', 150000, 1250, 13187.38, 'requested', 15, 12, NULL, 150000),
(25, '2025-03-17', 45000, 375, 2076.52, 'Accepted', 27, 24, '2025-03-17', 45000);

-- --------------------------------------------------------

--
-- Table structure for table `memberapp_tbl_loantransaction`
--

DROP TABLE IF EXISTS `memberapp_tbl_loantransaction`;
CREATE TABLE IF NOT EXISTS `memberapp_tbl_loantransaction` (
  `loantrans_id` int(11) NOT NULL AUTO_INCREMENT,
  `paiddate` date NOT NULL,
  `loanamount` double NOT NULL,
  `amount` double NOT NULL,
  `loan_id_id` int(11) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `fine` int(11) DEFAULT NULL,
  `paidduedate` date DEFAULT NULL,
  PRIMARY KEY (`loantrans_id`),
  KEY `memberapp_tbl_loantransaction_loan_id_id_a7e0d308` (`loan_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `memberapp_tbl_loantransaction`
--

INSERT INTO `memberapp_tbl_loantransaction` (`loantrans_id`, `paiddate`, `loanamount`, `amount`, `loan_id_id`, `status`, `fine`, `paidduedate`) VALUES
(2, '2025-02-21', 500000, 23072.46, 12, NULL, NULL, NULL),
(3, '2025-02-25', 500000, 23072.46, 12, NULL, NULL, NULL),
(5, '2025-02-25', 500000, 23072.46, 12, NULL, NULL, NULL),
(31, '2025-03-18', 100000, 8791.59, 13, 'paid', 0, '2025-03-27'),
(8, '2025-02-28', 500000, 23072.46, 12, NULL, NULL, NULL),
(9, '2025-02-28', 500000, 23072.46, 12, NULL, NULL, NULL),
(10, '2025-02-28', 500000, 23072.46, 12, 'paid', NULL, NULL),
(11, '2025-02-28', 500000, 23072.46, 12, 'paid', NULL, NULL),
(12, '2025-02-28', 500000, 23072.46, 12, 'paid', NULL, NULL),
(13, '2025-03-03', 500000, 23072.46, 12, 'paid', NULL, NULL),
(16, '2025-03-04', 150000, 13187.38, 15, 'paid', NULL, NULL),
(24, '2025-03-17', 500000, 23072.46, 12, 'paid', NULL, NULL),
(25, '2025-03-17', 500000, 23072.46, 12, 'paid', NULL, NULL),
(26, '2025-03-17', 500000, 23072.46, 12, 'paid', NULL, NULL),
(27, '2025-03-17', 500000, 23072.46, 12, 'paid', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `memberapp_tbl_welfaretransaction`
--

DROP TABLE IF EXISTS `memberapp_tbl_welfaretransaction`;
CREATE TABLE IF NOT EXISTS `memberapp_tbl_welfaretransaction` (
  `trans_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `welfareamount` double NOT NULL,
  `member_id_id` int(11) NOT NULL,
  `welfare_id_id` int(11) NOT NULL,
  PRIMARY KEY (`trans_id`),
  KEY `memberapp_tbl_welfaretransaction_member_id_id_f1bb9260` (`member_id_id`),
  KEY `memberapp_tbl_welfaretransaction_welfare_id_id_a9bb19f3` (`welfare_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `memberapp_tbl_welfaretransaction`
--

INSERT INTO `memberapp_tbl_welfaretransaction` (`trans_id`, `date`, `welfareamount`, `member_id_id`, `welfare_id_id`) VALUES
(1, '2025-02-14', 350, 15, 13),
(2, '2025-03-12', 450, 16, 14),
(3, '2025-03-17', 350, 15, 13);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
