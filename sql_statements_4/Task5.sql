CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    p_employeeid INT,
    p_salary NUMERIC --функция принимает параметры 
) 
RETURNS NUMERIC --возвращает параметр
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN p_salary * 0.1; --10% от salary
END;
$$;


SELECT *,CalculateAnnualBonus(employeeid, salary) AS AnnualBonus
FROM employees; --выводим всё + поле с пасчетом бонуса

CREATE OR REPLACE VIEW IT_Department_View AS --создание представления
SELECT employeeid, firstname, lastname, salary
FROM employees
WHERE department = 'IT';

SELECT * FROM IT_Department_View; --демострация представления