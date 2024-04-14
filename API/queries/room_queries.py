create = "INSERT INTO rooms (name, owner) VALUES (%s, %s);"
delete = "DELETE FROM rooms WHERE name = %s;"
get = "SELECT * FROM rooms WHERE name = %s;"