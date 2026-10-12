## 📊 Examinationsuppgift
### Testautomatisering och testverktyg

### 🟦Vad är testat

#### Enhetstester
Filen test_book_store.py innehåller nedanstående enhetstester för att verifiera 
BookStores metoder addBook() och toggleFavorite().  

1. test_book_store_add_book 
2. test_book_store_toggle_favorite_adds_book 
3. test_book_store_toggle_favorite_removes_book

Jag har använt Pytest Mock för att för att ersätta beroendet till FavoriteBooks.
```python
book_store.favorite_books = Mock()
book_store.favorite_books.books = {book_id: book}
```
Filen test_fav_books.py innehåller nedanstående enhetstester för att verifiera 
FavoriteBooks metoder add() och remove(). 

1. test_fav_books_add_book
2. est_fav_books_remove_book
3. test_fav_books_add_existing_book_does_not_add_duplicate

### :🟦Start av tester
Jag har använt Pytest markers för att separera exekvering av olika testtyper.
#### Enhetstester
```
pytest -m "unittest" -v
```
