-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 24 mai 2022 à 15:28
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
