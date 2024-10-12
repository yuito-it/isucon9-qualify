from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import config

from pydantic import BaseModel

router = APIRouter(
    prefix="/apps",
    tags=["apps"],
)

class Item(BaseModel):
    payment_service_url: str
    shipment_service_url: str

@router.post("/initialize")
async def initalize(
            item: Item,
            db: Session = Depends(get_db)
        ):
    config = config(name="payment_service_url", value=item.payment_service_url)
    db.add(config)
    return {
        "campaign": 0,
        "language": "python"
    }