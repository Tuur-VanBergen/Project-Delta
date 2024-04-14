import string

from fastapi import FastAPI
import database
from queries import room_queries as rq
from queries import user_queries as uq
from queries import message_queries as mq
import random


app = FastAPI()


@app.get("/login")
def login(username: str):
    result = database.execute_sql_query(uq.check, (username,))
    if result[0][0] > 0:
        return {"status": "user exists"}
    database.execute_sql_query(uq.create, (username,))
    return {'festivals': "user created"}


@app.get("/logout")
def logout(username: str):
    database.execute_sql_query(uq.delete, (username,))


@app.get("/messages")
def messages(room_name: str):
    result = database.execute_sql_query(mq.get_messages, room_name)
    return {'messages': result}


@app.get("/create_room")
def create_room(username: str):
    characters = string.ascii_uppercase + string.digits
    room_name = "".join(random.choice(characters) for _ in range(10))
    database.execute_sql_query(rq.create, (room_name, username))
    database.execute_sql_query(uq.room, (room_name, username))


@app.get("/join_room")
def join_room(username: str, room_name: str):
    database.execute_sql_query(uq.room, (room_name, username))


@app.get("/get_messages")
def get_messages(username: str, room_name: str):
    if database.execute_sql_query(rq.get, (room_name,))[0][1] == username:
        return {"messages": database.execute_sql_query(mq.get, (room_name,))}
    return "Not allowed"


@app.get("/send_messages")
def send_messages(room_name: str, username: str,  message: str):
    if database.execute_sql_query(mq.send, (room_name, username, message)):
        return True
    return False


print(get_messages("b", "YXMU7JTJPS"))

