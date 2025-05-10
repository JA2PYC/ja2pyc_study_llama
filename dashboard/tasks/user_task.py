from database.services.user_service import UserService

user_service = UserService()

def create_user(name: str, email: str):
    return user_service.register_user(name, email)

def get_user(user_id: int):
    return user_service.get_user_detail(user_id)
