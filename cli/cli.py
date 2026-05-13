from cli.menu import Menu
from cli.auth_handlers import AuthHandler
from cli.bookhandler import Bookhandlers


class Library:
    def __init__(self):
        self.menu = Menu()
        self.auth_handler = AuthHandler()
        self.book_handler = Bookhandlers()
    

    def run(self):
       print("------Welcome to library------")

       while True:
           if self.auth_handler.current_user:
               self.menu.print_user_menu()

               option = input("> ")
               if option == "0":
                   self.auth_handler.logout()
               elif option == "1":
                   self.book_handler.search_book()
               elif option == "2":
                   self.book_handler.show_all_books()
               elif option == "3":
                   self.book_handler.borrow_books(self.auth_handler.current_user)
               elif option == "4":
                   self.book_handler.return_book(self.auth_handler.current_user)
               else:
                   print("Bunday option topilmadi!")
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
                   

        