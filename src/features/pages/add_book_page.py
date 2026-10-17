class AddBookPage:
    """
    Represents the view of the view "Lägg till bok" in "Läslistan"
    """
    def __init__(self, page):
        self.page = page
        self.add_book_form = page.locator(".form")
        self.title_field = page.get_by_test_id("add-input-title")
        self.author_field = page.get_by_test_id("add-input-author")
        self.add_new_book_button = page.get_by_test_id("add-submit")
