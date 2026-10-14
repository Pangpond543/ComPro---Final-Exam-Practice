class LibraryBook:
    def __init__(self, title: str, author: str, year_published: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year_published
        self.isbn = isbn
        self.status = "available"
        
    def check_out(self):
        if self.status == "available":
            self.status = "checked out"
            print(f"\nยืมหนังสือ {self.title} สำเร็จ")
        else:
            print(f"{self.title} - หนังสือเล่มนี้ถูกยืมไปแล้ว ")
     
    def return_book(self):
        if self.status == "checked out":
            self.status = "available"
            print(f"\nคืนหนังสือ {self.title} สำเร็จ")
        else:
            print(f"{self.title} - หนังสือเล่มนี้ยังไม่ได้ถูกยืม ")
    
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nISBN: {self.isbn}\nStatus: {self.status}\n")
    
    
def menu():
    
    library = {}
    while True:
        print("1. Add a new book to the library.\n2. Check out a book.\n3. Return a book.\n4. Display information about a specific book.\n5. Display all books in the library.\n6. Exit the program.\n")
        num = int(input("choose menu 1-6: "))
        if num == 1:
            name = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            isbn = input("ISBN: ")
            
            while not isbn.isdigit():
                isbn = input("กรอกเฉาะตัวเลขเท่านั้น: ")
                
            new_book = LibraryBook(name, author, year, isbn)
            library[isbn] = new_book
            
        elif num == 2 :
            isbn = input("ยืมหนังสือ(ISBN): ")
            while not isbn.isdigit():
                isbn = input("กรอกเฉาะตัวเลขเท่านั้น: ")
            
            if isbn not in library:
                print("\nไม่พบหนังสือ")
                continue
                 
            book = library.get(isbn)
            book.check_out()
            
        elif num == 3 :
            isbn = input("คืนหนังสือ(ISBN): ")
            while not isbn.isdigit():
                isbn = input("กรอกเฉาะตัวเลขเท่านั้น: ")
                    
            book = library.get(isbn)
            book.return_book()
            
        elif num == 4 :
            isbn = input("หาหนังสือ(ISBN): ")
            while not isbn.isdigit():
                isbn = input("กรอกเฉาะตัวเลขเท่านั้น: ")
            
            if isbn not in library:
                print("\nไม่พบหนังสือ")
                continue
                    
            book = library.get(isbn)
            book.display_info()
            
        elif num == 5 :      
            print("\nAll book: ")
            for b in library.values():
                book = b
                print(f"หนังสือ: {book.title}")
            
        elif num == 6 :
            break
        else:
            print("\nIncorrect")
            
menu()