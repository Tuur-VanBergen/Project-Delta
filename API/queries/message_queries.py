get_messages = "SELECT * FROM messages WHERE room_name = %s;"
send_messages = "INSERT INTO messages (room_name, sender_id, message) VALUES (%s, %s, %s);"