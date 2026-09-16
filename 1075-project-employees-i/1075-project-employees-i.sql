# Write your MySQL query statement below
SELECT p.project_id, ROUND(AVG(emp.experience_years),2) as average_years
FROM Project p
LEFT JOIN Employee emp
ON p.employee_id = emp.employee_id
GROUP BY p.project_id