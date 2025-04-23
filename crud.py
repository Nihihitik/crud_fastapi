from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

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
async def get_all_messages() -> List[Message]:
    return messages_db

@app.get("/messages/{message_id}")
async def get_message(message_id: int) -> Message:
    try:
        return messages_db[message_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")

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
    try:
        edit_message = messages_db[message_id]
        edit_message.text = message
        return f"Message updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "Все сообщения удалены"