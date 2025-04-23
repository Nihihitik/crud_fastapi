from fastapi import FastAPI, Body

app = FastAPI()

messages_db = {"0": "First post in FastAPI"}

@app.get('/')
async def get_all_messages() -> dict:
    return messages_db

@app.get("/messages/{message_id}")
async def get_message(message_id: int) -> str:
    return messages_db[message_id]

@app.post("/message")
async def create_message(message:  str) -> str:
    current_index = len(messages_db)
    messages_db[current_index] = message
    return f"Сообщение добавлено!"

@app.put("/message/{message_id}")
async def update_message(message_id: str, message: str = Body()) -> str:
    messages_db[message_id] = message
    return f"Сообщение изменено!"

@app.delete("/message/{message_id}")
async def delete_message(message_id: str) -> str:
    messages_db.pop(message_id)
    return f"Сообщение с ID: {message_id} было удалено!"

@app.delete("/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "Все сообщения удалены"