# Write your MySQL query statement below
SELECT t.id
FROM Weather t
JOIN Weather y
ON y.recordDate = DATE_SUB(t.recordDate, INTERVAL 1 DAY) AND t.temperature > y.temperature
