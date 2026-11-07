from pydantic import BaseModel
from datetime import datetime
from app.DataAccess.Models.User import Role

class UserResponse(BaseModel):
    id : int
    username : str
    email : str
    firstName : str
    lastName : str
    role : Role
    createdAt : datetime
    updatedAt: datetime | None = None