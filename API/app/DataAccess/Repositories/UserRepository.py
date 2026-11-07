from app.DataAccess.memories_data import USERS
from app.DataAccess.Models.User import User

class UserRepository:

    def retrieve_all(self) -> list[User]:
        return USERS

    def retrieve_by_id(self, user_id: int) -> User | None:
        for user in USERS:
            if user.id == user_id:
                return user
        return None
    