SELECT query_name, ROUND(AVG(rating / position), 2) as quality, ROUND(COUNT(CASE WHEN rating < 3 THEN query_name END) / COUNT(rating) * 100, 2) as poor_query_percentage
FROM Queries
GROUP BY query_name
ORDER BY quality DESC;