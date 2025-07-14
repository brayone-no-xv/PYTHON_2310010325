-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 27, 2025 at 03:57 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_2310010325`
--

-- --------------------------------------------------------

--
-- Table structure for table `keranjang`
--

CREATE TABLE `keranjang` (
  `id_keranjang` char(20) NOT NULL,
  `nama_menu` varchar(20) DEFAULT NULL,
  `qty` varchar(20) DEFAULT NULL,
  `catatan` varchar(20) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp(),
  `updated_at` timestamp NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `keranjang`
--

INSERT INTO `keranjang` (`id_keranjang`, `nama_menu`, `qty`, `catatan`, `created_at`, `updated_at`) VALUES
('A01', 'mie instan', 'tes', '', '2023-03-31 16:00:00', '2025-04-30 16:00:00'),
('A01', 'tes', 'tes', 'tes', '2025-06-26 13:02:46', '2025-06-26 13:02:46'),
('A01', 'tes', 'tes', 'tes', '2025-06-26 13:02:53', '2025-06-26 13:02:53'),
('A01', 'tes', 'tes', 'tes', '2025-06-26 13:03:38', '2025-06-26 13:03:38'),
('A10', 'book', 'dijual', 'tes', '2025-06-26 21:10:26', '2025-06-26 21:10:26'),
('A05', 'tes', 'tes', 'tes', '2025-06-26 20:28:29', '2025-06-26 20:28:29');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
