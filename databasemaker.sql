BEGIN TRANSACTION;
CREATE TABLE Subjects (
	subjectId integer PRIMARY KEY AUTOINCREMENT,
	name text,
	professorId text,
	FOREIGN KEY(professorId) REFERENCES Professors(professorId)
);

CREATE TABLE Professors (
	professorId integer PRIMARY KEY AUTOINCREMENT,
	professorname text
);

CREATE TABLE `Monday` (
	`starttime`	TEXT,
	`subject`	TEXT,
	`room`	INTEGER,
	`professorname`	TEXT
);

COMMIT;
