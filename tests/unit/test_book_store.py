import pytest
from unittest.mock import Mock


@pytest.mark.unittest
def test_book_store_add_book(book_store):
    """
    Verify that a book can be added to the book store.
    """
    # Arrange
    book_author = "Alex DeLarge"
    book_title = "My first test book"
    expected_id = book_store.next_id

    # Act
    book_store.addBook(book_author, book_title)

    # Assert
    assert expected_id in book_store.books
    assert book_store.books[expected_id].author == book_author
    assert book_store.books[expected_id].title == book_title
    assert book_store.next_id == expected_id + 1


@pytest.mark.unittest
def test_book_store_toggle_favorite_adds_book(book_store):
    """
    Verify that a book can be added as a favorite.
    """
    # Arrange
    book_id = next(iter(book_store.books))
    book = book_store.books[book_id]

    # Mock FavoriteBooks objekt with no items
    book_store.favorite_books = Mock()
    book_store.favorite_books.books = {}

    # Act
    book_store.toggleFavorite(book_id)

    # Assert
    book_store.favorite_books.add.assert_called_once_with(book)


@pytest.mark.unittest
def test_book_store_toggle_favorite_removes_book(book_store):
    """
    Verify that a book can be removed as a favorite.
    """
    # Arrange
    book_id = next(iter(book_store.books))
    book = book_store.books[book_id]

    # Mock FavoriteBooks objekt with one item
    book_store.favorite_books = Mock()
    book_store.favorite_books.books = {book_id: book}

    # Act
    book_store.toggleFavorite(book_id)

    # Assert
    book_store.favorite_books.remove.assert_called_once_with(book)
