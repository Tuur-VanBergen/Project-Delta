import string

from fastapi import FastAPI
import database
from queries import room_queries as rq
from queries import user_queries as uq
from queries import message_queries as mq
import random


app = FastAPI()


@app.post("/login")
def login(username: str):
    result = database.execute_sql_query(uq.check, (username,))
    if result[0][0] > 0:
        return {"status": "user exists"}
    database.execute_sql_query(uq.create, (username,))
    return True


@app.post("/logout")
def logout(username: str):
    database.execute_sql_query(uq.delete, (username,))


@app.post("/create_room")
def create_room(username: str):
    characters = string.ascii_uppercase + string.digits
    room_name = "".join(random.choice(characters) for _ in range(10))
    database.execute_sql_query(rq.create, (room_name, username))
    database.execute_sql_query(uq.room, (room_name, username))


@app.post("/remove_room")
def remove_room(room_name: str):
    database.execute_sql_query(rq.delete1, (room_name,))
    database.execute_sql_query(rq.delete2, (room_name,))
    database.execute_sql_query(rq.delete3, (room_name,))


@app.post("/join_room")
def join_room(username: str, room_name: str):
    database.execute_sql_query(uq.room, (room_name, username))


@app.post("/get_messages")
def get_messages(username: str, room_name: str):
    if database.execute_sql_query(rq.get, (room_name,))[0][1] == username or public:
        return {"messages": database.execute_sql_query(mq.get_all, (room_name,))}
    return {"messages": database.execute_sql_query(mq.get, [room_name, database.execute_sql_query(rq.get, [room_name,])[0][1]])}


@app.post("/send_message")
def send_message(room_name: str, username: str,  message: str):
    if database.execute_sql_query(mq.send, (room_name, username, message)):
        return True
    return False


@app.post("/toggle_message_privacy")
def toggle_message_privacy(room_name: str):
    if database.execute_sql_query(rq.get, (room_name,))[0][2] == 0:
        database.execute_sql_query(rq.set_public, (room_name,))
    else:
        database.execute_sql_query(rq.set_private, (room_name,))


