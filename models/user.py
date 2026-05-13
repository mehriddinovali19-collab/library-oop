class User:

    def __init__(self, id: str, username: str, hash_password: str, full_name: str):
        self.id = id
        self.username = username
        self.hash_password = hash_password
        self.full_name = full_name

    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "hash_password": self.hash_password,
            "Full name": self.full_name,

        }
        