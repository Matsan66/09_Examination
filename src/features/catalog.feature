# noinspection CucumberUndefinedStep

# User story
# Som en användare
# vill jag kunna öppna vyn katalog och se dess rubrik
# så att jag vet att jag navigerat rätt och kan utforska böckerna


  Feature: Funktioner i vyn Katalog

  Scenario: Kontrollera navigation till vyn och dess rubrik
    Given att jag är på startsidan
    And en annan vy än "Katalog" är vald
    When jag klickar på knappen "Katalog"
    Then ska rubriken "Sidan för dig som gillar att läsa. Välj dina favoriter." visas
    And listan med böcker ska visas


# User story
# Som en användare
# vill jag förvissa mig om att det finns böcker i katalogen
# så att jag vet att listan inte är tom

  Scenario: Kontrollera att det finns böcker i boklistan
    Given att jag är på startsidan
    Then ska minst en bok visas i boklistan


# User story
# Som en användare
# vill jag kunna se alla böcker i katalogen
# så att jag kan utforska vilka böcker som finns tillgängliga

  Scenario: Kontrollera att alla böcker i katalogen visas
    Given att jag är på startsidan
    Then ska alla böcker i katalogen visas


# User story
# Som en användare
# vill jag kunna markera en bok som favorit
# så att jag kan markera de böcker jag tycker om

  Scenario: Kontrollera att det går att favoritmarkera en bok
    Given att jag är på startsidan
    When jag klickar på hjärt-ikonen för en bok
    Then ska boken markeras som favorit


# User story
# Som en användare
# vill jag kunna ta bort en bok från mina favoriter
# så att jag kan ändra vilka böcker jag tycker om

  Scenario: Kontrollera att det går att ta bort en favoritmarkerad bok
    Given att jag är på startsidan
    And en bok är markerad som favorit
    When jag klickar på hjärt-ikonen för en favoritmarkerad bok
    Then ska boken inte längre vara markerad som favorit