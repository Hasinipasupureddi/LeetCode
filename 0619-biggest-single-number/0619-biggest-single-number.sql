# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN COUNT(*) = 1 THEN num
        ELSE NULL
    END AS num
FROM MyNumbers
GROUP BY num
ORDER BY COUNT(*) = 1 DESC, num DESC
LIMIT 1;