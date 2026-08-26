INSERT INTO employees (FirstName, LastName, Department, Salary) VALUES
('Artem', 'Kobylinskij', 'Finance', 45000.00),
('Mark', 'Twen', 'HR', 50000.00); --добавил 2 сотрудников

SELECT * FROM employees ; --вывел всех сотрудников

SELECT firstname, lastname FROM employees
WHERE department = 'IT';  --вывел только из отдела 'IT'

UPDATE employees
SET salary = 65000.00
WHERE firstname = 'Alice' and lastname = 'Smith'; --поменял Salary для всех с ФИ Alice Smith

DELETE FROM employees 
WHERE firstname = 'Eve' and lastname = 'Davis'; --удалил всех с ФИ Eve Davis

SELECT * FROM employees ; --вывел для проверки