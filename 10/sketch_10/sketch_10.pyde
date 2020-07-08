import unittest

class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self):
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook):
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")
 
class Customer():
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
 
def setup():
    size(220,100)
    global library, Madzia
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
    library = Library(books)
    Madzia = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)
 
def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            
class Testowanie(unittest.TestCase):
    def test_klient_wypozycza_i_oddaje_ksiazke(self): # unit testy z zalożenia powinny testować najmniejszą jednostkę logiczną kodu
        klient = Customer()
        self.assertFalse(klient.haveBook)
        self.assertEqual(klient.book, "") # do tąd to powinien być test tworzenia klienta
        klient.requestBook("Wiedzmin") # od tąd to powinien być oddzielny test wypożyczania
        self.assertTrue(klient.haveBook)
        self.assertEqual(klient.book, "Wiedzmin")
        klient.returnBook() # a od tąd to mógłby być trzeci test - zwrócenia książki
        self.assertFalse(klient.haveBook)
        
    def test_zwrocenie_ksiazki_do_biblioteki(self):
        biblioteka = Library(["Zbrodnia i kara", "Buszujacy w zbozu"])
        self.assertEqual(biblioteka.availableBooks, ["Zbrodnia i kara", "Buszujacy w zbozu"])
        biblioteka.addBook("Folwark zwierzecy") # ponownie - to już kolejny test, powyżej tworzenia biblioteki, poinżej dodawnaia (oddawania) książek
        self.assertEqual(biblioteka.availableBooks, ["Zbrodnia i kara", "Buszujacy w zbozu", "Folwark zwierzecy"])
        
if __name__ == '__main__':
    unittest.main()
    
# 2 pkt
            
