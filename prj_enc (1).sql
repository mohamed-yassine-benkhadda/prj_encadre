-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 24 mai 2022 à 15:30
-- Version du serveur :  5.7.31
-- Version de PHP : 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `prj_enc`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(40) NOT NULL,
  `prenom` varchar(40) NOT NULL,
  `tel` varchar(10) NOT NULL,
  `mail` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
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
-- Structure de la table `auth_group_permissions`
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
-- Structure de la table `auth_permission`
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
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_permission`
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
(25, 'Can add admin', 7, 'add_admin'),
(26, 'Can change admin', 7, 'change_admin'),
(27, 'Can delete admin', 7, 'delete_admin'),
(28, 'Can view admin', 7, 'view_admin'),
(29, 'Can add plante', 8, 'add_plante'),
(30, 'Can change plante', 8, 'change_plante'),
(31, 'Can delete plante', 8, 'delete_plante'),
(32, 'Can view plante', 8, 'view_plante'),
(33, 'Can add plante zone', 9, 'add_plantezone'),
(34, 'Can change plante zone', 9, 'change_plantezone'),
(35, 'Can delete plante zone', 9, 'delete_plantezone'),
(36, 'Can view plante zone', 9, 'view_plantezone'),
(37, 'Can add tache', 10, 'add_tache'),
(38, 'Can change tache', 10, 'change_tache'),
(39, 'Can delete tache', 10, 'delete_tache'),
(40, 'Can view tache', 10, 'view_tache'),
(41, 'Can add technicien', 11, 'add_technicien'),
(42, 'Can change technicien', 11, 'change_technicien'),
(43, 'Can delete technicien', 11, 'delete_technicien'),
(44, 'Can view technicien', 11, 'view_technicien'),
(45, 'Can add technicien zone', 12, 'add_technicienzone'),
(46, 'Can change technicien zone', 12, 'change_technicienzone'),
(47, 'Can delete technicien zone', 12, 'delete_technicienzone'),
(48, 'Can view technicien zone', 12, 'view_technicienzone'),
(49, 'Can add utilisateur', 13, 'add_utilisateur'),
(50, 'Can change utilisateur', 13, 'change_utilisateur'),
(51, 'Can delete utilisateur', 13, 'delete_utilisateur'),
(52, 'Can view utilisateur', 13, 'view_utilisateur'),
(53, 'Can add zone', 14, 'add_zone'),
(54, 'Can change zone', 14, 'change_zone'),
(55, 'Can delete zone', 14, 'delete_zone'),
(56, 'Can view zone', 14, 'view_zone'),
(57, 'Can add demande', 15, 'add_demande'),
(58, 'Can change demande', 15, 'change_demande'),
(59, 'Can delete demande', 15, 'delete_demande'),
(60, 'Can view demande', 15, 'view_demande');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
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
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$shmfJQD9FPfwaMSN8XaZM5$C6BQajElgK06CHBd2Ud4yBMwsc08gnVeXkcTvsvVDkU=', '2022-05-24 11:55:56.198008', 1, 'admin@gmail.com', '', '', 'mybenkhadda@gmail.com', 1, 1, '2022-05-21 20:31:05.145708'),
(2, 'pbkdf2_sha256$260000$sLDJfoTkmbjSlvLEbKAIRm$No5Muc/F05UuKLjo/cVtl9J6q5z9j5CrnoDVFv7w+BE=', '2022-05-23 18:54:56.950201', 0, 'mybenkhadda@gmail.com', '', '', '', 1, 1, '2022-05-22 16:27:23.000000'),
(4, 'pbkdf2_sha256$260000$HxcHDEK0b7X1ymSsNE3P3l$YhyJDeTTr1vSCbKzJ9eMi9YFokcCaDw04QRhaoh/W/M=', '2022-05-24 10:31:44.213051', 0, 'oa_amaziane@gmail.com', '', '', 'oa_amaziane@gmail.com', 1, 1, '2022-05-23 21:29:46.083605');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
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
-- Structure de la table `auth_user_user_permissions`
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
-- Structure de la table `demande`
--

DROP TABLE IF EXISTS `demande`;
CREATE TABLE IF NOT EXISTS `demande` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_utilisateur` int(11) NOT NULL,
  `id_admin` int(11) NOT NULL,
  `type_demande` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `jour` datetime(6) NOT NULL,
  `adresse` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
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
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-05-22 14:50:36.372551', '1', 'Jardin Hassan 2', 1, '[{\"added\": {}}]', 14, 1),
(2, '2022-05-22 14:57:24.511623', '1', 'Jardin Majorel', 2, '[{\"changed\": {\"fields\": [\"Nom\", \"Public\", \"Prix\", \"Image\"]}}]', 14, 1),
(3, '2022-05-22 14:58:44.019836', '1', 'Jardin Majorel', 3, '', 14, 1),
(4, '2022-05-22 16:27:24.045909', '2', 'mybenkhadda@gmail.com', 1, '[{\"added\": {}}]', 4, 1),
(5, '2022-05-22 16:27:53.657148', '2', 'mybenkhadda@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 4, 1),
(6, '2022-05-23 16:13:57.898885', '2', 'Botanical Garden', 1, '[{\"added\": {}}]', 14, 1),
(7, '2022-05-24 11:58:12.438237', '3', 'Urban Forest Ibn Sina \"Hilton\"', 1, '[{\"added\": {}}]', 14, 1),
(8, '2022-05-24 12:12:33.073947', '3', 'Les Jardins Exotiques de Bouknadel', 2, '[{\"changed\": {\"fields\": [\"Nom\", \"Adresse\", \"Public\", \"Prix\", \"Description\", \"Image\"]}}]', 14, 1),
(9, '2022-05-24 12:20:33.387214', '4', 'Hassan II Park', 1, '[{\"added\": {}}]', 14, 1),
(10, '2022-05-24 12:33:40.362605', '4', 'Nouzhat Hassan Garden', 2, '[{\"changed\": {\"fields\": [\"Nom\", \"Adresse\", \"Superficie\", \"Description\", \"Image\"]}}]', 14, 1),
(11, '2022-05-24 13:09:48.929233', '2', 'Jardin Botanique d\'Essais, Av. Annasr', 2, '[{\"changed\": {\"fields\": [\"Nom\", \"Adresse\", \"Superficie\", \"Manger\"]}}]', 14, 1),
(12, '2022-05-24 13:20:51.675427', '5', 'Jardin Zoologique de Rabat', 1, '[{\"added\": {}}]', 14, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'main_app', 'admin'),
(8, 'main_app', 'plante'),
(9, 'main_app', 'plantezone'),
(10, 'main_app', 'tache'),
(11, 'main_app', 'technicien'),
(12, 'main_app', 'technicienzone'),
(13, 'main_app', 'utilisateur'),
(14, 'main_app', 'zone'),
(15, 'main_app', 'demande');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-21 19:47:10.210972'),
(2, 'auth', '0001_initial', '2022-05-21 19:47:10.741245'),
(3, 'admin', '0001_initial', '2022-05-21 19:47:10.881824'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-21 19:47:10.898820'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-21 19:47:10.913819'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-21 19:47:10.991821'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-21 19:47:11.033822'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-21 19:47:11.074824'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-21 19:47:11.089824'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-21 19:47:11.132826'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-21 19:47:11.137824'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-21 19:47:11.155824'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-21 19:47:11.198825'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-21 19:47:11.241825'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-21 19:47:11.282821'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-21 19:47:11.298833'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-21 19:47:11.340056'),
(18, 'main_app', '0001_initial', '2022-05-21 19:47:11.537870'),
(19, 'main_app', '0002_auto_20220521_2041', '2022-05-21 19:47:11.601742'),
(20, 'main_app', '0003_auto_20220521_2047', '2022-05-21 19:47:11.659743'),
(21, 'sessions', '0001_initial', '2022-05-21 19:47:11.712747'),
(22, 'main_app', '0004_alter_zone_prix', '2022-05-22 14:44:22.063722'),
(23, 'main_app', '0005_auto_20220522_1550', '2022-05-22 14:50:14.011931'),
(24, 'main_app', '0006_alter_zone_image', '2022-05-22 14:56:33.079976'),
(25, 'main_app', '0007_auto_20220522_1630', '2022-05-22 15:30:09.230200'),
(26, 'main_app', '0008_auto_20220522_1634', '2022-05-22 15:34:57.700979');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
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
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('a71b506j8ym8cg9ya9g5977ugr92pj2s', '.eJxVjEEOwiAQRe_C2hAGpgVcuu8ZmhkGbdVAUtqV8e7apAvd_vfef6mRtnUat5aXcRZ1VqBOvxtTeuSyA7lTuVWdalmXmfWu6IM2PVTJz8vh_h1M1KZvnUxkiQTIQTrresLO9oLgJZADQgtMIZreM0cr5koWwaWM4sEG7FC9P9UKNys:1ntT8m:AYVZee6QYolYqMiRgRvhMxKIRr8Ms_wLq-dE7GzcOrY', '2022-06-07 11:55:56.203009');

-- --------------------------------------------------------

--
-- Structure de la table `plante`
--

DROP TABLE IF EXISTS `plante`;
CREATE TABLE IF NOT EXISTS `plante` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `besoin_eau` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `plantezone`
--

DROP TABLE IF EXISTS `plantezone`;
CREATE TABLE IF NOT EXISTS `plantezone` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_zone` int(11) NOT NULL,
  `id_plante` int(11) NOT NULL,
  `dernier_arr` datetime(6) NOT NULL,
  `prochain_arr` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `tache`
--

DROP TABLE IF EXISTS `tache`;
CREATE TABLE IF NOT EXISTS `tache` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_admin` int(11) NOT NULL,
  `id_tech` int(11) NOT NULL,
  `adresse` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `technicien`
--

DROP TABLE IF EXISTS `technicien`;
CREATE TABLE IF NOT EXISTS `technicien` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(40) NOT NULL,
  `prenom` varchar(40) NOT NULL,
  `tel` varchar(10) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `department` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `technicienzone`
--

DROP TABLE IF EXISTS `technicienzone`;
CREATE TABLE IF NOT EXISTS `technicienzone` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_zone` int(11) NOT NULL,
  `id_tech` int(11) NOT NULL,
  `id_resp` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(40) NOT NULL,
  `prenom` varchar(40) NOT NULL,
  `tel` varchar(10) NOT NULL,
  `mail` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `zone`
--

DROP TABLE IF EXISTS `zone`;
CREATE TABLE IF NOT EXISTS `zone` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(40) NOT NULL,
  `adresse` varchar(200) NOT NULL,
  `superficie` int(11) NOT NULL,
  `public` varchar(50) NOT NULL,
  `prix` int(11) DEFAULT NULL,
  `id_utilisateur` int(11) DEFAULT NULL,
  `picnic` tinyint(1) NOT NULL,
  `camping` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext,
  `manger` tinyint(1) NOT NULL,
  `lat` double DEFAULT NULL,
  `lon` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `zone`
--

INSERT INTO `zone` (`id`, `nom`, `adresse`, `superficie`, `public`, `prix`, `id_utilisateur`, `picnic`, `camping`, `image`, `description`, `manger`, `lat`, `lon`) VALUES
(2, 'Jardin Botanique d\'Essais, Av. Annasr', 'Jardin Botanique d\'Essais, Av. Annasr, Rabat', 20, 'Public', 0, NULL, 1, 0, 'Zone/2022-02-06.jpg', 'botanical garden, also called botanic garden, originally, a collection of living plants designed chiefly to illustrate relationships within plant groups.', 1, 34.008986, -6.848435),
(3, 'Les Jardins Exotiques de Bouknadel', 'KM 13, Km 13 Rte de Rabat, Salé 11000', 120, 'Prive', 20, NULL, 1, 0, 'Zone/les-jardins-exotiques.jpg', 'Grâce à ses collections de plantes et d’animaux exotiques, ses multiples jardins et son circuit pédagogique, les Jardins exotiques de Bouknadel se classe parmi les plus importants et les plus beaux jardins du Maroc. Ils sont situés sur la route nationale n°1 à 10 Km de Salé vers Kenitra.', 1, 34.094718, -6.766013),
(4, 'Nouzhat Hassan Garden', '25C8+V9R, Rabat', 210, 'Public', 0, NULL, 0, 0, 'Zone/akb6.jpg', 'Tree-shaded park established in 1924, with a duck pond & a playground, plus a flower market nearby.', 1, 34.021174, -6.834706),
(5, 'Jardin Zoologique de Rabat', 'Annexe 23eme, (Ceinture verte), Cité Yacoub El Mansour,, Rabat', 50, 'Public', 0, NULL, 1, 0, 'Zone/jardin-rabat-678x381.jpg', 'Zoological park with 130 species in simulated mountain, desert, savanna & rainforest habitats.', 1, 33.9519345, -6.8957298);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
