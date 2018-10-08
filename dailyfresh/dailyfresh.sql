/*
Navicat MySQL Data Transfer

Source Server         : 5.0user
Source Server Version : 50090
Source Host           : localhost:3306
Source Database       : dailyfresh

Target Server Type    : MYSQL
Target Server Version : 50090
File Encoding         : 65001

Date: 2018-09-30 12:37:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add user info', '7', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('20', 'Can change user info', '7', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete user info', '7', 'delete_userinfo');
INSERT INTO `auth_permission` VALUES ('22', 'Can add type info', '8', 'add_typeinfo');
INSERT INTO `auth_permission` VALUES ('23', 'Can change type info', '8', 'change_typeinfo');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete type info', '8', 'delete_typeinfo');
INSERT INTO `auth_permission` VALUES ('25', 'Can add goods info', '9', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change goods info', '9', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete goods info', '9', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can add type info', '10', 'add_typeinfo');
INSERT INTO `auth_permission` VALUES ('29', 'Can change type info', '10', 'change_typeinfo');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete type info', '10', 'delete_typeinfo');
INSERT INTO `auth_permission` VALUES ('31', 'Can add goods info', '11', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can change goods info', '11', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete goods info', '11', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('34', 'Can add cart info', '12', 'add_cartinfo');
INSERT INTO `auth_permission` VALUES ('35', 'Can change cart info', '12', 'change_cartinfo');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete cart info', '12', 'delete_cartinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `password` varchar(128) NOT NULL,
  `last_login` datetime default NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$20000$FFq4qLMByyrX$G2ZndZNqVr8f0XXC3Jr0uPLTMkNNJgW8SP5a0iDNzMQ=', '2018-09-26 02:37:24', '1', 'root', '', '', '12345@qw.com', '1', '1', '2018-09-26 02:04:01');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for df_cart_cartinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_cart_cartinfo`;
CREATE TABLE `df_cart_cartinfo` (
  `id` int(11) NOT NULL auto_increment,
  `count` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`goods_id`),
  KEY `df_cart_cartinfo_6753b66e` (`goods_id`),
  KEY `df_cart_cartinfo_e8701ad4` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_cart_cartinfo
-- ----------------------------
INSERT INTO `df_cart_cartinfo` VALUES ('1', '8', '1', '4');
INSERT INTO `df_cart_cartinfo` VALUES ('2', '3', '3', '4');
INSERT INTO `df_cart_cartinfo` VALUES ('3', '7', '4', '4');
INSERT INTO `df_cart_cartinfo` VALUES ('7', '2', '18', '4');
INSERT INTO `df_cart_cartinfo` VALUES ('67', '2', '21', '4');
INSERT INTO `df_cart_cartinfo` VALUES ('4', '1', '21', '1');
INSERT INTO `df_cart_cartinfo` VALUES ('70', '31', '22', '4');
INSERT INTO `df_cart_cartinfo` VALUES ('71', '1', '41', '4');

-- ----------------------------
-- Table structure for df_goods_goodsinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_goodsinfo`;
CREATE TABLE `df_goods_goodsinfo` (
  `id` int(11) NOT NULL auto_increment,
  `gtitle` varchar(20) NOT NULL,
  `gpic` varchar(100) NOT NULL,
  `gprice` decimal(5,2) NOT NULL,
  `gunit` varchar(20) NOT NULL,
  `gclick` int(11) NOT NULL,
  `gjianjie` varchar(200) NOT NULL,
  `gkucun` int(11) NOT NULL,
  `gcontent` longtext NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  `gtype_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `df_goods_goodsinfo_3204e418` (`gtype_id`)
) ENGINE=MyISAM AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_goodsinfo
-- ----------------------------
INSERT INTO `df_goods_goodsinfo` VALUES ('1', '柠檬', '/static/images/goods/goods001.jpg', '3.90', '3.90/500g', '1', '紫葡萄紫葡萄', '100', '紫葡萄紫葡萄紫葡萄紫葡萄', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('2', '紫葡萄', '/static/images/goods/goods002.jpg', '16.80', '16.80/500g', '2', '葡萄葡萄', '100', '葡萄葡萄葡萄葡萄', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('3', '草莓', '/static/images/goods/goods003.jpg', '16.80', '16.80/500g', '3', '草莓浆果柔软多汁，味美爽口，适合速冻保鲜贮藏。草莓速冻后，可以保持原有的色、香、味，既便于贮藏，又便于外销。', '100', '草莓采摘园位于北京大兴区 庞各庄镇四各庄村 ，每年1月-6月面向北京以及周围城市提供新鲜草莓采摘和精品礼盒装草莓，草莓品种多样丰富，个大香甜。所有草莓均严格按照有机标准培育，不使用任何化肥和农药。草莓在采摘期间免洗可以直接食用。欢迎喜欢草莓的市民前来采摘，也欢迎各大单位选购精品有机草莓礼盒，有机草莓礼盒是亲朋馈赠、福利送礼的最佳选择。 ', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('4', '梨光杏', '/static/images/goods/goods004.jpg', '5.50', '5.50/500g', '4', '梨光杏梨光杏', '100', '梨光杏梨光杏梨光杏梨光杏', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('5', '黄肉桃', '/static/images/goods/goods005.jpg', '10.00', '10.00/500g', '5', '黄肉桃黄肉桃', '100', '黄肉桃黄肉桃黄肉桃黄肉桃', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('6', '西梅', '/static/images/goods/goods006.jpg', '28.80', '28.8/500g', '6', '西梅西梅', '100', '西梅西梅西梅西梅', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('7', '香梨', '/static/images/goods/goods007.jpg', '6.45', '6.45/500g', '9', '香梨香梨', '100', '香梨香梨香梨香梨', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('8', '栗子', '/static/images/goods/goods008.jpg', '9.50', '9.50/500g', '18', '栗子栗子', '100', '栗子栗子栗子栗子', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('9', '香蕉', '/static/images/goods/goods009.jpg', '3.30', '3.30/500g', '45', '香蕉香蕉', '100', '香蕉香蕉香蕉香蕉', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('10', '青苹果', '/static/images/goods/goods010.jpg', '5.00', '5.00/500g', '2', '青苹果青苹果', '100', '青苹果青苹果青苹果青苹果', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('11', '山莓', '/static/images/goods/goods011.jpg', '28.80', '28.8/500g', '3', '山莓山莓', '100', '山莓山莓山莓山莓', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('12', '奇异果', '/static/images/goods/goods012.jpg', '25.80', '25.8/500g', '5', '奇异果奇异果', '100', '奇异果奇异果奇异果奇异果', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('13', '蜜桔', '/static/images/goods/goods013.jpg', '4.80', '4.8/500g', '7', '蜜桔蜜桔', '100', '蜜桔蜜桔蜜桔蜜桔', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('14', '脐橙', '/static/images/goods/goods014.jpg', '3.50', '3.50/500g', '20', '脐橙脐橙', '100', '脐橙脐橙脐橙脐橙', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('15', '椰子', '/static/images/goods/goods015.jpg', '28.80', '28.80/500g', '3', '椰子椰子', '100', '椰子椰子椰子椰子', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('16', '油桃', '/static/images/goods/goods016.jpg', '39.90', '39.90/500g', '6', '油桃油桃', '100', '油桃油桃油桃油桃', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('17', '红提葡萄', '/static/images/goods/goods017.jpg', '26.80', '26.80/500g', '5', '红提葡萄红提葡萄', '100', '红提葡萄红提葡萄红提葡萄红提葡萄', '0', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('18', '青虾', '/static/images/goods/goods018.jpg', '48.00', '48.00/500g', '3', '青虾青虾', '100', '青虾青虾青虾青虾', '0', '2');
INSERT INTO `df_goods_goodsinfo` VALUES ('19', '扇贝', '/static/images/goods/goods019.jpg', '46.00', '46.00/500g', '10', '扇贝扇贝', '100', '扇贝扇贝扇贝扇贝', '0', '2');
INSERT INTO `df_goods_goodsinfo` VALUES ('20', '秋刀鱼', '/static/images/goods/goods020.jpg', '19.00', '19.00/500g', '3', '秋刀鱼秋刀鱼', '100', '秋刀鱼秋刀鱼秋刀鱼秋刀鱼', '0', '2');
INSERT INTO `df_goods_goodsinfo` VALUES ('21', '基围虾', '/static/images/goods/goods021.jpg', '25.00', '25.00/500g', '9', '基围虾基围虾', '100', '基围虾基围虾基围虾基围虾', '0', '2');
INSERT INTO `df_goods_goodsinfo` VALUES ('22', '生蚝', '/static/images/goods/goods022.jpg', '22.00', '22.00/500g', '10', '生蚝生蚝', '100', '生蚝生蚝生蚝生蚝', '0', '2');
INSERT INTO `df_goods_goodsinfo` VALUES ('23', '猪肉', '/static/images/goods/goods023.jpg', '23.00', '23.00/500g', '9', '猪肉猪肉', '100', '猪肉猪肉猪肉猪肉', '0', '3');
INSERT INTO `df_goods_goodsinfo` VALUES ('24', '牛肉', '/static/images/goods/goods024.jpg', '24.00', '24.00/500g', '3', '牛肉牛肉', '100', '牛肉牛肉牛肉牛肉', '0', '3');
INSERT INTO `df_goods_goodsinfo` VALUES ('25', '羊肉', '/static/images/goods/goods025.jpg', '25.00', '25.00/500g', '3', '羊肉羊肉', '100', '羊肉羊肉羊肉羊肉', '0', '3');
INSERT INTO `df_goods_goodsinfo` VALUES ('26', '兔肉', '/static/images/goods/goods026.jpg', '26.00', '26.00/500g', '6', '兔肉兔肉', '100', '兔肉兔肉兔肉兔肉', '0', '3');
INSERT INTO `df_goods_goodsinfo` VALUES ('27', '鸡肉', '/static/images/goods/goods027.jpg', '27.00', '27.00/500g', '10', '鸡肉鸡肉', '100', '鸡肉鸡肉鸡肉鸡肉', '0', '3');
INSERT INTO `df_goods_goodsinfo` VALUES ('28', '土鸡蛋', '/static/images/goods/goods028.jpg', '28.00', '28.00/500g', '15', '土鸡蛋土鸡蛋', '100', '土鸡蛋土鸡蛋土鸡蛋土鸡蛋', '0', '4');
INSERT INTO `df_goods_goodsinfo` VALUES ('29', '鸭蛋', '/static/images/goods/goods029.jpg', '29.00', '29.00/500g', '9', '鸭蛋鸭蛋', '100', '鸭蛋鸭蛋鸭蛋鸭蛋', '0', '4');
INSERT INTO `df_goods_goodsinfo` VALUES ('30', '鹌鹑蛋', '/static/images/goods/goods030.jpg', '30.00', '30.00/500g', '6', '鹌鹑蛋鹌鹑蛋', '100', '鹌鹑蛋鹌鹑蛋鹌鹑蛋鹌鹑蛋', '0', '4');
INSERT INTO `df_goods_goodsinfo` VALUES ('31', '皮蛋', '/static/images/goods/goods031.jpg', '31.00', '31.00/500g', '4', '皮蛋皮蛋', '100', '皮蛋皮蛋皮蛋皮蛋', '0', '4');
INSERT INTO `df_goods_goodsinfo` VALUES ('32', '咸蛋', '/static/images/goods/goods032.jpg', '32.00', '32.00/500g', '7', '咸蛋咸蛋', '100', '咸蛋咸蛋咸蛋咸蛋', '0', '4');
INSERT INTO `df_goods_goodsinfo` VALUES ('33', '生菜', '/static/images/goods/goods033.jpg', '33.00', '33.00/500g', '74', '生菜生菜', '100', '生菜生菜生菜生菜', '0', '5');
INSERT INTO `df_goods_goodsinfo` VALUES ('34', '白菜', '/static/images/goods/goods034.jpg', '34.00', '34.00/500g', '2', '白菜白菜', '100', '白菜白菜白菜白菜', '0', '5');
INSERT INTO `df_goods_goodsinfo` VALUES ('35', '油麦菜', '/static/images/goods/goods035.jpg', '35.00', '35.00/500g', '2', '油麦菜油麦菜', '100', '油麦菜油麦菜油麦菜油麦菜', '0', '5');
INSERT INTO `df_goods_goodsinfo` VALUES ('36', '通心菜', '/static/images/goods/goods036.jpg', '36.00', '36.00/500g', '3', '通心菜通心菜', '100', '通心菜通心菜通心菜通心菜', '0', '5');
INSERT INTO `df_goods_goodsinfo` VALUES ('37', '芥菜', '/static/images/goods/goods037.jpg', '37.00', '37.00/500g', '4', '芥菜芥菜', '100', '芥菜芥菜芥菜芥菜', '0', '5');
INSERT INTO `df_goods_goodsinfo` VALUES ('38', '草莓圣代', '/static/images/goods/goods038.jpg', '38.00', '38.00/500g', '3', '草莓圣代草莓圣代', '100', '草莓圣代草莓圣代草莓圣代草莓圣代', '0', '6');
INSERT INTO `df_goods_goodsinfo` VALUES ('39', '圆筒雪糕', '/static/images/goods/goods039.jpg', '39.00', '39.00/500g', '35', '圆筒雪糕圆筒雪糕', '100', '圆筒雪糕圆筒雪糕圆筒雪糕圆筒雪糕', '0', '6');
INSERT INTO `df_goods_goodsinfo` VALUES ('40', '麦旋风', '/static/images/goods/goods040.jpg', '40.00', '40.00/500g', '1', '麦旋风麦旋风', '100', '麦旋风麦旋风麦旋风麦旋风', '0', '6');
INSERT INTO `df_goods_goodsinfo` VALUES ('41', '雪媚娘', '/static/images/goods/goods041.jpg', '41.00', '41.00/500g', '6', '雪媚娘雪媚娘', '100', '雪媚娘雪媚娘雪媚娘雪媚娘', '0', '6');
INSERT INTO `df_goods_goodsinfo` VALUES ('42', '芭菲', '/static/images/goods/goods042.jpg', '42.00', '42.00/500g', '18', '芭菲芭菲', '100', '芭菲芭菲芭菲芭菲', '0', '6');

-- ----------------------------
-- Table structure for df_goods_typeinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_typeinfo`;
CREATE TABLE `df_goods_typeinfo` (
  `id` int(11) NOT NULL auto_increment,
  `ttitle` varchar(20) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_typeinfo
-- ----------------------------
INSERT INTO `df_goods_typeinfo` VALUES ('1', '新鲜水果', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('2', '海鲜产品', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('3', '猪羊牛肉', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('4', '禽类蛋品', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('5', '新鲜蔬菜', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('6', '速冻食品', '0');

-- ----------------------------
-- Table structure for df_user_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `df_user_userinfo`;
CREATE TABLE `df_user_userinfo` (
  `id` int(11) NOT NULL auto_increment,
  `uname` varchar(20) NOT NULL,
  `upwd` varchar(40) NOT NULL,
  `uemail` varchar(30) NOT NULL,
  `ushou` varchar(30) NOT NULL,
  `uphone` varchar(11) NOT NULL,
  `uaddress` varchar(100) NOT NULL,
  `uyoubian` varchar(6) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_user_userinfo
-- ----------------------------
INSERT INTO `df_user_userinfo` VALUES ('1', 'asdasdasd', '7c222fb2927d828af22f592134e8932480637c0d', '12589', '李开复', '12345678910', '快快减肥你会死的', '邮编');
INSERT INTO `df_user_userinfo` VALUES ('2', 'hesh23333', '7c222fb2927d828af22f592134e8932480637c0d', '1.1@.com', '地址', '12345', '地址', '邮编');
INSERT INTO `df_user_userinfo` VALUES ('4', 'adminadmin', '7c222fb2927d828af22f592134e8932480637c0d', '15986', '李开复', '12345678910', '阿拉山口多久爱死了大街上', '');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) default NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `django_content_type_app_label_4ac2ef2d4987aa0_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'df_user', 'userinfo');
INSERT INTO `django_content_type` VALUES ('10', 'df_goods', 'typeinfo');
INSERT INTO `django_content_type` VALUES ('11', 'df_goods', 'goodsinfo');
INSERT INTO `django_content_type` VALUES ('12', 'df_cart', 'cartinfo');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL auto_increment,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-09-21 01:51:47');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('4', 'contenttypes', '0002_remove_content_type_name', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0002_alter_permission_name_max_length', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0003_alter_user_email_max_length', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0004_alter_user_username_opts', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0005_alter_user_last_login_null', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0006_require_contenttypes_0002', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('10', 'df_user', '0001_initial', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('11', 'sessions', '0001_initial', '2018-09-21 01:51:48');
INSERT INTO `django_migrations` VALUES ('16', 'df_goods', '0001_initial', '2018-09-26 02:32:23');
INSERT INTO `django_migrations` VALUES ('17', 'df_user', '0002_auto_20180921_1438', '2018-09-26 02:32:23');
INSERT INTO `django_migrations` VALUES ('18', 'df_cart', '0001_initial', '2018-09-28 08:41:27');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('j4pqvtujth0p55wgz91bfbs4gazul5ln', 'MWJlMzFkZGU1NDdlY2RkODZiZWRmOGU3ZTYxZGE4ZGU1Njk1MGEyZjp7InVzZXJfaWQiOjEsInVzZXJfbmFtZSI6ImFzZGFzZGFzZCJ9', '2018-10-09 08:45:36');
INSERT INTO `django_session` VALUES ('u8cu7bqul4beqfiw4n2xlga7er5ebblq', 'ZWQwNmMyMTdlODQyYWUxYjI2ZWNmOTNlMDQzNzEyNDBjMzBiZTgyNDp7InVzZXJfaWQiOjQsInVzZXJfbmFtZSI6ImFkbWluYWRtaW4iLCJpc2xvZ2luIjoxfQ==', '2018-10-11 11:15:48');
INSERT INTO `django_session` VALUES ('6pxi88w8w44ekjgqhmhsnz5hdnnopxwy', 'YWY4MmRlYzI5N2IzN2Q3OWYzMjJmYzAzNjczMWJjYzBlZWM4YzRjMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZWQyMGU1YjE0ZTJhODMxZDllZDM4NDQzNTRhYTc2YTZmMGJlYmMwIiwidXNlcl9pZCI6MSwidXNlcl9uYW1lIjoiYXNkYXNkYXNkIn0=', '2018-10-10 03:25:47');
INSERT INTO `django_session` VALUES ('fu3sirj3r78rv11957yen5s0ynohmh1m', 'MGEzNzRmYTNjMzM3NDY4NDJkYjc1ODM1ZTZjYTdlMDZmYzU2MTUzZTp7InVzZXJfaWQiOjQsInVzZXJfbmFtZSI6ImFkbWluYWRtaW4ifQ==', '2018-10-11 12:27:40');
INSERT INTO `django_session` VALUES ('aoy3ty7mcpavc4eflkor1kkqker7cc48', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-12 02:42:44');
INSERT INTO `django_session` VALUES ('wzha0dmftxric1dsxhuc8z9o1wipcgil', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-12 06:49:27');
INSERT INTO `django_session` VALUES ('99pq0k5owjq7e6fegewhx9ysgiae5juk', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-12 07:48:24');
INSERT INTO `django_session` VALUES ('fn2ir5y6fh2ckfqy5lnw5jbnv4d6arqv', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-13 06:34:04');
INSERT INTO `django_session` VALUES ('xhihxiucrk79bp18uzzwa1h98zm1v7u4', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-12 07:59:54');
INSERT INTO `django_session` VALUES ('kryu3beus237esil4dh3jowdbe9snl0x', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-12 08:09:25');
INSERT INTO `django_session` VALUES ('x30bv5yymrggvfok8y5x8v3p2c173gad', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-13 04:22:18');
INSERT INTO `django_session` VALUES ('txjtjqx32fks2kl3h2hqfu90h7c9nqdv', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-12 12:02:10');
INSERT INTO `django_session` VALUES ('pbhsg6lzoamkr3mte45azbd4b3h6l050', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-13 08:14:56');
INSERT INTO `django_session` VALUES ('dux7o9g04pv4r95garwth4wv3yu684pc', 'ZmY1NmJmMGZlNDc3ZjdjYzJjOGJjY2JlNjFlNGUwNjk3MTg3OTViMTp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhZG1pbmFkbWluIiwiaXNsb2dpbiI6MX0=', '2018-10-14 02:30:58');
