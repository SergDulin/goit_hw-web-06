SELECT
    student_id,
    name,
    AVG(grade) AS average_grade
FROM grades
WHERE subject_id = ?
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 1;