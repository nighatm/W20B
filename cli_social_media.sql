-- cli_social_media.exploits definition

CREATE TABLE `exploits` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `content` varchar(200) DEFAULT NULL,
  `user_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exploits_FK` (`user_id`),
  CONSTRAINT `exploits_FK` FOREIGN KEY (`user_id`) REFERENCES `hackers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- cli_social_media.hackers definition

CREATE TABLE `hackers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;