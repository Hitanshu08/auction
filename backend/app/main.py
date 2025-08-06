from fastapi import FastAPI, WebSocket, Depends, WebSocketDisconnect
from . import database, crud, schemas, websocket_manager
from .model import models
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from typing import List
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app = FastAPI()

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# WebSocket for auction updates
@app.websocket("/ws/auction/{item_id}")
async def auction_ws(websocket: WebSocket, item_id: int
                    #  , db: AsyncSession = Depends(database.SessionLocal)
                     ):
    await websocket_manager.manager.connect(websocket)
    try:
        print("test")
        while True:
            data = await websocket.receive_json()
            print(data)
            bid = schemas.BidIn(**data)
            # await crud.create_bid(db, item_id, bid)
            await websocket_manager.manager.broadcast({
                "item_id": item_id,
                "user": bid.user,
                "amount": bid.amount
            })
    except WebSocketDisconnect:
        websocket_manager.manager.disconnect(websocket)
