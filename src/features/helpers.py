from src.features.pages.base_page import BasePage
from src.features.pages.catalog_page import CatalogPage
from src.features.pages.add_book_page import AddBookPage
from src.features.pages.my_books_page import MyBooksPage
from src.features.pages.statistics_page import StatisticsPage


def get_base_page(context):
    """
    Instanciate a base_page
    :param context: page context
    :return: base_page
    """
    if not hasattr(context, "base_page"):
        context.base_page = BasePage(context.page)
    return context.base_page


def get_catalog_page(context):
    """
    Instantiate a catalog_page
    :param context: page context
    :return: catalog_page
    """
    if not hasattr(context, "catalog_page"):
        context.catalog_page = CatalogPage(context.page)
    return context.catalog_page


def get_add_book_page(context):
    """
   Instantiate an add_book page
   :param context: page context
   :return: add_book page
   """
    if not hasattr(context, "add_book_page"):
        context.add_book_page = AddBookPage(context.page)
    return context.add_book_page


def get_my_books_page(context):
    """
   Instantiate a my_books page
   :param context: page context
   :return: my_books page
   """
    if not hasattr(context, "my_books_page"):
        context.my_books_page = MyBooksPage(context.page)
    return context.my_books_page


def get_statistics_page(context):
    """
   Instantiate a statistics page
   :param context: page context
   :return: statistics page
   """
    if not hasattr(context, "statistics_page"):
        context.statistics_page = StatisticsPage(context.page)
    return context.statistics_page
