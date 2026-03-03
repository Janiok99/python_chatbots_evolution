x = input("Podaj swoje imię:")
print("Podane przez Ciebie imię to:", x)
y = (input("Czy to na prawdę twoje imię? Odpisz mi: Tak/Nie:"))

if y == "Tak":
    print("Cieszę się, że podałeś prawdziwe imię.")
elif y == "Nie":
    print("Bardzo mi przykro, że zostałem oszukany.")
else:
    print("Hej, nie odpowiadasz na moje pytanie, tak jak proszę.")
