from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import schemas
from .model import models

async def create_bid(db: AsyncSession, item_id: int, bid: schemas.BidIn):
    db_bid = models.Bid(user=bid.user, amount=bid.amount, item_id=item_id)
    await db.add(db_bid)
    await db.commit()
    return db_bid

async def get_highest_bid(db: AsyncSession, item_id: int):
    result = await db.execute(
        select(models.Bid).where(models.Bid.item_id == item_id).order_by(models.Bid.amount.desc()).limit(1)
    )
    return result.scalar_one_or_none()
