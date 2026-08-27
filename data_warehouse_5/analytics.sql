--1. Подсчёт количества проведённых занятий каждым преподавателем за учебный год.
SELECT
    t.full_name, --ФИО
    t.department, --кафедра
    d.academic_year, --учебный год
    COUNT(*) AS lessons_count --считаем количество проведённых занятий
FROM fact_schedule AS f
JOIN dim_teacher AS t ON f.teacher_sk = t.teacher_sk
JOIN dim_date AS d ON f.date_sk = d.date_sk
WHERE d.academic_year = '2026/2027'
GROUP BY t.full_name, t.department, d.academic_year --группируем записи
ORDER BY lessons_count DESC; --сортируем по количеству проведённых занятий в порядке убывания

--2. Подсчёт количества проведённых занятий по каждому предмету и процент выполнения плана.
SELECT
    s.name, --название предмета
    s.number_of_hours, --количество часов по плану
    COUNT(*) AS lessons_completed, --количество проведённых занятий
    ROUND(100.0 * COUNT(*) * 2 / NULLIF(s.number_of_hours, 0), 1) AS completion_of_plan --процент выполнения плана (умножаем на 2, так как 1 занятие = 2 часа)
--NULLIF чтобы не делить на ноль
FROM fact_schedule AS f
JOIN dim_subject AS s ON f.subject_sk = s.subject_sk
GROUP BY s.name, s.number_of_hours --группируем записи
ORDER BY completion_of_plan DESC; --сортируем по проценту выполнения плана в порядке убывания

--3. Подсчёт количества проведённых занятий по каждой группе за учебный год и среднего количества в день.
SELECT
    g.name, --название группы
    d.academic_year, --учебный год
    COUNT(*) AS total_lessons, --занятий было проведено
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT d.full_date), 1) AS avg_lessons_per_day --среднее количество занятий в день
FROM fact_schedule f
JOIN dim_group AS g ON f.group_sk = g.group_sk
JOIN dim_date AS d ON f.date_sk = d.date_sk
WHERE d.academic_year = '2025/2026'
GROUP BY g.name, d.academic_year
ORDER BY total_lessons DESC;

-- 4. Подсчёт количества проведённых занятий каждым преподавателем в каждой аудитории.
SELECT
    t.full_name,
    c.number,
    COUNT(*) AS lessons_count -- количество проведённых занятий
FROM fact_schedule AS f
JOIN dim_teacher AS t ON f.teacher_sk = t.teacher_sk
JOIN dim_classroom AS c ON f.classroom_sk = c.classroom_sk
GROUP BY t.full_name, c.number -- группируем записи
ORDER BY t.full_name, lessons_count DESC;