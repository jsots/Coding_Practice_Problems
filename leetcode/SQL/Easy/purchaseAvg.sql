SELECT p.product_id, if(SUM(units) is not null, ROUND(SUM(p.price * u.units) / SUM(u.units), 2),0) AS 'average_price'
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.Start_date AND p.end_date
GROUP BY p.product_id
ORDER BY p.product_id;


SELECT p.product_id, ROUND(IFNULL(SUM(p.price * u.units)/ SUM(units), 0), 2) as average_price
FROM Prices p
LEFT JOIN UnitsSold u
ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id