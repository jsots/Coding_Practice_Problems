SELECT weather.id AS 'Id'
FROM Weather JOIN Weather w 
ON DATEDIFF(weather.recordDate, w.recordDate) = 1
AND weather.Temperature > w.Temperature;