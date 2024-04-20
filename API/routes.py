from fastapi import APIRouter
import database
from queries import room_queries as rq
from queries import user_queries as uq
from queries import message_queries as mq
import random

import string

app = APIRouter()


@app.post("/login")
def login(username: str):
    result = database.execute_sql_query(uq.check, (username,))
    if result[0][0] > 0:
        return {"status": "user exists"}
    success = database.execute_sql_query(uq.create, (username,))
    if success:
        return {"status": "user created"}
    return {"status": "user creation failed"}


@app.post("/logout")
def logout(username: str):
    success = database.execute_sql_query(uq.delete, (username,))
    if success:
        return {"status": "user logged out"}
    return {"status": "user logout failed"}


@app.post("/create_room")
def create_room(username: str):
    characters = string.ascii_uppercase + string.digits
    room_name = "".join(random.choice(characters) for _ in range(10))
    success1 = database.execute_sql_query(rq.create, (room_name, username))
    success2 = database.execute_sql_query(uq.room, (room_name, username))
    if success1 and success2:
        return {"status": "room created", "room": room_name}
    return {"status": "room creation failed"}


@app.post("/remove_room")
def remove_room(username: str):
    room_name = database.execute_sql_query(uq.get, (username,))[0][2]
    success1 = database.execute_sql_query(rq.delete1, (room_name,))
    success2 = database.execute_sql_query(rq.delete2, (room_name,))
    success3 = database.execute_sql_query(rq.delete3, (room_name,))
    if success1 and success2 and success3:
        return {"status": "room removed"}
    return {"status": "room removed failed"}


@app.post("/join_room")
def join_room(username: str, room_name: str):
    success = database.execute_sql_query(uq.room, (room_name, username))
    if success:
        return {"status": "room joined"}
    return {"status": "room not found"}


@app.post("/get_messages")
def get_messages(username: str, room_name: str):
    if (database.execute_sql_query(rq.get, (room_name,))[0][1] == username or
            database.execute_sql_query(rq.get, (room_name,))[0][2] > 0):
        return {"messages": database.execute_sql_query(mq.get_all, (room_name,))}
    return {"messages": database.execute_sql_query(mq.get, (room_name, database.execute_sql_query(rq.get, (room_name,))[0][1]))}


@app.post("/send_message")
def send_message(room_name: str, username: str,  message: str):
    success = database.execute_sql_query(mq.send, (room_name, username, message,))
    if success:
        return {"status": "message sent"}

    return {"status": "message not sent"}


@app.post("/toggle_message_privacy")
def toggle_message_privacy(room_name: str):
    if database.execute_sql_query(rq.get, (room_name,))[0][2] == 0:
        database.execute_sql_query(rq.set_public, (room_name,))
        return {"status": "privacy disabled"}
    database.execute_sql_query(rq.set_private, (room_name,))
    return {"status": "privacy enabled"}


