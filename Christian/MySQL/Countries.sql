-- 1
SELECT name, percentage, language 
FROM countries 
JOIN languages 
ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER by percentage DESC;


-- 2
SELECT countries.name, Count(cities.name) as NumberOfCities
FROM cities
join countries 
ON countries.code = cities.country_code
GROUP BY countries.name
ORDER BY NumberOfCities DESC;

-- 3
SELECT cities.name, cities.population
FROM countries
JOIN cities
ON cities.country_code = country_code 
WHERE countries.name = 'Mexico' and cities.population > 500000
ORDER BY cities.population DESC;

-- 4
SELECT countries.name, language, percentage 
FROM countries 
JOIN languages 
ON countries.id = languages.country_id
WHERE percentage > 89
ORDER BY percentage DESC;

-- 5
SELECT countries.name, population, surface_area
FROM COUNTRIES
WHERE surface_area < 501
AND population > 100000;

-- 6
SELECT name, government_form, capital, life_expectancy
FROM COUNTRIES
WHERE government_form = 'Constitutional Monarchy'
AND capital > 200
AND life_expectancy > 75;

-- 7
SELECT cities.name, countries.name, cities.district, cities.population
FROM cities
JOIN countries
ON cities.country_code = country_code
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population > 500000;

-- 8
SELECT countries.region, Count(countries.name) as Countries 
FROM countries
GROUP BY countries.region
ORDER BY Countries DESC;