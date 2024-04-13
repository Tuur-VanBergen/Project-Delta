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
    result = database.execute_sql_query(uq.check, username)
    if result[0] > 0:
        return {"status": "user exists"}
    database.execute_sql_query(uq.create, (username,))
    return {'festivals': "user created"}


@app.get("/logout")
def logout(username: str):
    database.execute_sql_query(uq.delete, username)


@app.get("/messages")
def messages(room_name: str):
    result = database.execute_sql_query(mq.get_messages, room_name)
    return {'messages': result}


@app.get("/create_room")
def create_room(user_id: int):
    characters = string.ascii_uppercase + string.digits
    room_name = "".join(random.choice(characters) for _ in range(10))
    print(room_name)
    database.execute_sql_query(rq.create, (room_name, 1))


login("a")
create_room()