CREATE DATABASE db_for_test_app;
USE db_for_test_app;



CREATE TABLE [Users]
(
    [ID] INT IDENTITY,
	[Time_log] VARCHAR(50),
    [login] VARCHAR(50) NOT NULL UNIQUE,
    [Password] VARCHAR(255) NOT NULL,
);


CREATE TABLE [Questions_for_100]
(
    [ID] INT IDENTITY,
	[Text_of_Question] VARCHAR(255),
    [first_ansver] VARCHAR(255) NOT NULL ,
    [second_ansver] VARCHAR(255) NOT NULL,
	[fourth_ansver] VARCHAR(255) NOT NULL,
	[fifth_ansver] VARCHAR(255) NOT NULL,
	[right_ansver] VARCHAR(255) NOT NULL
);

CREATE TABLE [Questions_for_200]
(
    [ID] INT IDENTITY,
	[Text_of_Question] VARCHAR(255),
    [first_ansver] VARCHAR(255) NOT NULL ,
    [second_ansver] VARCHAR(255) NOT NULL,
	[fourth_ansver] VARCHAR(255) NOT NULL,
	[fifth_ansver] VARCHAR(255) NOT NULL,
	[right_ansver] VARCHAR(255) NOT NULL
);

CREATE TABLE [Questions_for_300]
(
    [ID] INT IDENTITY,
	[Text_of_Question] VARCHAR(255),
    [first_ansver] VARCHAR(255) NOT NULL ,
    [second_ansver] VARCHAR(255) NOT NULL,
	[fourth_ansver] VARCHAR(255) NOT NULL,
	[fifth_ansver] VARCHAR(255) NOT NULL,
	[right_ansver] VARCHAR(255) NOT NULL
);

CREATE TABLE [Questions_for_400]
(
    [ID] INT IDENTITY,
	[Text_of_Question] VARCHAR(255),
    [first_ansver] VARCHAR(255) NOT NULL ,
    [second_ansver] VARCHAR(255) NOT NULL,
	[fourth_ansver] VARCHAR(255) NOT NULL,
	[fifth_ansver] VARCHAR(255) NOT NULL,
	[right_ansver] VARCHAR(255) NOT NULL
);

CREATE TABLE [Questions_for_500]
(
    [ID] INT IDENTITY,
	[Text_of_Question] VARCHAR(255),
    [first_ansver] VARCHAR(255) NOT NULL ,
    [second_ansver] VARCHAR(255) NOT NULL,
	[fourth_ansver] VARCHAR(255) NOT NULL,
	[fifth_ansver] VARCHAR(255) NOT NULL,
	[right_ansver] VARCHAR(255) NOT NULL
);

INSERT INTO [Questions_for_100] ([Text_of_Question], [first_ansver], [second_ansver], [fourth_ansver], [fifth_ansver], [right_ansver]) VALUES
('Что обозначает код 200?', 'Успешный запрос', 'Ошибка сервера', 'Не авторизован', 'Страница не найдена', 'Успешный запрос'),
('Что обозначает код 201?', 'Ресурс создан', 'Ошибка клиента', 'Ресурс удалён', 'Неверный токен', 'Ресурс создан'),
('Что обозначает код 202?', 'Запрос принят, но ещё не обработан', 'Не найдено', 'Ошибка сервера', 'Конфликт данных', 'Запрос принят, но ещё не обработан'),
('Что обозначает код 204?', 'Нет содержимого', 'Ошибка базы данных', 'Переадресация', 'Доступ запрещён', 'Нет содержимого'),
('Что означает код 203?', 'Неполная информация от сервера', 'Создано', 'Редирект', 'Сервер не работает', 'Неполная информация от сервера');


