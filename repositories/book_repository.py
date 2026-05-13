import json

class BookRepository:

    @staticmethod
    def read_file():
        with open("DATA/books.json") as f:
            return json.loads(f.read())
    

    @staticmethod
    def get_all_book():
        return BookRepository.read_file()
    
    @staticmethod
    def save_file(books):
        with open("data/books.json", "w") as f:
            f.write(json.dumps(books, indent=2))
   
    
