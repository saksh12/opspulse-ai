from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json

from app.services.store import events

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

@app.get("/")
def home():
    return {"message": "OpsPulse AI Running"}

@app.get("/events")
def get_events():
    return events

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)

async def broadcast(event):
    for c in clients:
        await c.send_text(json.dumps(event))