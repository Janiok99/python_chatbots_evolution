# Ewolucja prostego chatbota w Pythonie (v1 → v4)

    To repozytorium przedstawia cztery kolejne wersje prostego chatbota napisanego w Pythonie.  
    Każda wersja rozwija funkcjonalności poprzedniej, pokazując krok po kroku, jak chatbot może stawać się coraz bardziej interaktywny, elastyczny i naturalny w rozmowie.

    Repozytorium ma charakter edukacyjny i prezentuje proces stopniowego ulepszania logiki rozmowy, obsługi użytkownika oraz zarządzania kontekstem.

## Struktura repozytorium

    /README.md
    /v1
    v1_basic_chatbot.py
    README.md
    /v2
    v2_extended_chatbot.py
    README.md
    /v3
    v3_keyword_chatbot.py
    README.md
    /v4
    v4_advanced_keyword_chatbot.py
    README.md

## Opis wersji

### v1 – Podstawy interakcji
    Najprostsza wersja chatbota.  
    Bot pyta o imię i reaguje na odpowiedź użytkownika.  
    Brak pętli rozmowy, brak słów kluczowych, brak kontekstu.

### v2 – Rozszerzona rozmowa
    Bot zadaje więcej pytań: o samopoczucie oraz o zainteresowanie Gwiezdnymi Wojnami.  
    Pojawiają się pierwsze rozgałęzienia dialogu, ale nadal brak pętli i kontekstu.

### v3 – Chatbot oparty na słowach kluczowych
    Pierwsza wersja działająca w pętli.  
    Bot reaguje na słowa kluczowe (powitania, pytania o samopoczucie, Gwiezdne Wojny).  
    Pojawia się podstawowa forma „rozmowy”, ale bez pamięci kontekstu.

### v4 – Zaawansowany chatbot z kontekstem
    Najbardziej rozbudowana wersja.  
    Bot rozpoznaje kategorie wypowiedzi, zapamiętuje kontekst rozmowy i udziela odpowiedzi zależnych od poprzednich wiadomości.  
    Wprowadza subtelną odpowiedź domyślną, gdy nie zna tematu.

## Jak uruchomić dowolną wersję

    1. Wejdź do folderu wybranej wersji, np.:
        cd v3
    2. Uruchom plik:
        python v3_keyword_chatbot.py
    3. Aby zakończyć rozmowę, wpisz:
        koniec

## Cel projektu

    Repozytorium pokazuje, jak stopniowo rozwijać prostego chatbota:

        1. od pojedynczych pytań,
        2. przez rozbudowane dialogi,
        3. po obsługę słów kluczowych,
        4. aż do zarządzania kontekstem rozmowy.

    Każda wersja jest samodzielna i może być uruchomiona niezależnie.
