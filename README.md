# 📊 Examinationsuppgift

## Testautomatisering och testverktyg

## 🟦 Vad är testat

### 🟠 Enhetstester

Filen `test_book_store.py` innehåller enhetstester som verifierar metoderna `addBook()` och `toggleFavorite()` i `BookStore`.

1. `test_book_store_add_book`
2. `test_book_store_toggle_favorite_adds_book`
3. `test_book_store_toggle_favorite_removes_book`

I testerna används `Mock` från `unittest.mock` för att ersätta beroendet till `FavoriteBooks`. På så sätt kan `BookStore` testas isolerat från den riktiga favoritlistan.

```python
book_store.favorite_books = Mock()
book_store.favorite_books.books = {book_id: book}
```

Filen `test_fav_books.py` innehåller enhetstester som verifierar metoderna `add()` och `remove()` i `FavoriteBooks`.

1. `test_fav_books_add_book`
2. `test_fav_books_remove_book`
3. `test_fav_books_add_existing_book_does_not_add_duplicate`
4. `test_fav_books_remove_non_existing_book`

### 🟣 Integrationstester

Filen `test_book_store_fav_books.py` innehåller integrationstester som verifierar samspelet mellan `BookStore` och `FavoriteBooks` när en bok 
läggs till eller tas bort från favoritlistan.

1. `test_toggle_favorite_adds_book`
2. `test_toggle_favorite_removes_book`

#### Pytest Fixtures

För att förenkla testernas förberedelser och undvika duplicerad kod används pytest fixtures, definierade i tests/conftest.py.

Två fixtures används för att skapa testobjekt:  
- book_store: Skapar en instans av klassen BookStore. 
- favorite_books: Skapar en instans av klassen FavoriteBooks.

Fixtures återanvänds i både enhets- och integrationstesterna. Pytest tillhandahåller automatiskt objekten när respektive 
fixture anges som parameter i en testfunktion. Detta ger en konsekvent testmiljö och gör testerna enklare att läsa och underhålla.

### ⚪ E2E-tester med Gherkin, Behave och Playwright

#### Teststrategi och struktur

Jag har använt Gherkin för att beskriva testerna och specificera vad som ska verifieras. Behave läser mina `.feature`-filer och kopplar 
stegen i dessa till Python-funktioner i step-filer. Playwright används för att styra webbläsaren, hitta element på webbsidan och kontrollera 
att de uppfyller testernas förväntningar.

Jag har delat upp verifieringen av Läslistan i fem logiska delar. Den första omfattar sidans gemensamma gränssnitt, medan de övriga fyra 
fokuserar på funktionaliteten bakom respektive navigeringsknapp, det vill säga de olika vyerna.

De fem delarna är:

1. **Sidans gemensamma gränssnitt:** Kontroll av huvudrubriken, välkomstrubriken och de fyra navigeringsknapparnas synlighet.
2. **Katalogvyn:** Verifiering av att katalogen visas, att böckerna är synliga och att böcker kan favoritmarkeras och avmarkeras.
3. **Lägg till bok-vyn:** Verifiering av formuläret, knappens aktivering och att en ny bok kan läggas till.
4. **Mina böcker-vyn:** Verifiering av den tomma favoritlistan samt att favoritböcker visas och försvinner när favoritmarkeringen ändras.
5. **Statistikvyn:** Verifiering av att statistiksidan visas, att antalet böcker och hjärtmarkerade böcker visas samt att antalen 
6. överensstämmer med katalogen respektive favoritlistan efter en förändring.

#### Page Object Model (POM)

Testerna är uppbyggda enligt Page Object Model (POM), vilket innebär att sidornas element och locators samlas i separata klasser. 
Detta skiljer beskrivningen av sidornas struktur från teststegen och gör koden lättare att underhålla och återanvända.

#### BasePage

Klassen `BasePage` representerar Läslistans gemensamma gränssnitt. Den innehåller locators för huvudrubriken, välkomstrubriken och 
navigeringsknapparna till Katalog, Lägg till bok, Mina böcker och Statistik. Klassen innehåller även en metod för att navigera till webbplatsen.

I `base_page.feature` verifieras att huvudrubriken och välkomsthälsningen visas samt att navigeringsknapparna är synliga. För kontrollen 
av navigeringsknapparna används `Scenario Outline` tillsammans med en `Examples`-tabell. Det gör att samma scenario kan återanvändas för 
att kontrollera samtliga fyra knappar.

#### CatalogPage

