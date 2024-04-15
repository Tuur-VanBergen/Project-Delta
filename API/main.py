import string

from fastapi import FastAPI
import database
from queries import room_queries as rq
from queries import user_queries as uq
from queries import message_queries as mq
import random


app = FastAPI()
public = False


@app.get("/login")
def login(username: str):
    result = database.execute_sql_query(uq.check, (username,))
    if result[0][0] > 0:
        return {"status": "user exists"}
    database.execute_sql_query(uq.create, (username,))
    return True


@app.get("/logout")
def logout(username: str):
    database.execute_sql_query(uq.delete, (username,))


@app.get("/create_room")
def create_room(username: str):
    characters = string.ascii_uppercase + string.digits
    room_name = "".join(random.choice(characters) for _ in range(10))
    database.execute_sql_query(rq.create, (room_name, username))
    database.execute_sql_query(uq.room, (room_name, username))


@app.get("/remove_room")
def remove_room(room_name: str):



@app.get("/join_room")
def join_room(username: str, room_name: str):
    database.execute_sql_query(uq.room, (room_name, username))


@app.get("/get_messages")
def get_messages(username: str, room_name: str):
    global public
    if database.execute_sql_query(rq.get, (room_name,))[0][1] == username or public:
        return {"messages": database.execute_sql_query(mq.get_all, (room_name,))}
    return {"messages": database.execute_sql_query(mq.get, [room_name, database.execute_sql_query(rq.get, [room_name,])[0][1]])}


@app.get("/send_message")
def send_message(room_name: str, username: str,  message: str):
    if database.execute_sql_query(mq.send, (room_name, username, message)):
        return True
    return False


@app.get("/toggle_message_privacy")
def toggle_message_privacy():
    global public
    public = not public

