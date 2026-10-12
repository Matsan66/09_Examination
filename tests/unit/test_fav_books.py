import pytest
from src.book import Book
from src.fav_books import FavoriteBooks


@pytest.mark.unittest
def test_fav_books_add_book():
    """
    Verify that a book can be added to favorites.
    """
    # Arrange
    fav_books = FavoriteBooks()

    book = Book(500, "My test book", "John Doe")

    # Act
    fav_books.add(book)

    # Assert
    assert 500 in fav_books.books
    assert fav_books.books[book.id] == book


@pytest.mark.unittest
def test_fav_books_remove_book():
    """
    Verify that a book can be removed from favorites.
    """
    # Arrange
    fav_books = FavoriteBooks()
    book = Book(500, "My test book", "John Doe")
    fav_books.add(book)

    # Act
    fav_books.remove(book)

    # Assert
    assert book.id not in fav_books.books


@pytest.mark.unittest
def test_fav_books_add_existing_book_does_not_add_duplicate():
    """
    Verify that adding a book with an existing ID does not
    overwrite the original book.
    """
    # Arrange
    fav_books = FavoriteBooks()
    first_book = Book(500, "My test book", "John Doe")
    second_book = Book(500, "Another book", "Jane Doe")
    fav_books.add(first_book)

    # Act
    fav_books.add(second_book)

    # Assert
    assert len(fav_books.books) == 1
    assert fav_books.books[500] == first_book
