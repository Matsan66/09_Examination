class BasePage:
    """
    Represents the view of basepage "Läslistan"
    """
    def __init__(self, page):
        self.page = page
        self.main_heading = page.get_by_role("heading", name="Läslistan")
        self.welcome_heading = page.get_by_role("heading", name="Välkommen!")
        self.catalog_button = page.get_by_test_id("catalog")
        self.add_book_button = page.get_by_test_id("add-book")
        self.my_books_button = page.get_by_test_id("favorites")
        self.statistics_button = page.get_by_test_id("statistics")

    def navigate_to(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/",
                       timeout=10_000)

    def get_button_name(self, button_name):
        if button_name == "catalog":
            return self.catalog_button
        elif button_name == "add-book":
            return self.add_book_button
        elif button_name == "favorites":
            return self.my_books_button
        elif button_name == "statistics":
            return self.statistics_button
