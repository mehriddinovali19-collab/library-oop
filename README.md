TZ: Kutubxona Boshqaruv Tizimi (CLI)
1. Loyiha haqida
Python OOP yordamida yaratiladigan, JSON faylda ma'lumot saqlaydigan terminal-asoslangan kutubxona boshqaruv dasturi.

2. Texnik talablar
Til: Python 3.10+
Paradigma: OOP (klasslar, inheritance, encapsulation)
DB: JSON fayllar (users.json, books.json, borrows.json)
Interfeys: CLI (terminal menyusi)
Tashqi kutubxonalar: faqat standart kutubxona (json, hashlib, datetime, uuid, os)

3. Funksional talablar
3.1. Autentifikatsiya
Funksiya	Tavsif
register	username (unique), parol (hash qilinadi), full_name
login	username + parol tekshiruvi, sessiya ochish
logout	joriy sessiyani yopish
Validatsiya: username 3+ belgi, parol 6+ belgi, takroriy username taqiqlanadi.

3.2. Kitoblar bilan ishlash (faqat login qilingan user uchun)
Funksiya	Tavsif
search	nomi / muallifi / janri bo'yicha qidirish (case-insensitive)
borrow	kitobni olish (mavjud bo'lsa available -= 1, borrow record yaratiladi)
return	kitobni qaytarish (available += 1, borrow record yopiladi)
my_books	foydalanuvchining hozir o'qiyotgan kitoblari
Cheklovlar: bir foydalanuvchi bir vaqtda 3 tadan ortiq kitob ololmaydi. Kitob mavjud bo'lmasa borrow xatolik beradi.

4. Ma'lumotlar modellari
User

id, username, password_hash, full_name, created_at
Book

id, title, author, genre, total_copies, available_copies
Borrow

id, user_id, book_id, borrowed_at, returned_at (None bo'lishi mumkin)
5. Klasslar arxitekturasi
BaseRepository — abstract: load(), save(), find_by_id()
UserRepository(BaseRepository) — user CRUD
BookRepository(BaseRepository) — book CRUD
BorrowRepository(BaseRepository) — borrow CRUD
AuthService — register / login / logout / hash_password
LibraryService — search / borrow / return / my_books
Session — joriy login qilingan userni saqlaydi (singleton)
CLI — menyu va user input boshqaruvi
6. Fayl strukturasi
library_cli/
├── main.py                 # entry point
├── config.py               # konstantalar (fayl yo'llari, limitlar)
│
├── data/
│   ├── users.json
│   ├── books.json
│   └── borrows.json
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│   └── borrow.py
│
├── repositories/
│   ├── __init__.py
│   ├── base_repository.py
│   ├── user_repository.py
│   ├── book_repository.py
│   └── borrow_repository.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   └── library_service.py
│
├── cli/
│   ├── __init__.py
│   ├── menu.py             # asosiy menyu loop
│   ├── auth_handlers.py    # login/register/logout CLI
│   └── library_handlers.py # search/borrow/return CLI
│
├── utils/
│   ├── __init__.py
│   ├── session.py          # singleton current user
│   ├── hasher.py           # parolni hashlash
│   └── validators.py       # input validatsiya
│
└── exceptions.py           # custom xatoliklar (AuthError, BookNotFoundError, ...)
7. CLI oqimi
[Guest menu]  -> Register / Login / Exit
[User menu]   -> Search / Borrow / Return / My Books / Logout
8. Xatoliklarni boshqarish
Custom exception'lar: AuthError, UserExistsError, BookNotFoundError, BookUnavailableError, BorrowLimitError. Har biri CLI darajasida tutilib, foydalanuvchiga aniq xabar chiqariladi.

9. Qabul kriteriyalari
Dastur qayta ishga tushirilganda ma'lumotlar yo'qolmaydi (JSON saqlanadi)
Parollar plain text saqlanmaydi (SHA-256 + salt)
Login qilmagan user kitob menyusiga kira olmaydi
Bitta JSON fayl bitta repository tomonidan boshqariladi (single source of truth)