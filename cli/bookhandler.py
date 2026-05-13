from repositories.book_repository import BookRepository
from repositories.borrow_repository import BorrowRepository


class Bookhandlers:
    def show_all_books(self):
        books = BookRepository.get_all_book()
        for book in books:
            print(book['id'], book['title'])
            
    
    
    
    def search_book(self):
        search = input("Search: ")
        books = BookRepository.get_all_book()
        for book in books:
            if search.lower() == book['title'].lower():
                print(f"Id of the book: {book['id']} | Title of the book: {book['title']}")

    def borrow_books(self, user):
        book_id = input("Id of the book: ")
        BorrowRepository.create_borrow(user, book_id)

    def return_book(self, user):
        book_id = input('Book id: ')
        BorrowRepository.return_borrow(user.id, book_id)
        print('Kitob muvaffaqiyatli qaytarildi!')

    #def my_books(self, user):
     #   username = input("username: ")
       # BorrowRepository.my_all_books(user.username)
        



    
    
