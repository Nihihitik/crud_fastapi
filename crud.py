from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

messages_db = [
  {
    "id": 0,
    "text": "string"
  },
  {
    "id": 1,
    "text": "string"
  },
  {
    "id": 2,
    "text": "string"
  }
]

class Message(BaseModel):
    id: int
    text: str

@app.get('/')
async def get_all_messages() -> dict:
    return {'Сообщения': messages_db}

@app.get("/messages/{message_id}")
async def get_message(message_id: int):
    return messages_db[message_id]

@app.post("/message")
async def create_message(message:  Message) -> str:
    if len(messages_db) == 0:
        message.id = 0
    else:
        message.id = max([i.dict()['id'] for i in messages_db]) + 1
    messages_db.append(message)
    return f"Сообщение создано"

@app.put("/message/{message_id}")
async def update_message(message_id: int, message: str = Body()) -> str:
    edit_message = messages_db[message_id]
    edit_message.text = message
    return f"Сообщение обновлено!"

@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    messages_db.pop(message_id)
    return f"Сообщение с ID: {message_id} было удалено!"

@app.delete("/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "Все сообщения удалены"