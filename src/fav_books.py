
class FavoriteBooks:
    """
    Class represents a favorite books list
    """
    def __init__(self):
        self.books = {}

    def add(self, book):
        """
        Adds a book to the favorite books list
        :param book: The book to add
        """
        if book.id not in self.books:
            self.books[book.id] = book

    def remove(self, book):
        """
         Adds a book to the favorite books list
        :param book: The book to remove
        """
        if book.id in self.books:
            del self.books[book.id]
