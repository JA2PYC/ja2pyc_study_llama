# database/services/user_service.py
from database.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def list_users(self):
        return self.user_repository.get_all_users()

    def get_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)


# from database.repositories.user_repository import UserRepository

# class UserService:
#     def __init__(self):
#         self.repo = UserRepository()

#     def register_user(self, name: str, email: str):
#         # 예외 처리, 로깅, 검증 등 포함 가능
#         return self.repo.create(name, email)

#     def get_user_detail(self, user_id: int):
#         return self.repo.get_by_id(user_id)
