from fastapi import APIRouter, HTTPException
from app.Presentation.Schemas.UserSchema import UserResponse
from app.DataAccess.memories_data import USERS

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse], status_code=200)
def retrieveUsers():
    return USERS

@router.get("/{user_id}", response_model=UserResponse, status_code=200)
def retrieveUserById(user_id: int):
    for user in USERS:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")