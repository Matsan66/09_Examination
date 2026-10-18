# noinspection CucumberUndefinedStep


  Feature: Funktioner i vyn Mina böcker
    Scenario: Kontrollera att vyn Mina böcker visas korrekt
      Given att jag är på startsidan
      When jag klickar på knappen "Mina böcker"
      Then ska vyn för Mina böcker visas


    Scenario: Kontrollera att ett meddelande visas när listan är tom
      Given att jag är på startsidan
      And inga böcker är valda som favoriter
      When jag klickar på knappen "Mina böcker"
      Then ska meddelandet ”När du valt, kommer dina favoritböcker att visas här.” visas


  Scenario: Kontrollera att en bok som markeras som favorit listas i Mina böcker
      Given att jag är på startsidan
      When jag klickar på favoritknappen på en bok
      And jag klickar på knappen "Mina böcker"
      Then ska den valda boken visas i Mina böckers boklista


    Scenario: Kontrollera att en bok som avmarkeras som favorit tas bort från listan i Mina böcker
    Given att jag är på startsidan
    When jag klickar på favoritknappen på en bok
    And jag klickar på favoritknappen på den favoritmarkerade boken
    And jag klickar på knappen "Mina böcker"
    Then ska den avmarkerade boken inte visas i Mina böckers boklista
