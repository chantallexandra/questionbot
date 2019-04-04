
SELECT DISTINCT aggregate_rating, restaurant_name 
FROM restaurants 
WHERE rating_text='excellent'


SELECT DISTINCT city 
FROM code 
NATURAL JOIN restaurants 
WHERE country_name='canada'
