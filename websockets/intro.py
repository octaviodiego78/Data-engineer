from faker import Faker
from fastapi import FastAPI, WebSocket


app = FastAPI()

@app.get("/")
async def greet():
    f = Faker()
    return {"name": f.name()}


@app.websocket("/ws")
async def send_user_data(websocket: WebSocket):
    f = Faker()
    await websocket.accept()
    while True:
        await websocket.send_json({"name": f.name(), "email": f.email()})
    