-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2024 at 09:14 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carrentalsystem`
--
CREATE DATABASE IF NOT EXISTS `carrentalsystem` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `carrentalsystem`;

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
CREATE TABLE IF NOT EXISTS `cars` (
  `ID` int(11) NOT NULL  AUTO_INCREMENT PRIMARY KEY,
  `Brand` text NOT NULL,
  `Model` text NOT NULL,
  `Color` text NOT NULL,
  `Year` int(11) NOT NULL,
  `Price` double NOT NULL,
  `Available` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`Brand`, `Model`, `Color`, `Year`, `Price`, `Available`) VALUES
('Toyota', 'Corolla', 'White', 2019, 18000.50, 1),
('Honda', 'Civic', 'Black', 2020, 22000.00, 1),
('Ford', 'Mustang', 'Red', 2018, 35000.75, 2),
('Tesla', 'Model S', 'Blue', 2021, 79999.99, 1),
('BMW', 'X5', 'Gray', 2017, 45000.00, 0),
('Mercedes', 'C-Class', 'Silver', 2019, 38000.00, 2),
('Audi', 'A4', 'White', 2020, 40000.50, 1),
('Chevrolet', 'Camaro', 'Yellow', 2021, 37000.00, 0),
('Nissan', 'Altima', 'Blue', 2016, 15000.25, 2),
('Hyundai', 'Elantra', 'Green', 2018, 17000.00, 1);


-- --------------------------------------------------------

--
-- Table structure for table `rents`
--

DROP TABLE IF EXISTS `rents`;
CREATE TABLE IF NOT EXISTS `rents` (
  `ID` int(11) NOT NULL  AUTO_INCREMENT PRIMARY KEY,
  `user_id` int(11) NOT NULL,
  `car_id` int(11) NOT NULL ,
  `DateTime` text NOT NULL,
  `Hours` int(11) NOT NULL,
  `Total` double NOT NULL,
  `Status` int(11) NOT NULL , 
   FOREIGN KEY (`car_id`) REFERENCES cars (`ID`) ON DELETE CASCADE ON UPDATE CASCADE , 
   FOREIGN KEY (`user_id`) REFERENCES users (`ID`) ON DELETE CASCADE ON UPDATE CASCADE 

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rents`
--

INSERT INTO `rents` (`ID`, `user_id`, `car_id`, `DateTime`, `Hours`, `Total`, `Status`) VALUES
(0, 2, 7, '2023-22-12 23:59', 2, 3400, 0),
(1, 2, 0, '2023-22-12 23:59', 7, 7000, 0),
(2, 2, 2, '2023-23-12 00:00', 3, 3600, 0),
(3, 2, 3, '2023-23-12 00:16', 1, 1300, 0),
(4, 2, 5, '2023-23-12 00:16', 2, 3000, 0),
(5, 2, 5, '2023-23-12 00:16', 5, 7500, 0),
(6, 2, 9, '2023-23-12 00:16', 8, 14400, 0),
(7, 2, 7, '2023-23-12 00:16', 7, 11900, 0),
(8, 2, 5, '2023-23-12 00:16', 1, 1500, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `Email` text NOT NULL,
  `PhoneNumber` text NOT NULL,
  `Password` text NOT NULL,
  `Type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `Password`, `Type`) VALUES
(0, 'Admin', '0', 'admin', '0000', '0000', 1),
(1, 'Admin', '2', 'admin2', '222222', '1234', 1),
(2, 'Client', '1', 'client', '111111', '1111', 0),
(3, 'Client', '2', 'client2@crs.com', '222222', '2222', 0),
(4, 'Client', '3', 'client3@crs.com', '333333', '3333', 0),
(5, 'Client', '4', 'client4@crs.com', '444444', '4444', 0),
(6, 'Client', '5', 'client5@crs.com', '555555', '5555', 0),
(7, 'Client', '6', 'client6@crs.com', '666666', '6666', 0),
(8, 'Client', '7', 'client7@crs.com', '777777', '7777', 0),
(9, 'Client', '8', 'client8@crs.com', '888888', '8888', 0),
(10, 'Client', '9', 'client9@crs.com', '999999', '9999', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
