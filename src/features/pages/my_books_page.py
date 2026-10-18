class MyBooksPage:
    """
    Represents the view of "Mina böcker" in "Läslistan"
    """
    def __init__(self, page):
        self.page = page
        self.my_books_view = page.locator(".favorites")
        self.empty_list_message = page.get_by_text(
            "När du valt, kommer dina favoritböcker att visas här.")
        self.book_list = page.get_by_test_id("book-list")
