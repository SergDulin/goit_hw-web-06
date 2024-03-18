SELECT
    student_id,
    name,
    AVG(grade) AS average_grade
FROM grades
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 5;