SELECT
    group_id,
    AVG(grade) AS average_grade
FROM grades
WHERE subject_id = ?
GROUP BY group_id;