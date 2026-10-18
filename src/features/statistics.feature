# noinspection CucumberUndefinedStep


  Feature: Funktioner i vyn Statistik

  Scenario: Kontrollera att det går att navigera till statistikvyn
    Given att jag är på startsidan
    When jag klickar på knappen "Statistik"
    Then ska vyn för statistik visas


  Scenario: Kontrollera att statistiksidan visar antal böcker
    Given att jag är på startsidan
    When jag klickar på knappen "Statistik"
    Then ska texten med antalet böcker visas


  Scenario: Kontrollera att statistiksidan visar antal böcker som favoritmarkerats av användarna
    Given att jag är på startsidan
    When jag klickar på knappen "Statistik"
    Then ska texten med antalet hjärtmarkerade böcker visas


  Scenario: Kontrollera att statistiksidan visar samma antal böcker som katalogen efter att en bok lagts till
    Given att jag är i vyn för att lägga till en ny bok
    When jag fyllt i formuläret med titel "testbok" och författare "John Doe"
    And jag klickar på knappen "Lägg till ny bok"
    And jag klickar på knappen "Katalog"
    And jag kontrollerar antal böcker i katalogen
    And jag klickar på knappen "Statistik"
    Then ska antalet böcker som visas överensstämma med antalet i katalogen


  Scenario: Kontrollera att statistiksidan visar samma antal hjärtmarkerade böcker som Mina böcker efter att en favorit lagts till
    Given att jag är på startsidan
    When jag klickar på hjärt-ikonen för en bok
    And jag klickar på knappen "Mina böcker"
    And jag kontrollerar antal favoritböcker
    And jag klickar på knappen "Statistik"
    Then ska antalet favoriter som visas överensstämma med antalet i Mina böcker


