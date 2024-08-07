-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2024 at 08:09 AM
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
-- Database: `backup`
--

-- --------------------------------------------------------

--
-- Table structure for table `log_in_tbl`
--

CREATE TABLE `log_in_tbl` (
  `id` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log_in_tbl`
--

INSERT INTO `log_in_tbl` (`id`, `Username`, `Password`) VALUES
(1, 'hardik', '12345678'),
(4, 'sachin123', '10101010');

-- --------------------------------------------------------

--
-- Table structure for table `reg_table`
--

CREATE TABLE `reg_table` (
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `address` varchar(80) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobileno` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reg_table`
--

INSERT INTO `reg_table` (`fname`, `lname`, `address`, `email`, `mobileno`) VALUES
('hardik', 'parmar', 'rajkot', 'abc@gmail.com', 2147483647),
('sachin', 'kava', 'rajkot', 'xyz@gmail.com', 2147483647);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `log_in_tbl`
--
ALTER TABLE `log_in_tbl`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log_in_tbl`
--
ALTER TABLE `log_in_tbl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
