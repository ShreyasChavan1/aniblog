-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2024 at 04:17 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `anime_blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `name` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `message` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`name`, `email`, `message`, `date`) VALUES
('shreyas chavan', 'chavanshreyas120@gma', 'hello shreyas chavan i really like your posts please keep on posting them and can you please give me dashboard password so can i can add by own blog also pretty please ?', '2024-01-01 22:47:21'),
('shreyas chavan', 'idiotshark201@gmail.', 'hello i like your content very much please don\'t stop making such blogs', '2024-01-02 19:56:29'),
('shreyas chavan', 'idiotshark201@gmail.', 'hello i like your content very much please don\'t stop making such blogs', '2024-01-02 19:57:21'),
('shreyas chavan', 'idiotshark201@gmail.', 'hello i like your content very much please don\'t stop making such blogs', '2024-01-02 19:58:46'),
('and mand', 'andmand@gmail.com', 'and mand sand ', '2024-01-02 20:33:12'),
('smit potkar', 'nerd@gmail.com', 'hello world', '2024-01-02 20:39:30'),
('dfdd', 'dfdfd@gmail.com', 'dfdfdfdfdf', '2024-01-07 11:00:17');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `srno` int(5) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` text NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `category` varchar(20) NOT NULL,
  `img` varchar(50) NOT NULL,
  `author` varchar(20) NOT NULL,
  `author_img` varchar(20) NOT NULL,
  `author_desc` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`srno`, `title`, `tagline`, `slug`, `content`, `date`, `category`, `img`, `author`, `author_img`, `author_desc`) VALUES
(1, 'first post', 'pahila post', 'hello-post', 'hello this is first post hope you enjoy this', '2024-01-01 19:46:53', 'shounen', 'image.jpg', 'shreyas', 'author.jpg', 'hello this is shreyas'),
(5, 'rising of shield hero', 'downfall on second season ', 'isekai-blog', 'pretty obvious but everyone noticed the downfall of the once best known isekai anime \'tate no yuisha nariagiri\' aka rising of shield hero , but in the third season they have somewhat managed to maintain what they have little bit of fanbase left out of love for their beloved \'naofumi sama\'.', '2024-01-03 20:09:59', 'isekai', 'rising of shield hero.jpg', 'smit', 'author.jpg', 'hello this is smit'),
(6, 'romcom', 'love life of an introvert', 'love-anime', 'i think my teen romantic comedy snafu is the best romcom anime. it has all the emotions a romcom anime must have', '2024-01-03 20:22:44', 'love', 'oregairu.jpg', 'vighnesh', 'author.jpg', 'hello this is vighnesh'),
(7, 'naruto', 'shinobi-post', 'one of big three', 'hey ya this is an average weeb here who watched naruto as his first anime well i watched it i felt like there could be no one who can make anime series like this one , but after i watched attack on titan as my second anime my mind changed there', '2024-01-05 19:18:34', 'shounen', 'naruto.jpg', 'sahil', 'author.jpg', 'hello this is sahil');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `srno` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
