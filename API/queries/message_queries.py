get = "SELECT * FROM messages WHERE room_name = %s AND sender = %s;"
get_all = "SELECT * FROM messages WHERE room_name = %s;"
send = "INSERT INTO messages (room_name, sender, message) VALUES (%s, %s, %s);"