from uuid import uuid1

from models.user import User
from utils.hasher import hash_password
from utils.validators import validate_username, validate_password, nomalize_full_name
from repositories.user_repository import UserRepository

class UserService:

    @staticmethod

    def register(username: str, password: str, confirm: str, full_name: str):
        is_valid, error = validate_username(username)
        if not is_valid:
            print(error)
            return

        is_valid, error = validate_password(password)
        if not is_valid:
            print(error)
            return

        is_valid, error = validate_password(confirm)
        if not is_valid:
            print(error)
            return

        if password != confirm:
             print("Password bir xil emas.")
             return

        full_name = nomalize_full_name(full_name)

        user = User(
            str(uuid1()),
            username = username,
            hash_password = hash_password(password),
            full_name = full_name,

        )

        UserRepository.add_user(user)

        return 
    

    @staticmethod

    def get_user(username, password):
        user = UserRepository.get_user_username(username)
        if user.hash_password == hash_password(password):
            return user

    
