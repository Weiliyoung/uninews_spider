/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80400
 Source Host           : localhost:3306
 Source Schema         : uninews

 Target Server Type    : MySQL
 Target Server Version : 80400
 File Encoding         : 65001

 Date: 24/05/2024 15:54:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `university_id` int(0) NULL DEFAULT NULL COMMENT '大学ID',
  `title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '文章题目',
  `source` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '文章来源',
  `date` date NULL DEFAULT NULL COMMENT '文章发表时间',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '文章内容',
  `url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '文章URL',
  `picture` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '文章当中的照片',
  `attachment_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '附件URL',
  `crawl_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '爬取时间',
  `update_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_article_university`(`university_id`) USING BTREE,
  CONSTRAINT `fk_article_university` FOREIGN KEY (`university_id`) REFERENCES `university` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for city
-- ----------------------------
DROP TABLE IF EXISTS `city`;
CREATE TABLE `city`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '城市ID',
  `city_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '城市名字',
  `create_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `update_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for university
-- ----------------------------
DROP TABLE IF EXISTS `university`;
CREATE TABLE `university`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '学校ID',
  `city_id` int(0) NULL DEFAULT NULL COMMENT '城市ID',
  `university_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '学校名字',
  `university_website_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '学校官方网站url',
  `university_start_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '学校研究生招生网站url',
  `create_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `update_time` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_university_city`(`city_id`) USING BTREE,
  CONSTRAINT `fk_university_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
