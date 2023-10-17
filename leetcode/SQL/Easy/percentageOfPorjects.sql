SELECT r.contest_id, ROUND(COUNT(r.user_id) / total_users * 100, 2) AS 'percentage'
FROM Register r
JOIN (
  SELECT COUNT(*) AS total_users
  FROM Users
) AS u_total
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id;

-- Redone with CTES:

WITH total_users (total) as (
  SELECT COUNT(*) as total
  FROM users
)

SELECT r.contest_id, ROUND(COUNT(r.user_id) / (SELECT total FROM total_users) * 100, 2) AS 'percentage'
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id;