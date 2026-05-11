from cli.menu import Menu
from cli.auth_handlers import AuthHandler


class Library:
    def __init__(self):
        self.menu = Menu()
        self.auth_handler = AuthHandler()
    

    def run(self):
       print("------Welcome to library------")

       while True:
           if self.auth_handler.current_user:
               self.menu.print_user_menu()
           else:
               self.menu.print_main_menu()

               option = input("> ")
               if option == "1":
                   self.auth_handler.register()
               elif option == "2":
                   self.auth_handler.login()
               elif option == "0":
                   self.auth_handler.logout()
               else:
                   print("Bunday option topilmadi!")
                   

        