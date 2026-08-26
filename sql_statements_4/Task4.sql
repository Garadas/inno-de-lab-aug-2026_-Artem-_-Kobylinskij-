UPDATE employees 
SET salary = salary * 1.1
WHERE department = 'HR'; --увеличение для всех на 10%

UPDATE employees 
SET department = 'Senior IT'
WHERE salary > 70000.00; -- изменение department для всех с salary > 70к

DELETE FROM employees --удаление сотрудников не подходящих для Where
WHERE NOT EXISTS (
SELECT * FROM employeeprojects
WHERE employeeprojects.employeeid = employees.employeeid 
);

DO $$ --выполнение функции без названия
DECLARE
    proj_id INT; -- переменная для хранения созданного id проекта
BEGIN

INSERT INTO projects (ProjectName, Budget, StartDate, EndDate) VALUES 
('project New Dawn',3456,'2023-01-15', '2023-06-30')
RETURNING projectid INTO proj_id;-- создали проект и записали id

INSERT INTO employeeprojects (EmployeeID, ProjectID, HoursWorked) VALUES
(1,proj_id,40),
(2,proj_id,50); -- на id проекта записали 2 сотрудников

END;
$$;



