SELECT
    subject_id,
    name
FROM subjects
INNER JOIN grades ON subjects.id = grades.subject_id
WHERE student_id = ?
AND teacher_id = ?
GROUP BY subject_id;