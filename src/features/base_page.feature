# noinspection CucumberUndefinedStep

# User story
# Som en användare
# vill jag tydligt se sidans huvudrubrik
# så att jag vet att jag är på rätt sida


Feature: Läslistans gemensamma gränssnitt

  Scenario: Kontrollera huvudrubrik
    Given att jag är på startsidan
    Then ska huvudrubriken "Läslistan" synas


#  Som en användare
# vill jag mötas av en välkomsthälsning på startsidan
# så att startsidan känns välkomnande.

    Scenario: Kontrollera välkomstrubrik
    Given att jag är på startsidan
    Then ska rubriken "Välkommen!" synas


# Som en användare
# vill jag se sidans knappar för navigation
# så att jag vet vad jag kan göra på sidan

  Scenario Outline: Navigeringsknapparna visas på startsidan
    Given att jag är på startsidan
    Then ska knappen "<button_name>" visas

    Examples:
    | button_name |
    | catalog     |
    | add-book    |
    | favorites   |
    | statistics  |




