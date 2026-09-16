# Write your MySQL query statement below
WITH total_users AS (
    SELECT COUNT(*) AS total_cnt
    FROM Users
)

SELECT r.contest_id, 
    ROUND(COUNT(user_id) * 100.0 / tu.total_cnt, 2) AS percentage 
FROM Register r
CROSS JOIN total_users tu
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC