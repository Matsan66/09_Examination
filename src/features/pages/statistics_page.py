class StatisticsPage:
    """
    Represents the view of "Statistik" in "Läslistan"
    """
    def __init__(self, page):
        self.page = page
        self.statistics_view = page.locator(".stats")
        self.book_count = page.get_by_test_id("book-count")
        self.stars_count = page.get_by_test_id("stars-count")
