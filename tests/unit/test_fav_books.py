import pytest
from src.book import Book


@pytest.mark.unittest
def test_fav_books_add_book(favorite_books):
    """
    Verify that a book can be added to favorites.
    """
    # Arrange
    book = Book(500, "My test book", "John Doe")

    # Act
    favorite_books.add(book)

    # Assert
    assert 500 in favorite_books.books
    assert favorite_books.books[book.id] == book


@pytest.mark.unittest
def test_fav_books_remove_book(favorite_books):
    """
    Verify that a book can be removed from favorites.
    """
    # Arrange
    book = Book(500, "My test book", "John Doe")
    favorite_books.add(book)

    # Act
    favorite_books.remove(book)

    # Assert
    assert book.id not in favorite_books.books


@pytest.mark.unittest
def test_fav_books_add_existing_book_does_not_add_duplicate(favorite_books):
    """
    Verify that adding a book with an existing ID does not
    overwrite the original book.
    """
    # Arrange
    first_book = Book(500, "My test book", "John Doe")
    second_book = Book(500, "Another book", "Jane Doe")
    favorite_books.add(first_book)

    # Act
    favorite_books.add(second_book)

    # Assert
    assert len(favorite_books.books) == 1
    assert favorite_books.books[500] == first_book


@pytest.mark.unittest
def test_fav_books_remove_non_existing_book(favorite_books):
    """Verify that removing a non-existing book does nothing."""
    # Arrange
    book = Book(500, "My test book", "John Doe")

    # Act
    favorite_books.remove(book)

    # Assert
    assert favorite_books.books == {}
