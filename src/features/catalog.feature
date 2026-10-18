# noinspection CucumberUndefinedStep


  Feature: Funktioner i vyn Katalog

  Scenario: Kontrollera navigation till vyn och dess rubrik
    Given att jag är på startsidan
    And en annan vy än "Katalog" är vald
    When jag klickar på knappen "Katalog"
    Then ska rubriken "Sidan för dig som gillar att läsa. Välj dina favoriter." visas
    And listan med böcker ska visas


  Scenario: Kontrollera att det finns böcker i boklistan
    Given att jag är på startsidan
    Then ska minst en bok visas i boklistan


  Scenario: Kontrollera att alla böcker i katalogen visas
    Given att jag är på startsidan
    Then ska alla böcker i katalogen visas


  Scenario: Kontrollera att det går att favoritmarkera en bok
    Given att jag är på startsidan
    When jag klickar på hjärt-ikonen för en bok
    Then ska boken markeras som favorit


  Scenario: Kontrollera att det går att ta bort en favoritmarkerad bok
    Given att jag är på startsidan
    And en bok är markerad som favorit
    When jag klickar på hjärt-ikonen för en favoritmarkerad bok
    Then ska boken inte längre vara markerad som favorit