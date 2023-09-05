--
-- Create database
--

DROP DATABASE IF EXISTS culinary_recipes_mysql;
CREATE DATABASE culinary_recipes_mysql;
USE culinary_recipes_mysql;

--
-- Table structure for table `job_title`
--

CREATE TABLE `job_title` (
  `id` bigint NOT NULL,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` bigint NOT NULL,
  `id_encoded` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `sex` enum('Male','Female') NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `birthdate` date NOT NULL,
  `id_job_title` bigint NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `user_fk_1` FOREIGN KEY (`id_job_title`) REFERENCES `job_title` (`id`)
);

--
-- Table structure for table `recipe`
--

CREATE TABLE `recipe` (
  `id` bigint NOT NULL,
  `id_user` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `minutes` int NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `steps` json DEFAULT NULL,
  `nutrition` json DEFAULT NULL,
  `calorie_level` int NOT NULL,
  `submitted_at` datetime NOT NULL,
  `last_updated` datetime NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `recipe_fk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`),
  CONSTRAINT `recipe_chk_1` CHECK (0<=`calorie_level` AND `calorie_level`<=2)
);

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `id` bigint NOT NULL,
  `id_user` bigint NOT NULL,
  `id_recipe` bigint NOT NULL,
  `valuation` int NOT NULL,
  `review` varchar(255) DEFAULT NULL,
  `submitted_date` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`id_user`,`id_recipe`),
  CONSTRAINT `rating_fk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`),
  CONSTRAINT `rating_fk_2` FOREIGN KEY (`id_recipe`) REFERENCES `recipe` (`id`),
  CONSTRAINT `rating_chk_1` CHECK (0<=`valuation` AND `valuation`<=5)
);

--
-- Table structure for table `ingredient`
--

CREATE TABLE `ingredient` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `recipe_ingredient`
--

CREATE TABLE `recipe_ingredient` (
  `id_recipe` bigint NOT NULL,
  `id_ingredient` bigint NOT NULL,
  PRIMARY KEY (`id_recipe`,`id_ingredient`),
  CONSTRAINT `recipe_ingredient_fk_1` FOREIGN KEY (`id_recipe`) REFERENCES `recipe` (`id`),
  CONSTRAINT `recipe_ingredient_fk_2` FOREIGN KEY (`id_ingredient`) REFERENCES `ingredient` (`id`)
);

--
-- Table structure for table `tag`
--

CREATE TABLE `tag` (
  `id` bigint NOT NULL,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `recipe_tag`
--

CREATE TABLE `recipe_tag` (
  `id_recipe` bigint NOT NULL,
  `id_tag` bigint NOT NULL,
  PRIMARY KEY (`id_recipe`,`id_tag`),
  CONSTRAINT `recipe_tag_fk_1` FOREIGN KEY (`id_recipe`) REFERENCES `recipe` (`id`),
  CONSTRAINT `recipe_tag_fk_2` FOREIGN KEY (`id_tag`) REFERENCES `tag` (`id`)
);
