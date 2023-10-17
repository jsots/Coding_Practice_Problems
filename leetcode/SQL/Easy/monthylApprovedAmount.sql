SELECT DATE_FORMAT(trans_date, '%Y-%m') as month, country, COUNT(trans_date) as trans_count, COUNT(CASE WHEN state LIKE 'approved' THEN trans_date END) as approved_count, SUM(amount) as trans_total_amount, SUM(CASE WHEN state LIKE 'approved' THEN amount ELSE 0 END) as approved_total_amount
FROM Transactions
GROUP BY country, month