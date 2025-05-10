from database.connector import db_client
from database.entities.user_entity import User
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self):
        self.Session = db_client.get_session

    def get_by_id(self, user_id: int) -> User:
        with self.Session() as db:
            return db.query(User).filter(User.id == user_id).first()

    def create(self, name: str, email: str) -> User:
        with self.Session() as db:
            user = User(name=name, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
