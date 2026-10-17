# 📊 Examinationsuppgift
## Testautomatisering och testverktyg

## 🟦Vad är testat

### 🟠 Enhetstester
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

### 🟣 Integrationstester
Filen test_book_store_fav_books.py innehåller nedanstående integrationstester för att verifiera 
BookStores och FavoriteBooks interaktion då en bok läggs till eller tas bort från favoritlistan.

1. test_toggle_favorite_adds_book
2. test_toggle_favorite_removes_book


### ⚪ E2E tester med Gherkin, Behave och PlayWright

### Teststrategi och struktur
Jag har använt Gherkin för att beskriva testerna och specificera vad som ska verifieras. Jag har använt Behave för att läsa mina 
.feature-filer och koppla stegen i dessa till Python-funktioner i så kallade stepfiler. Slutligen har jag använt Playwright för 
att styra webbläsaren, hitta element på webbsidan och kontrollera att de uppfyller testernas förväntningar.

Jag har valt att dela upp verifieringen av Läslistan i fem logiska delar. Den första delen omfattar sidans gemensamma gränssnitt, 
medan de övriga fyra fokuserar på funktionaliteten bakom respektive navigeringsknapp.

De fem delarna är:
1. Sidans gemensamma gränssnitt: Kontroll av huvudrubriken, välkomstrubrik och de fyra navigeringsknapparnas synlighet. 
2. Katalog: Verifiering av funktionaliteten bakom knappen ”Katalog”. 
3. Lägg till bok: Verifiering av funktionaliteten bakom knappen ”Lägg till bok”. 
4. Mina böcker: Verifiering av funktionaliteten bakom knappen ”Mina böcker”. 
5. Statistik: Verifiering av funktionaliteten bakom knappen ”Statistik”.

### Kodstruktur och genomförande
##### Page Object Model (POM)

Testerna är uppbyggda enligt Page Object Model (POM), vilket innebär att sidornas element och locators samlas i separata klasser. 
Detta skiljer beskrivningen av sidornas struktur från teststegen och gör koden lättare att underhålla och återanvända.

##### BasePage

Klassen BasePage representerar Läslistans gemensamma gränssnitt. Den innehåller locators för huvudrubriken, välkomstrubriken 
och navigeringsknapparna till Katalog, Lägg till bok, Mina böcker och Statistik. Klassen innehåller även en metod för att 
navigera till webbplatsen.

I base_page.feature verifieras att rubrikerna visas och att navigeringsknapparna är synliga. För kontrollen av navigeringsknapparna 
används Scenario Outline med Examples, vilket gör att samma scenario kan återanvändas för flera knappar.

##### CatalogPage

Klassen CatalogPage innehåller locators för katalogens beskrivning, boklistan, enskilda böcker och favoritknapparna. Locatorn .book 
används för att identifiera böckerna i katalogen, medan .star används för favoritknapparna.

I catalog.feature finns scenarier som verifierar att katalogen visas vid navigation, att minst en bok finns i listan och att 
alla identifierade böcker är synliga. Därutöver testas att en bok kan markeras som favorit och att favoritmarkeringen kan tas bort.

För att kontrollera flera böcker används count() och nth(i). Playwrights expect() används för att verifiera synlighet och CSS-klasser.

##### AddBookPage

Klassen AddBookPage representerar vyn Lägg till bok. Den innehåller locators för formuläret, titelfältet, författarfältet och knappen 
Lägg till ny bok. Locators hämtas med hjälp av sidans test-id där sådana finns.

I add_book.feature testas först att vyn visas korrekt efter navigation. Testet verifierar att formuläret och både titel- och författarfältet 
är synliga.

Ett separat scenario testar knappens aktivering. När endast titeln har fyllts i ska knappen vara inaktiverad. När även författaren har 
fyllts i ska knappen aktiveras.

Ytterligare ett scenario testar hela flödet för att lägga till en bok. Testet fyller i titel och författare, klickar på knappen och 
verifierar att formuläret töms och att knappen åter blir inaktiverad. Därefter navigerar testet till katalogen och kontrollerar att den nya boken visas med rätt titel och författare.

##### Gemensamma hjälpfunktioner

I helpers.py finns funktionerna get_base_page(context), get_catalog_page(context) och get_add_book_page(context). De skapar 
respektive Page Object vid behov och återanvänder objektet under det aktuella scenariot. På så sätt undviks onödig duplicering 
av kod och initialisering.

Step-filerna importerar de hjälpfunktioner de behöver från helpers.py. Detta gör att stegen kan återanvändas mellan olika features 
utan att samma stegdefinition behöver implementeras flera gånger.

##### Testmiljö och körning

I environment.py hanteras Playwrights livscykel med Behaves hooks. Webbläsaren startas före testkörningen, en ny sida skapas 
för varje scenario och resurserna stängs efteråt. Testerna körs med Behave och synkron Playwright.

Testsviten är organiserad i separata feature-filer för det gemensamma gränssnittet, katalogen och vyn Lägg till bok. Detta gör 
det möjligt att utveckla och underhålla testerna per funktion samtidigt som hela testsviten kan köras gemensamt med kommandot behave.


#### Scenario Outline och Examples
För att verifiera att alla fyra navigeringsknappar visas har jag använt Scenario Outline i Gherkin tillsammans med en Examples-tabell.

I stället för att skriva ett separat scenario för varje knapp använder jag en parameter, button_name, vars värde hämtas från tabellen. 
Tabellen innehåller de fyra knapparnas test-id:n: catalog, add-book, favorites och statistics.

Behave kör scenariot en gång för varje rad i tabellen. Det innebär att samma stegdefinition kan användas för att verifiera samtliga 
fyra knappar.

I stepfilen tar Python-funktionen emot parametern button_name och skickar den vidare till en metod i BasePage. Metoden returnerar 
rätt Playwright-locator, som sedan kontrolleras med expect(...).to_be_visible().

Detta minskar dupliceringen av testkod och gör det enklare att lägga till fler exempel i framtiden.

###  Environment och testlivscykeln
Jag använder environment.py för att hantera den gemensamma uppstarten och avslutningen av testerna. Där kan Behave anropa särskilda 
funktioner vid olika tidpunkter under testkörningen.

before_all: startar Playwright och webbläsaren inför testkörningen.  
before_scenario: skapar en ny sida (page) inför varje scenario och förbereder dess inställningar.   
after_scenario: stänger sidan när scenariot är klart.   
after_all: stänger webbläsaren och avslutar Playwright efter att alla scenarier har körts.

Genom att hantera webbläsarens livscykel på ett gemensamt ställe slipper jag upprepa samma uppstarts- och avslutningskod i 
varje stepfunktion. Varje scenario får en egen sida, medan webbläsaren kan återanvändas under hela testkörningen.


## 🟦Start av tester
Jag har använt Pytest markers för att separera exekvering av enhets- och intergrationstester.
### Enhetstester
```
pytest -m "unittest" -v
```
### Integrationstester
```
pytest -m "integrationtest" -v
```

### E2E-tester
Mina E2E tester kan startas från projektets root då jag lagt till sökvägen i behave.ini.

```
behave
```