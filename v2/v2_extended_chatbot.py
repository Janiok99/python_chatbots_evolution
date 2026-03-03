x = input("Podaj proszę swoje imię abyśmy mogli się poznać:")
print("Witaj, miło mi Cię poznać", x)
y = input("Jak się dzisiaj czujesz? dobrze/kiepsko/źle:").lower()

if y == "dobrze":
    print("bardzo mnie to cieszy.")
elif y == "kiepsko":
    print("Rozumiem, może jutro będzie lepiej.")
elif y == "źle":
    print("Bardzo mi przykro.")

z = input("Czy lubisz uniwersum Gwiezdnych Wojen? Odpowiedz tak/nie:").lower()

if z == "tak":
    print("Super!, Też uwielbiam to uniwersum.")

    postac = input("A jaka jest Twoja ulubiona postać? ")
    print("Świetny wybór! " + postac + " to naprawdę ciekawa postać.")

elif z == "nie":
    print("Rozumiem, nie każdy musi lubić kosmiczne przygody.")