INSERT INTO [Questions_for_200] ([Text_of_Question], [first_ansver], [second_ansver], [fourth_ansver], [fifth_ansver], [right_ansver]) VALUES
('Что обозначает код 400?', 'Неверный запрос', 'Не найдено', 'Ошибка сервера', 'Файл загружен', 'Неверный запрос'),
('Что обозначает код 401?', 'Не авторизован', 'Редирект', 'Ошибка базы данных', 'Переадресация', 'Не авторизован'),
('Что обозначает код 403?', 'Запрещено', 'Файл не найден', 'Неверный токен', 'Сервер выключен', 'Запрещено'),
('Что обозначает код 404?', 'Создание прошло успешно', 'Страница не найдена', 'Перенаправление', 'Нету правильного ответа', 'Страница не найдена'),
('Что означает код 405?', 'Метод не разрешён', 'Файл перемещён', 'Доступ разрешён', 'Ресурс создан', 'Метод не разрешён');


INSERT INTO [Questions_for_300] ([Text_of_Question], [first_ansver], [second_ansver], [fourth_ansver], [fifth_ansver], [right_ansver]) VALUES
('Что означает код 300?', 'Множественный выбор', 'Ошибка клиента', 'Редирект', 'Сервер не найден', 'Множественный выбор'),
('Что означает код 301?', 'Ресурс перемещён навсегда', 'Удалённый доступ', 'Не найдено', 'Требуется авторизация', 'Ресурс перемещён навсегда'),
('Что означает код 302?', 'Временное перенаправление', 'Ошибка авторизации', 'Файл повреждён', 'Перенос завершён', 'Временное перенаправление'),
('Что означает код 303?', 'Перейти по другому URI', 'Пользователь не найден', 'Файл обновлён', 'Неизвестная ошибка', 'Перейти по другому URI'),
('Что означает код 304?', 'Ресурс не изменялся', 'Неверная сессия', 'Редирект', 'Сбой подключения', 'Ресурс не изменялся');

INSERT INTO [Questions_for_400] ([Text_of_Question], [first_ansver], [second_ansver], [fourth_ansver], [fifth_ansver], [right_ansver]) VALUES
('Что означает код 407?', 'Требуется аутентификация прокси', 'Неверный логин', 'Файл не найден', 'Сервер выключен', 'Требуется аутентификация прокси'),
('Что означает код 408?', 'Истекло время ожидания запроса', 'Редирект', 'Неверный заголовок', 'Сбой сервера', 'Истекло время ожидания запроса'),
('Что означает код 409?', 'Конфликт запроса', 'Создан новый ресурс', 'Сервер перегружен', 'Неверный путь', 'Конфликт запроса'),
('Что означает код 410?', 'Ресурс удалён', 'Неавторизованный доступ', 'Файл повреждён', 'Неправильный метод', 'Ресурс удалён'),
('Что означает код 429?', 'Слишком много запросов', 'Доступ разрешён', 'Успешный ответ', 'Редирект навсегда', 'Слишком много запросов');

INSERT INTO [Questions_for_500] ([Text_of_Question], [first_ansver], [second_ansver], [fourth_ansver], [fifth_ansver], [right_ansver]) VALUES
('Что означает код 500?', 'Клиент не авторизован', 'Сервер не отвечает', 'Внутренняя ошибка сервера', 'Запрос выполнен успешно', 'Внутренняя ошибка сервера'),
('Что означает код 501?', 'Метод не реализован', 'Ресурс обновлён', 'Код неверен', 'Редирект', 'Метод не реализован'),
('Что означает код 502?', 'Плохой шлюз', 'Нет доступа к клиенту', 'Обновление успешно', 'Успешный ответ', 'Плохой шлюз'),
('Что означает код 503?', 'Служба недоступна', 'Клиент отключён', 'Ресурс доступен', 'Метод устарел', 'Служба недоступна'),
('Что означает код 504?', 'Шлюз не отвечает', 'Ресурс найден', 'Файл не существует', 'Неправильная сессия', 'Шлюз не отвечает');

SELECT * FROM [Questions_for_100]
SELECT * FROM [Questions_for_200]
SELECT * FROM [Questions_for_300]
SELECT * FROM [Questions_for_400]
SELECT * FROM [Questions_for_500]

SELECT * FROM [Users]
DROP TABLE [Users]