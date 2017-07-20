-- 1
select customer.first_name, customer.last_name, customer.email, address, city.city_id
from city
JOIN address
ON city.city_id = address.city_id
JOIN customer
ON address.address_id = customer.address_id
WHERE city.city_id = 312;

-- 2

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name
from film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'comedy'