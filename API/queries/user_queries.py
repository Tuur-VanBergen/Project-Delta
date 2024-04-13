create = "INSERT INTO user (username) VALUES (%s)"
delete = "DELETE FROM user WHERE username = %s"
check = "SELECT COUNT(*) FROM users WHERE username = %s"