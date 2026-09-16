# Write your MySQL query statement below
SELECT mg.name
FROM Employee mg
JOIN Employee e
    ON mg.id = e.managerId
GROUP BY mg.id, mg.name
HAVING COUNT(e.id) >= 5