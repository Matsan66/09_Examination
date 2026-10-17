import re

class CatalogPage:
    """
    Represents the view of the view "Katalog" in "Läslistan"
    """
    def __init__(self, page):
        self.page = page
        self.catalog_description = page.get_by_text(re.compile("Sidan för dig som gillar att läsa."))
        self.catalog = page.locator(".catalog")
        self.books = page.locator(".book")
        self.favorite_buttons = page.locator(".star")


