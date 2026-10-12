from src.book import Book
from src.fav_books import FavoriteBooks


class BookStore:
    def __init__(self):
        self.books = {
            100: Book(100, "Ormar på ett plan: En Python-berättelse",
                      "Guido van Rossum"),
            101: Book(101, "The Pragmatic Procrastinator",
                      "Dave Thomasson"),
            102: Book(102, "Python för folk som hatar ormar",
                      "Monty Pythonsson"),
            103: Book(103, "Why Your Tests Are Lying to You",
                      "Kent Backdoor"),
            104: Book(104, "Playwright: Click It Till You Make It",
                      "Microslop Browserdóttir"),
            105: Book(105, "Git Blame and Other Ways to Lose Friends",
                      "Linus Torvalds"),
            106: Book(106, "Learn Python in 21 Years",
                      "Sams Teachyourself"),
            107: Book(107, "Agile Is a Feeling",
                      "Jeff Sutherland"),
            108: Book(108, "Playwright: Waiting for Selectors",
                      "Samuel Barclay Beckett"),
            109: Book(109, "Stack Overflow: A Love Story",
                      "Copy Pasta"),
            110: Book(110, "My First Regex (And Last)",
                      "Larry Wallström"),
            111: Book(111, "The Developer Who Knew Nothing",
                      "George R.R. Martin"),
            112: Book(112, "The Bugs are Coming",
                      "George R.R. Martin"),
        }
        self.next_id = max(self.books.keys()) + 1
        self.favorite_books = FavoriteBooks()

    def addBook(self, author, title):
        book = Book(self.next_id, title, author)
        self.books[self.next_id] = book
        self.next_id += 1

    def toggleFavorite(self, book_id):
        if book_id not in self.books:
            return

        book = self.books[book_id]

        if book_id in self.favorite_books.books:
            self.favorite_books.remove(book)
        else:
            self.favorite_books.add(book)
