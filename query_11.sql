SELECT
    AVG(grade) AS average_grade
FROM grades
WHERE student_id = ?
AND teacher_id = ?;