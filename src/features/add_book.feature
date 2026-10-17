# noinspection CucumberUndefinedStep

# User story
# Som en användare
# vill jag kunna klicka på knappen "Lägg till bok"
# så att jag kommer till vyn för att lägga till en bok


  Feature: Funktioner i vyn Lägg till bok

  Scenario: Kontrollera att vyn Lägg till bok visas korrekt
    Given att jag är på startsidan
    When jag klickar på knappen "Lägg till bok"
    Then ska formuläret för att lägga till en bok visas
    And textfältet titel visas
    And textfältet författare visas


# User story
# Som en användare
# vill jag kunna aktivera knappen ”Lägg till ny bok” när jag fyllt i formuläret
# så att jag kan lägga till boken.

  Scenario: Kontrollera att knappen "Lägg till ny bok" aktiveras
    Given att jag är i vyn för att lägga till en ny bok
    When jag fyller i textfältet titel med "testbok"
    Then ska knappen ”Lägg till ny bok” förbli inaktiverad
    When jag fyller i textfältet författare med "John Doe"
    Then ska knappen ”Lägg till ny bok” aktiveras



# User story
# Som en användare
# vill jag kunna lägga till en ny bok
# så att jag kan se den i katalogen

  Scenario: Kontrollera att en ny bok läggs till i katalogen
    Given att jag är i vyn för att lägga till en ny bok
    When jag fyllt i formuläret med titel "testbok" och författare "John Doe"
    And jag klickar på knappen "Lägg till ny bok"
    Then ska formuläret tömmas
    And knappen "Lägg till ny bok" deaktiveras
    When jag klickar på knappen "Katalog"
    Then den nya boken visas i katalogen med rätt titel och författare
