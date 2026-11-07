from fastapi import APIRouter, HTTPException, status
from app.Presentation.Schemas.UserSchema import UserResponse
from app.DataAccess.memories_data import USERS
from app.DataAccess.Repositories.UserRepository import UserRepository
from app.Business.Services.UserService import UserService
from app.Business.Exceptions.UserException import UserNotFound

router = APIRouter(prefix="/users", tags=["Users"])

service = UserService(UserRepository())

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def retrieveUsers():
    return service.retrieve_all_users()

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def retrieveUserById(user_id: int):
    try:
        user = service.retrieve_user_by_id(user_id)
        return user
    except UserNotFound as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=str(exc)
        )