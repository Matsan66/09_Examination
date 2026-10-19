import pytest
from src.book_store import BookStore
from src.fav_books import FavoriteBooks


@pytest.fixture
def book_store():
    """ returns a BookStore object """
    return BookStore()


@pytest.fixture
def favorite_books():
    """ returns a FavoriteBooks object """
    return FavoriteBooks()
