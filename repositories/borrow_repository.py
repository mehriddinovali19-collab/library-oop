import json 
from uuid import uuid1

class BorrowRepository:     
    @staticmethod
    def read_file():
        with open("DATA/borrow.json") as f:
            return json.loads(f.read())
        
    
    @staticmethod
    def save_file(borrows):
        with open("data/borrow.json", "w") as f:
            f.write(json.dumps(borrows, indent=4))


    @staticmethod
    def create_borrow(user, book_id):
        borrows = BorrowRepository.read_file()
        borrows.append({
            'id': str(uuid1()),
            'user_id': user.id,
            'book_id': book_id,
            'username': user.username
        })
        BorrowRepository.save_file(borrows)

    @staticmethod
    def return_borrow(user_id, book_id):
        borrows = BorrowRepository.read_file()
        borrows = [b for b in borrows if not (b['user_id'] == user_id and b['book_id'] == book_id)]
        BorrowRepository.save_file(borrows)

    @staticmethod
    def my_all_books(username):
        my_books = BorrowRepository.read_file()
        for book in my_books:
            if book['username'] == username:
                print(f"Id of the book: {book['id'], book['title']}")
                

