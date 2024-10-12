from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import config

from pydantic import BaseModel

router = APIRouter(
    prefix="/initialize",
    tags=["initialize"],
)

class Item(BaseModel):
    payment_service_url: str
    shipment_service_url: str

@router.post("/initialize")
async def initalize(
            item: Item,
            db: Session = Depends(get_db)
        ):
    shipment = config(name="shipment_service_url", value=item.shipment_service_url)
    payment = config(name="payment_service_url", value=item.payment_service_url)
    db.add(shipment)
    db.add(payment)
    return {
        "campaign": 0,
        "language": "python"
    }