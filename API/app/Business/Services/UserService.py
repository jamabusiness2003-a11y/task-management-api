from app.DataAccess.Repositories.UserRepository import UserRepository
from app.Business.Exceptions.UserException import UserNotFound

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def retrieve_all_users(self):
        return self.user_repository.retrieve_all()

    def retrieve_user_by_id(self, user_id: int):
        user = self.user_repository.retrieve_by_id(user_id)

        if user is None:
            raise UserNotFound()

        return user