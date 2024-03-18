SELECT
    student_id,
    name,
    grade,
    date
FROM grades
WHERE group_id = ?
AND subject_id = ?
ORDER BY date DESC
LIMIT 1;