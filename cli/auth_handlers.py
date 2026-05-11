from getpass import getpass

from utils.validators import validate_user, validate_password, nomalize_full_name

class AuthHandler:

    def __init__(self):
        self.current_user = None

        
    def register(self):
        print("Ro'yxatdan o'tish uchun formani to'ldiring!")

        username = input("Username: ").strip()
        password = getpass("Password: ").strip()
        confirm = getpass("Confirm: ").strip()
        full_name = nomalize_full_name(input("Full Name: ").strip())

        is_valid, error = validate_user(username)
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
    def login(self):
          print("Tizimdan kirish uchun formani to'ldiring!")

          username = input("Username: ").strip()
          password = getpass("Password: ").strip()

    def logout(self):
        self.current_user = None
        print("Siz muvaffaqiyiatli tizimdan chiqdingiz.")



        
