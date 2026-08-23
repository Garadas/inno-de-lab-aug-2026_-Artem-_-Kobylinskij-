CREATE TABLE Departments ( -- создание таблицы с параметрами
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
Location VARCHAR(50)
); 

ALTER TABLE employees 
ADD COLUMN Email VARCHAR(100); --добавление поля Email

UPDATE employees
SET Email =  employeeid || 'stud@mail.ru'; --заполнени полей на основе уникального поля


ALTER TABLE employees
ADD CONSTRAINT UQ_Email UNIQUE (Email); --добавление ограничения UNIQUE

ALTER TABLE Departments
RENAME Location TO OfficeLocation ; --переименование поля

