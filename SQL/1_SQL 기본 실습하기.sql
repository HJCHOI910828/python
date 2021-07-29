# 날짜 : 2021/07/26
# 이름 : 임진슬
# 내용 : SQL 기본 실습하기

# 실습하기 1-1
CREATE DATABASE `TestDB`;
DROP DATABASE `TestDB`;

# 실습하기 1-2
CREATE TABLE `USER1`(
	`uid` VARCHAR(10),
	`name` VARCHAR(10),
	`hip` CHAR(13),
	`age` INT
	);

DROP TABLE `USER1`;

# 실습하기 1-3
INSERT INTO `USER1` VALUES ('A101', '김유신', '010-1234-1111', 25);
INSERT INTO `USER1` VALUES ('A102', '김춘추', '010-1234-2222', 23);
INSERT INTO `USER1` VALUES ('A103', '장보고', '010-1234-3333', 32);
INSERT INTO `USER1` (`age`, `name`, `uid`, `hip`) 
			VALUES(45, '강감찬', 'A104', '010-1234-4444');
INSERT INTO `USER1` SET 
	`name`='이순신', 
	`age`=51, 
	`hip`='010-1234-5555', 
	`uid`='A105';