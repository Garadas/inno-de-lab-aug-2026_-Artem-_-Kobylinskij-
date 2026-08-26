CREATE USER hr_user WITH PASSWORD 'hr_user123';

CREATE ROLE	employees_user;
GRANT SELECT ON employees TO employees_user;

GRANT employees_user TO hr_user;

GRANT INSERT, UPDATE ON employees TO employees_user;