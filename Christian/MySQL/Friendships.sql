SELECT users.first_name, users.last_name, users2.first_name, users2.last_name
FROM users 
LEFT JOIN friendships ON users.id = friendships.users_id
LEFT JOIN users as users2 ON friendships.friend_id = users2.id 