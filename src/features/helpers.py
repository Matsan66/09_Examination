from src.features.pages.base_page import BasePage
from src.features.pages.catalog_page import CatalogPage
from src.features.pages.add_book_page import AddBookPage


def get_base_page(context):
    if not hasattr(context, "base_page"):
        context.base_page = BasePage(context.page)
    return context.base_page


def get_catalog_page(context):
    if not hasattr(context, "catalog_page"):
        context.catalog_page = CatalogPage(context.page)
    return context.catalog_page


def get_add_book_page(context):
    if not hasattr(context, "add_book_page"):
        context.add_book_page = AddBookPage(context.page)
    return context.add_book_page