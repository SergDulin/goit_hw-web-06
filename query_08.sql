SELECT
    teacher_id,
    AVG(grade) AS average_grade
FROM grades
GROUP BY teacher_id;