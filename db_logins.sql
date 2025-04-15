CREATE DATABASE db_for_test_app;
USE db_for_test_app;



CREATE TABLE [Users]
(
    [ID] INT IDENTITY,
	[Time_log] VARCHAR(50),
    [login] VARCHAR(50) NOT NULL UNIQUE,
    [Password] VARCHAR(255) NOT NULL,
);



SELECT * FROM [Users]
DROP TABLE [Users]