import json
from models.user import User

class UserRepository:
    @staticmethod
    def read_file():
        with open("DATA/users.json") as f:
            return json.loads(f.read())
        
    
    @staticmethod
    def add_user(user: User):
        users = UserRepository.read_file()
        users.append(user.to_dict())
        UserRepository.save_file(users)

    
    @staticmethod
    def save_file(users):
        with open("DATA/users.json", "w") as f:
            f.write(json.dumps(users, indent = 4))
    


    @staticmethod
    def get_user_username(username):
        users = UserRepository.read_file()
        for user in users:
            if user["username"] == username:
                return User(
                    id=user["id"],
                    username=user["username"],
                    hash_password=user["hash_password"],
                    full_name=user["Full name"],
                )

