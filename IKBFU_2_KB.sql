BEGIN TRANSACTION;
CREATE TABLE Subjects (
	subjectId integer PRIMARY KEY AUTOINCREMENT,
	name text,
	professorId text
);

CREATE TABLE Professors (
	professorId integer PRIMARY KEY AUTOINCREMENT,
	professorname text,
	subjectId integer
);

CREATE TABLE `Monday` (
	`starttime`	TEXT,
	`subject`	TEXT,
	`room`	INTEGER,
	`professorname`	TEXT
);
INSERT INTO `Monday` VALUES ('13:40','Calculus',213,'Aleshnikova');
COMMIT;
