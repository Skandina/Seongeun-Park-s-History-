CREATE DATABASE roytuts;
use roytuts;

CREATE TABLE `user`(
	`id` int unsigned NOT NULL AUTO_INCREMENT,
	`name` varchar(50) NOT NULL,
	`age` int unsigned NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert into `user`(`id`,`name`,`age`) values
(1,'david',35),
(2,'anna',24);
