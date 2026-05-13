from repositories.borrow_repository import BorrowRepository

class BorrowService:

    @staticmethod
    def return_book(user, book_id):
        BorrowRepository.return_book(user, book_id)