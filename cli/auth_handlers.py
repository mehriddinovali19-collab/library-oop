from getpass import getpass
from sys import exit


from utils.validators import nomalize_full_name
from services.user_service import UserService

class AuthHandler:

    def __init__(self):
        self.current_user = None

        
    def register(self):
        print("Ro'yxatdan o'tish uchun formani to'ldiring!")

        username = input("Username: ").strip()
        password = getpass("Password: ").strip()
        confirm = getpass("Confirm: ").strip()
        full_name = nomalize_full_name(input("Full Name: ").strip())
        
        
        self.current_user = UserService.register(username, password, confirm, full_name)


    def login(self):
          print("Tizimdan kirish uchun formani to'ldiring!")

          username = input("Username: ").strip()
          password = getpass("Password: ").strip()

          self.current_user = UserService.get_user(username, password)
          if self.current_user:
              print("Siz muvaffaqiyatli kirdingiz.")

          

    def logout(self):
        self.current_user = None
        exit()
        print("Siz muvaffaqiyiatli tizimdan chiqdingiz.")



        
