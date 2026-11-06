from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class Role(Enum):
    REGISTERED_USER = "registered_user"
    ADMINISTRATER = "administrater"
    SUPPORT_STAFF = "support_staff"


class UserResponse(BaseModel):
    id : int
    username : str
    email : str
    passwordHash : str
    firstName : str
    lastName : str
    role : Role
    createdAt : datetime = Field(default_factory=datetime.now)
    updateAt: datetime | None = None