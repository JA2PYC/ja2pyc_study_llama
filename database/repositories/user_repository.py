# database/repositories/user_repository.py
from database.database_manager import DatabaseManager as db_manager
from database.entities.user_entity import UserEntity

class UserRepository:
    def __init__(self):
        self.db_session = db_manager.get_session()

    def get_all_users(self):
        return self.db_session.query(UserEntity).all()

    def get_user_by_id(self, user_id):
        return self.db_session.query(UserEntity).filter(UserEntity.id == user_id).first()


# from database.connector import db_client
# from database.entities.user_entity import User
# from sqlalchemy.orm import Session


# class UserRepository:
#     def __init__(self):
#         self.Session = db_client.get_session

#     def get_by_id(self, user_id: int) -> User:
#         with self.Session() as db:
#             return db.query(User).filter(User.id == user_id).first()

#     def create(self, name: str, email: str) -> User:
#         with self.Session() as db:
#             user = User(name=name, email=email)
#             db.add(user)
#             db.commit()
#             db.refresh(user)
#             return user
