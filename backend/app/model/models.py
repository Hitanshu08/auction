from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class AuctionItem(Base):
    __tablename__ = "auction_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    starting_price = Column(Float)
    current_price = Column(Float, default=0.0)
    end_time = Column(DateTime)
    active = Column(Boolean, default=True)  # is auction still live?


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    item_id = Column(Integer, ForeignKey("auction_items.id"))

