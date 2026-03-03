print("Cześć! Jestem prostym chatbotem. Napisz coś do mnie!")
print("Aby zakończyć rozmowę, wpisz: koniec")
print("\nJeśli nie wiesz od czego zacząć, możesz:")
print("- przywitać się,")
print("- zapytać jak się mam,")
print("- powiedzieć jak się czujesz,")
print("- porozmawiać o Gwiezdnych Wojnach.\n")

powitania = ["hej", "cześć", "siema", "witaj", "elo"]
humor = ["jak się masz", "co słychać", "jak tam", "jak leci", "co tam"]
emocje_pozytywne = ["dobrze", "super", "świetnie", "fantastycznie"]
emocje_negatywne = ["źle", "kiepsko", "smutno", "fatalnie", "tak sobie"]
star_wars = ["gwiezdne wojny", "star wars", "skywalker", "vader", "mandalorian"]
pozegnania = ["pa", "do widzenia", "nara", "trzymaj się"]

current_topic = None  # zapamiętuje, o czym rozmawiacie

while True:
    user = input("Ty: ").lower()

    if user == "koniec":
        print("Bot: Miło było z Tobą porozmawiać. Do zobaczenia!")
        break

    # Powitania
    if any(word in user for word in powitania):
        print("Bot: Hej! Miło Cię widzieć. Jak się dzisiaj czujesz?")
        current_topic = "mood"

    # Pytania o samopoczucie
    elif any(word in user for word in humor):
        print("Bot: Mam się świetnie, dzięki że pytasz! A jak Ty się czujesz?")
        current_topic = "mood"

    # Emocje pozytywne
    elif any(word in user for word in emocje_pozytywne):
        print("Bot: Super, bardzo się cieszę! Co takiego sprawiło, że masz dobry humor?")
        current_topic = "positive"

    # Emocje negatywne
    elif any(word in user for word in emocje_negatywne):
        print("Bot: Przykro mi to słyszeć. Może skupmy się na czymś przyjemniejszym")
        current_topic = "negative"

    # Gwiezdne Wojny
    elif any(word in user for word in star_wars):
        print("Bot: Uwielbiam to uniwersum! Masz ulubioną postać?")
        current_topic = "star_wars"

    # Pożegnania
    elif any(word in user for word in pozegnania):
        print("Bot: Trzymaj się! Mam nadzieję, że jeszcze pogadamy.")
        current_topic = None

    # Reakcje zależne od kontekstu
    elif current_topic == "positive":
        print("Bot: Brzmi świetnie! Cieszę się, że dzięki temu masz dobry dzień.")
        current_topic = None

    elif current_topic == "negative":
        print("Bot: Jasne, powiedz o czym chcesz pogadać?")
        current_topic = None

    elif current_topic == "star_wars":
        print("Bot: Świetny wybór! Ta postać naprawdę ma coś w sobie.")
        current_topic = None

    elif current_topic == "mood":
        print("Bot: Dzięki za odpowiedź! O czym chcesz teraz pogadać?")
        current_topic = None

    # Odpowiedź domyślna
    else:
        print("Bot: To brzmi ciekawie, choć nie znam się na tym. Wybierzmy może inny temat.")
