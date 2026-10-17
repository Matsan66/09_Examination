import pytest
from src.book_store import BookStore


@pytest.mark.integrationtest
def test_toggle_favorite_adds_book():
    """
    Verify that a book can be added as a favorite.
    """
    # Arrange
    book_store = BookStore()
    book_id = next(iter(book_store.books))

    # Act
    book_store.toggleFavorite(book_id)

    # Assert
    assert book_id in book_store.favorite_books.books


@pytest.mark.integrationtest
def test_toggle_favorite_removes_book():
    """
    Verify that a book can be removed as a favorite.
    """
    # Arrange
    book_store = BookStore()
    book_id = next(iter(book_store.books))

    # Act
    book_store.toggleFavorite(book_id)

    book_store.toggleFavorite(book_id)

    # Assert
    assert book_id not in book_store.favorite_books.books