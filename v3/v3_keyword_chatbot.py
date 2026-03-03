print("Cześć! Jestem prostym chatbotem. Napisz coś do mnie!")
print("Aby zakończyć rozmowę, wpisz: koniec")

while True:
    user = input("Ty: ").lower()

    if user == "koniec":
        print("Bot: Miło było z Tobą porozmawiać. Do zobaczenia!")
        break

    if "hej" in user or "cześć" in user:
        print("Bot: Hej! Jak mogę Ci pomóc?")
    elif "jak się masz" in user:
        print("Bot: Mam się świetnie, dzięki że pytasz.")
    elif "gwiezdne wojny" in user:
        print("Bot: Uwielbiam to uniwersum! A Ty?")
    else:
        print("Bot: Hm… jeszcze nie znam odpowiedzi na to, ale uczę się każdego dnia!")