Klassen `CatalogPage` innehåller locators för katalogens beskrivning, boklistan, enskilda böcker och favoritknapparna. Locatorn `.book` 
används för att identifiera böckerna i katalogen, medan `.star` används för favoritknapparna.

I `catalog.feature` finns scenarier som verifierar att katalogen visas vid navigering, att minst en bok finns i listan och att alla 
böcker i katalogen är synliga. Därutöver testas att en bok kan markeras som favorit och att favoritmarkeringen kan tas bort.

För att kontrollera flera böcker används Playwright-metoderna `count()` och `nth(i)`. Playwrights `expect()` används för att verifiera 
synlighet och CSS-klasser.

#### AddBookPage

Klassen `AddBookPage` representerar vyn Lägg till bok. Den innehåller locators för formuläret, titelfältet, författarfältet och 
knappen Lägg till ny bok. Där sådana finns hämtas locators med hjälp av sidans `test-id`.

I `add_book.feature` testas att vyn visas korrekt efter navigering. Testet verifierar att formuläret samt titel- och författarfälten 
är synliga.

Ett separat scenario testar knappens aktivering. När endast titeln har fyllts i ska knappen vara inaktiverad. När även författaren 
har fyllts i ska knappen aktiveras.

Ytterligare ett scenario testar hela flödet för att lägga till en bok. Testet fyller i titel och författare, klickar på knappen och 
verifierar att formuläret töms och att knappen åter blir inaktiverad. Därefter navigerar testet till katalogen och kontrollerar att den nya boken visas med rätt titel och författare.

#### MyBooksPage

Klassen `MyBooksPage` representerar vyn Mina böcker. Den innehåller locators för vyn, boklistan och meddelandet som visas när inga 
favoritböcker har valts.

I `my_books.feature` testas att användaren kan navigera till vyn, att rätt meddelande visas när favoritlistan är tom och att en 
favoritbok visas i listan. Det testas även att en bok försvinner från listan när favoritmarkeringen tas bort.

Testerna kontrollerar därmed både hur vyn visas när listan är tom och hur listan uppdateras när användaren ändrar sina favoriter.

#### StatisticsPage

Klassen `StatisticsPage` representerar vyn Statistik. Den innehåller locators för statistikvyn, antalet böcker och antalet hjärtmarkerade 
böcker. Dessa används för att hämta information från sidans textelement.

I `statistics.feature` finns scenarier som verifierar att statistikvyn visas och att texten med antalet böcker respektive antalet 
hjärtmarkerade böcker är synlig.

Därutöver finns tre scenarier som jämför statistiken med informationen i övriga vyer:

- I det första scenariot läggs en ny bok till. Antalet böcker i katalogen sparas och jämförs sedan med antalet som visas på statistiksidan.
- I det andra scenariot favoritmarkeras en bok. Antalet böcker i vyn Mina böcker sparas och jämförs sedan med antalet hjärtmarkerade böcker 
på statistiksidan.
- I det tredje scenariot favoritmarkeras en bok som sedan avmarkeras igen. Antalet böcker i vyn Mina böcker sparas och jämförs sedan 
med antalet hjärtmarkerade böcker på statistiksidan.

För att hämta antalen från statistiksidans texter används det reguljära uttrycket `re.search(r"\d+", ...)` för att hitta sifferföljden. 
Resultatet hämtas med `group()` och omvandlas till ett heltal med `int()` innan värdena jämförs med `assert`.

Dessa scenarier kontrollerar därmed inte bara att statistiken visas, utan även att den överensstämmer med innehållet i katalogen och 
favoritlistan.

#### Gemensamma hjälpfunktioner

I `helpers.py` finns funktionerna `get_base_page(context)`, `get_catalog_page(context)`, `get_add_book_page(context)`, 
`get_my_books_page(context)` och `get_statistics_page(context)`. De skapar respektive Page Object vid behov och återanvänder 
objektet under det aktuella scenariot.

Hjälpfunktionerna samlar initialiseringen av Page Object-klasserna på ett ställe. Det minskar dupliceringen av kod och gör att 
step-filerna kan använda samma Page Object utan att upprepa initieringslogiken.

Hjälpfunktionerna navigerar inte automatiskt till respektive vy. Navigeringen utförs i teststegen, medan Page Object-klasserna 
innehåller locators för sidans element.

#### Scenario Outline och Examples

I `base_page.feature` används `Scenario Outline` tillsammans med en `Examples`-tabell för att verifiera att de fyra navigeringsknapparna 
är synliga. Parametern `button_name` får ett värde från varje rad i tabellen. Värdena motsvarar knapparnas test-id:n: `catalog`, `add-book`, 
`favorites` och `statistics`.

