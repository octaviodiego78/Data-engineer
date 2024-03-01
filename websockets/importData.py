import websockets
import asyncio
import uuid
import json

async def connect():
    users = []
    async with websockets.connect("ws://localhost:4444/ws") as connection:
        while True:
            if len(users) < 1000:
                msg = await connection.recv()
                msg = json.loads(msg)
                users.append(msg)
            
            else:
                file_path = f'./data/users/{uuid.uuid4()}.json'
                with open(file_path, 'w+') as f:
                    json.dump(users, f)
                users = []


if __name__ == "__main__":
    asyncio.run(connect())