BEGIN TRANSACTION;
CREATE TABLE "Subjects" (
	`subjectId`	integer NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	text,
	`professorId`	text,
	FOREIGN KEY(`professorId`) REFERENCES `Professors`(`professorId`)
);
INSERT INTO `Subjects` VALUES (1,'Физкультура','0');
INSERT INTO `Subjects` VALUES (2,'Матанализ (Л)','1');
INSERT INTO `Subjects` VALUES (3,'ТФКП (Л)','2');
INSERT INTO `Subjects` VALUES (4,'Матлогика (Л)','3');
INSERT INTO `Subjects` VALUES (5,'Методы программирования (Л)','4');
INSERT INTO `Subjects` VALUES (6,'Немецкий язык','5');
INSERT INTO `Subjects` VALUES (7,'Методы программирования (П)','4');
INSERT INTO `Subjects` VALUES (8,'ТФКП (П)','6');
INSERT INTO `Subjects` VALUES (9,'Прикладная алгебра (Л)','7');
INSERT INTO `Subjects` VALUES (10,'Английский язык','8');
INSERT INTO `Subjects` VALUES (11,'Методы программирования (П)','9');
INSERT INTO `Subjects` VALUES (12,'Дискретная математика (Л)','10');
INSERT INTO `Subjects` VALUES (13,'Дискретная математика (П)','10');
INSERT INTO `Subjects` VALUES (14,'Прикладная алгебра (П)','7');
INSERT INTO `Subjects` VALUES (15,'Матанализ (П)','1');
INSERT INTO `Subjects` VALUES (16,'ОИБ','11');
INSERT INTO `Subjects` VALUES (17,'Матлогика (П)','3');
CREATE TABLE `StartTimes` (
	`lessonNumber`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`startTime`	TEXT,
	`endTime`	TEXT
);
INSERT INTO `StartTimes` VALUES (1,'08:30','10:00');
INSERT INTO `StartTimes` VALUES (2,'10:10','11:40');
INSERT INTO `StartTimes` VALUES (3,'12:00','13:30');
INSERT INTO `StartTimes` VALUES (4,'13:40','15:10');
INSERT INTO `StartTimes` VALUES (5,'15:20','16:50');
CREATE TABLE "Schedule" (
	`day`	INTEGER NOT NULL,
	`lessonNumber`	INTEGER,
	`subjectId`	INTEGER,
	`room`	INTEGER,
	FOREIGN KEY(`lessonNumber`) REFERENCES `StartTimes`(`lessonNumber`),
	FOREIGN KEY(`subjectId`) REFERENCES `Subjects`(`subjectId`)
);
INSERT INTO `Schedule` VALUES (1,3,1,NULL);
INSERT INTO `Schedule` VALUES (1,4,2,205);
INSERT INTO `Schedule` VALUES (1,5,3,205);
INSERT INTO `Schedule` VALUES (2,1,4,209);
INSERT INTO `Schedule` VALUES (2,2,17,209);
INSERT INTO `Schedule` VALUES (2,3,5,215);
INSERT INTO `Schedule` VALUES (2,4,6,232);
INSERT INTO `Schedule` VALUES (2,4,7,101);
INSERT INTO `Schedule` VALUES (3,1,8,231);
INSERT INTO `Schedule` VALUES (3,2,9,231);
INSERT INTO `Schedule` VALUES (3,3,10,232);
INSERT INTO `Schedule` VALUES (3,4,11,214);
INSERT INTO `Schedule` VALUES (4,2,12,215);
INSERT INTO `Schedule` VALUES (4,3,13,215);
INSERT INTO `Schedule` VALUES (4,4,14,213);
INSERT INTO `Schedule` VALUES (5,3,1,NULL);
INSERT INTO `Schedule` VALUES (5,4,15,209);
INSERT INTO `Schedule` VALUES (5,5,16,215);
INSERT INTO `Schedule` VALUES (6,2,4,209);
INSERT INTO `Schedule` VALUES (6,3,17,209);
CREATE TABLE "Professors" (
	`professorId`	integer PRIMARY KEY AUTOINCREMENT,
	`professorname`	text
);
INSERT INTO `Professors` VALUES (0,NULL);
INSERT INTO `Professors` VALUES (1,'Алешникова М.В.');
INSERT INTO `Professors` VALUES (2,'Шевченко Ю.И.');
INSERT INTO `Professors` VALUES (3,'Касаткина Ю.С.');
INSERT INTO `Professors` VALUES (4,'Мацула П.В.');
INSERT INTO `Professors` VALUES (5,'Свиридова Л.И.');
INSERT INTO `Professors` VALUES (6,'Кочина А.С.');
INSERT INTO `Professors` VALUES (7,'Алексеенко Е.С.');
INSERT INTO `Professors` VALUES (8,'Кужулова И.В.');
INSERT INTO `Professors` VALUES (9,'Шарамет А.А.');
INSERT INTO `Professors` VALUES (10,'Корсакова Л.Г.');
INSERT INTO `Professors` VALUES (11,'Полковский О.А.');
COMMIT;
