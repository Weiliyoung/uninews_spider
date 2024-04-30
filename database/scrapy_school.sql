/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80300
 Source Host           : localhost:3306
 Source Schema         : scrapy_school

 Target Server Type    : MySQL
 Target Server Version : 80300
 File Encoding         : 65001

 Date: 30/04/2024 08:37:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `source` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `content` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `url` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `crawl_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of test
-- ----------------------------
BEGIN;
INSERT INTO `test` VALUES (1, '广州华商学院2024年依据台湾地区大学考试学科能力测试成绩招收台湾高中毕业生简章', '文章来源：', '2024-02-02 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1501.htm', '2024-04-29 20:10:41');
INSERT INTO `test` VALUES (2, '学院纵览 | 你好，这里是国际学院！', '文章来源：', '2023-06-07 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1519.htm', '2024-04-29 20:10:46');
INSERT INTO `test` VALUES (3, '2022年国际项目招生简章', '文章来源：', '2022-06-29 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1474.htm', '2024-04-29 20:11:00');
INSERT INTO `test` VALUES (4, '广东省2019年夏季普通高校招生录取工作日程表', '文章来源：', '2019-07-01 00:00:00', '随着2019年高考放榜，广东考生的志愿填报工作也正在进行中。志愿填报结束后，就要进入录取阶段！小编现在就带大家来先了解一下有关高校招生录取的流程，请下载附件。广东省2019年夏季普通高校招生录取安排.doc', 'https://zs.gdhsc.edu.cn/info/1023/1313.htm', '2024-04-29 20:11:48');
INSERT INTO `test` VALUES (5, '广东财经大学华商学院2020年本科插班生招生考试专业课考试大纲', '文章来源：', '2019-12-09 00:00:00', '各位报考本科插班生的同学：       现公布广东财经大学华商学院2020年本科插班生招生考试专业课考试大纲，请根据报考专业下载以下附件中的考试大纲，使用PDF软件打开。      欢迎报考广东财经大学华商学院！华商学院欢迎你们！', 'https://zs.gdhsc.edu.cn/info/1023/1299.htm', '2024-04-29 20:12:09');
INSERT INTO `test` VALUES (6, '广东省招生委员会办公室关于推迟广东省2020年普通高考英语听说考试和本科插班生考试时间的紧急通知', '文章来源：', '2020-02-07 00:00:00', '各地级以上市招生办公室（考试中心），各本科插班生招生院校和考点：为贯彻落实国家和我省对新型冠状病毒感染的肺炎疫情防控有关工作的部署和要求，切实保障广大考生和考试工作人员生命安全和身体健康，经研究决定，推迟原定于3月7-8日举行的普通高考英语听说考试和本科插班生考试（含三二分段专升本转段考试）。具体时间安排视疫情控制情况另行通知。请各市、各有关高校迅速将以上内容通知本辖区各有关中学和考生。 广东省招生委员会办公室 2020年2月6日', 'https://zs.gdhsc.edu.cn/info/1023/1300.htm', '2024-04-29 20:12:11');
INSERT INTO `test` VALUES (7, '广东省2020年夏季普通高校招生录取工作日程表', '文章来源：广东省教育考试院', '2020-08-02 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1307.htm', '2024-04-29 20:12:31');
INSERT INTO `test` VALUES (8, '2021年国际项目招生简章', '文章来源：', '2021-06-25 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1258.htm', '2024-04-29 20:12:35');
INSERT INTO `test` VALUES (9, '广东财经大学华商学院“一带一路”来华留学生培训项目', '文章来源：', '2019-04-04 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1324.htm', '2024-04-29 20:12:47');
INSERT INTO `test` VALUES (10, '2019年高校联合招收华侨港澳台学生入学考试今天起打印准考证', '文章来源：', '2019-05-14 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1320.htm', '2024-04-29 20:12:53');
INSERT INTO `test` VALUES (11, '广东财经大学华商学院2019年新生入学须知', '文章来源：', '2019-07-22 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1296.htm', '2024-04-29 20:13:21');
INSERT INTO `test` VALUES (12, '2018年省外本科计划表：新疆、云南、海南、广西、湖南、河南江西和福建等8省', '文章来源：', '2018-06-06 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1251.htm', '2024-04-29 20:13:29');
INSERT INTO `test` VALUES (13, '华商学院2018年招生宣传圆满结束，港澳联招录取工作今天开始', '文章来源：', '2018-07-03 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1254.htm', '2024-04-29 20:13:36');
INSERT INTO `test` VALUES (14, '广东省2019年普通高校本科插班生体检表', '文章来源：', '2018-11-26 00:00:00', '各位报考2019年本科插班生的同学：    请下载《广东省2019年高等学校本科插班生招生体格检查表》，用一张A4纸正反面打印，填写个人信息，在体检表上张贴1张小1寸半身脱帽证件照（背景颜色无特殊要求），在规定时间内（体检表有效期：2018年12月9日-2019年1月9日）自行前往二级甲等（含）以上医院或相应的医疗单位进行体检，报名确认时（2019年1月7-9日）须向我校提交体检结果。体检表下载：', 'https://zs.gdhsc.edu.cn/info/1023/1331.htm', '2024-04-29 20:13:50');
INSERT INTO `test` VALUES (15, '广东财经大学华商学院2019年本科插班生招生考试专业课考试大纲', '文章来源：', '2018-11-30 00:00:00', '各位报考本科插班生的同学：     现公布广东财经大学华商学院2019年本科插班生招生考试专业课考试大纲，请根据报考专业下载以下附件中的考试大纲，使用PDF软件打开。     欢迎报考广东财经大学华商学院！华商学院欢迎你们！', 'https://zs.gdhsc.edu.cn/info/1023/1330.htm', '2024-04-29 20:13:53');
INSERT INTO `test` VALUES (16, '广东财经大学华商学院招收华侨和港澳台学生招生简章', '文章来源：', '2019-04-04 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1325.htm', '2024-04-29 20:14:07');
INSERT INTO `test` VALUES (17, '广东财经大学华商学院2018年本科插班生招生问答', '文章来源：', '2017-12-28 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1238.htm', '2024-04-29 20:14:20');
INSERT INTO `test` VALUES (18, '【录取喜讯】华商学院圆满完成2018年本科插班生录取工作，生源质量创新高！', '文章来源：', '2018-04-26 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1245.htm', '2024-04-29 20:14:37');
INSERT INTO `test` VALUES (19, '广东财经大学华商学院2018年招收香港和澳门地区学生招生简章', '文章来源：港澳台侨招生办公室', '2018-05-16 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1246.htm', '2024-04-29 20:14:40');
INSERT INTO `test` VALUES (20, '广东财经大学华商学院外国留学生招生简章', '文章来源：外国留学生招生办', '2018-05-25 00:00:00', '', 'https://zs.gdhsc.edu.cn/info/1023/1247.htm', '2024-04-29 20:14:42');
INSERT INTO `test` VALUES (21, '2018年在粤本科招生计划表', '文章来源：', '2018-06-06 00:00:00', '‍', 'https://zs.gdhsc.edu.cn/info/1023/1250.htm', '2024-04-29 20:14:43');
INSERT INTO `test` VALUES (22, '广东财经大学华商学院2018年本科插班生招生考试专业课考试大纲', '文章来源：招生办公室', '2017-11-30 00:00:00', '各位报考本科插班生的同学：     现公布广东财经大学华商学院2018年本科插班生招生考试专业课考试大纲，请根据报考专业下载以下附件中的考试大纲，使用PDF软件打开。     欢迎报考广东财经大学华商学院！华商学院欢迎你们！', 'https://zs.gdhsc.edu.cn/info/1023/1234.htm', '2024-04-29 20:14:45');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
