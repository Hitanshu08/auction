from pydantic import BaseModel
from datetime import datetime

class BidIn(BaseModel):
    user: str
    amount: float

class BidOut(BidIn):
    timestamp: datetime

class AuctionItemOut(BaseModel):
    id: int
    name: str
    description: str
    current_price: float
    end_time: datetime
