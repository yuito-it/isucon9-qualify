from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import (
    App as AppSchema,
    CreateApp as AppCreateSchema,
    Me as MeSchema,
)
from ...cruds.app import (
    create_app, add_admin_user_to_app,
    get_app_by_id, update_app, delete_app
)
from ...cruds.token import verify_token
from ...database import get_db

router = APIRouter(
    prefix="/apps",
    tags=["apps"],
)


@router.post("/", response_model=AppSchema)
async def create_apps(
            app: AppCreateSchema,
            user: MeSchema = Depends(verify_token),
            db: Session = Depends(get_db)
        ):
    new_app: AppSchema = create_app(db=db, app=app)
    app: AppSchema = add_admin_user_to_app(db, new_app.id, user.id)
    return app