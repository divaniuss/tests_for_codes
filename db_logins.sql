CREATE DATABASE db_for_test_app;
USE db_for_test_app;

CREATE TABLE [Users]
(
    [ID] INT IDENTITY,
	[Time_log] VARCHAR(50),
	[Name] VARCHAR(50) NOT NULL,
    [login] VARCHAR(50) NOT NULL UNIQUE,
    [Password] VARCHAR(255) NOT NULL,
);


CREATE TABLE [Questions] (
    [ID] INT IDENTITY PRIMARY KEY,
    [Level] INT NOT NULL,
    [Text] VARCHAR(255) NOT NULL
);


CREATE TABLE [Answers] (
    [ID] INT IDENTITY PRIMARY KEY,
    [QuestionID] INT FOREIGN KEY REFERENCES Questions(ID),
    [Text] VARCHAR(255) NOT NULL,
    [isCorrect] BIT DEFAULT 0 NOT NULL
);


CREATE TABLE [Logs] (
    [ID] INT IDENTITY PRIMARY KEY,
    [User] VARCHAR(255) NOT NULL,
    [Test] VARCHAR(255) NOT NULL,
    [Answers] VARCHAR(50) NOT NULL,
	[Time_log] VARCHAR(255),
);

SELECT * FROM [Answers]
SELECT * FROM [Questions]
SELECT * FROM [Users]
SELECT * FROM [Logs]

DROP TABLE [Logs]
DROP TABLE [Answers]
DROP TABLE [Questions]
DROP TABLE [Users]