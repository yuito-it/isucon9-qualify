from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST
from database import get_db

router = APIRouter()

@router.get("/new_items")
async def get_new_items(
            item_id: int = 0,
            created_at: int = 0,
            db: Session = Depends(get_db)
        ):

    if not isinstance(item_id, int) or item_id <= 0:
        raise HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail="item_id param error"
    )
    if not isinstance(item_id, int) or created_at <= 0:
        raise HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail="created_at param error"
    )

    items = []