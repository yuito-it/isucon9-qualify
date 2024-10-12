from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/apps",
    tags=["apps"],
)

@router.post("/initialize", response_model=AppSchema)
async def create_apps(
            app: AppCreateSchema,
            user: MeSchema = Depends(verify_token),
            db: Session = Depends(get_db)
        ):
    new_app: AppSchema = create_app(db=db, app=app)
    app: AppSchema = add_admin_user_to_app(db, new_app.id, user.id)
    return app