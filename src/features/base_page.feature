# noinspection CucumberUndefinedStep

Feature: Läslistans gemensamma gränssnitt

  Scenario: Kontrollera huvudrubrik
    Given att jag är på startsidan
    Then ska huvudrubriken "Läslistan" synas


    Scenario: Kontrollera välkomstrubrik
    Given att jag är på startsidan
    Then ska rubriken "Välkommen!" synas


  Scenario Outline: Navigeringsknapparna visas på startsidan
    Given att jag är på startsidan
    Then ska knappen "<button_name>" visas

    Examples:
    | button_name |
    | catalog     |
    | add-book    |
    | favorites   |
    | statistics  |
