class LibraryService:
    def __init__(self, book_repo, borrow_repo):
        self.book_repo = book_repo
        self.borrow_repo = borrow_repo

    def return_book(self, user_id, book_id):

        borrows = self.borrow_repo.get_all()
        books = self.book_repo.get_all()

        found = False

        for borrow in borrows:

            if (
                borrow["user_id"] == user_id and
                borrow["book_id"] == book_id and
                borrow["returned_at"] is None
            ):

                borrow["returned_at"] = "returned"

                for book in books:
                    if book["id"] == book_id:
                        book["available_copies"] += 1

                self.borrow_repo.save_all(borrows)
                self.book_repo.save_all(books)

                print("Kitob muvaffaqiyatli qaytarildi")
                found = True
                return

        if found == False:
            print("Sizda bu kitob yo'q")