Behave kör scenariot en gång per rad i tabellen. I step-filen skickas parametern vidare till en metod i `BasePage`, som returnerar 
rätt Playwright-locator. Därefter används `expect(...).to_be_visible()` för att verifiera att knappen visas.

Detta minskar dupliceringen av testkod och gör det enklare att lägga till fler exempel i framtiden.

#### Testmiljö och testlivscykel

I `environment.py` hanteras Playwrights livscykel med Behaves hooks. Webbläsaren startas före testkörningen, en ny sida skapas 
för varje scenario och resurserna stängs efteråt.

Följande hooks används:

- `before_all`: startar Playwright och webbläsaren inför testkörningen.
- `before_scenario`: skapar en ny sida (`page`) inför varje scenario och förbereder dess inställningar.
- `after_scenario`: stänger sidan när scenariot är klart.
- `after_all`: stänger webbläsaren och avslutar Playwright efter att alla scenarier har körts.

Genom att hantera webbläsarens livscykel på ett gemensamt ställe slipper jag upprepa samma uppstarts- och avslutningskod i varje 
step-funktion. Webbläsaren återanvänds under testkörningen, medan varje scenario får en egen sida.

#### Testsvitens omfattning och körning

Testerna är organiserade i separata feature-filer utifrån webbplatsens funktioner. Varje feature beskriver det förväntade beteendet 
med Gherkin, medan step-filerna kopplar stegen till Python-kod och Page Object-klasserna samlar sidornas locators och relaterade funktioner.

Testerna körs med Behave och synkron Playwright. Hela E2E-testsviten kan köras från projektets rotkatalog med kommandot `behave`. 
Resultatet visar hur många features, scenarier och steg som har passerat eller misslyckats.

## 🟡 CI-implementation

Continuous Integration (CI) har implementerats med GitHub Actions för att automatiskt kontrollera projektet när kod pushas till brancherna 
main eller dev, samt vid pull requests mot dessa brancher.

Arbetsflödet består av följande steg:

Miljöuppsättning: Hämtar projektets kod, installerar Python 3.14 och installerar beroenden från requirements.txt.

Kodkvalitet: Använder Flake8 för att identifiera kodstilproblem och potentiella fel i Python-koden.

Automatiserade tester: Kör enhets- och integrationstester med pytest, följt av BDD-scenarier med Behave.

Headless browser-testning: Installerar Chromium och kör Playwright-baserade webbläsartester i headless-läge, utan att ett 
grafiskt webbläsarfönster behöver visas.

Arbetsflödet avbryts om något steg misslyckas, vilket gör det enklare att identifiera problem tidigt. Resultatet av varje 
körning visas i GitHub Actions.

CI-lösningen har verifierats genom en lyckad körning där samtliga kontroller och testsviter passerade.




## 🟦 Start av tester

Jag har använt Pytest-markers för att separera körningen av enhets- och integrationstester.

### Enhetstester

```bash
pytest -m "unittest" -v
```

### Integrationstester

```bash
pytest -m "integrationtest" -v
```

### E2E-tester

E2E-testerna kan startas från projektets rotkatalog eftersom sökvägen till feature-filerna har konfigurerats i `behave.ini`.

```bash
behave
```

## Resultat

### Enhetstester

```text
tests/unit/test_book_store.py::test_book_store_add_book PASSED
tests/unit/test_book_store.py::test_book_store_toggle_favorite_adds_book PASSED
tests/unit/test_book_store.py::test_book_store_toggle_favorite_removes_book PASSED
tests/unit/test_fav_books.py::test_fav_books_add_book PASSED
tests/unit/test_fav_books.py::test_fav_books_remove_book PASSED
tests/unit/test_fav_books.py::test_fav_books_add_existing_book_does_not_add_duplicate PASSED
tests/unit/test_fav_books.py::test_fav_books_remove_non_existing_book PASSED
```

### Integrationstester

```text
tests/integration/test_book_store_fav_books.py::test_toggle_favorite_adds_book PASSED
tests/integration/test_book_store_fav_books.py::test_toggle_favorite_removes_book PASSED
```

### E2E-tester

```text
5 features passed, 0 failed, 0 skipped
24 scenarios passed, 0 failed, 0 skipped
90 steps passed, 0 failed, 0 skipped
```
![Lyckad CI-körning i GitHub Actions](images/ci_example.png)