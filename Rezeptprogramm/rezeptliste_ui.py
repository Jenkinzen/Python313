import rezeptliste_services as service
import rezeptliste_model as model
neustart = True



def filter_auswaehlen():
    return input("Nach welchen Kriterien soll die Rezeptauswahl gefiltert werden?\n"
                 "[Gerichte]\n[Zutaten]\noder\n[Gang]?\n").strip().lower()

def rezepte_ansehen_nach_gang():
    gang = input("Welchen Gang möchten Sie wählen?\n").strip().lower()
    rezepte = service.filter_rezepte_nach_gang(gang)

    if not rezepte:
        print("Keine Rezepte gefunden.")
        return

    
    for i, rezept in enumerate(rezepte, start=1):
        print(f"{i}. {rezept.name}")

    
    try:
        nummer = int(input("Nummer wählen:\n"))
        rezept = service.rezept_nach_index(rezepte, nummer)

        if rezept is None:
            print("Ungültige Nummer.")
            return

        for zeile in rezept.anzeigen():
            print(zeile)

    except ValueError:
        print("Bitte eine Zahl eingeben.")

def rezepte_ansehen_nach_zutaten():
    zutat = [z.strip() for z in input("Welche Zutat(en) möchten Sie wählen?\nBitte Zutaten mit , trennen.\n").strip().lower().split(",")]
    rezepte = service.filter_rezepte_nach_zutaten(zutat)

    if not rezepte:
        print("Keine Rezepte gefunden.")
        return

    for i, rezept in enumerate(rezepte, start=1):
        print(f"{i}. {rezept.name}")

    try:
        nummer = int(input("Nummer wählen:\n"))
        rezept = service.rezept_nach_index(rezepte, nummer)

        if rezept is None:
            print("Ungültige Nummer.")
            return

        for zeile in rezept.anzeigen():
            print(zeile)

    except ValueError:
        print("Bitte eine Zahl eingeben.")   

def rezepte_ansehen_nach_Gericht():
    for i, rezept in enumerate(service.alle_rezeptnamen(), start=1):
        print(f"{i}. {rezept}")
    
    gerichte = service.filter_rezepte_nach_gericht("")
    nummer = int(input("Wählen sie bitte die Nummer des Gerichtes:\n"))
    rezepte = service.rezept_nach_index(gerichte,nummer)

    if not rezepte:
        print("Keine Rezepte gefunden.")
        return

    
    for zeile in rezepte.anzeigen():
        print(zeile)




def rezepte_ansehen():
    while True:
        filterwahl = filter_auswaehlen()

        if filterwahl == "zutaten":
            rezepte_ansehen_nach_zutaten()
            return
        
        elif filterwahl == "gang":
            rezepte_ansehen_nach_gang()
            return
        
        elif filterwahl == "gerichte":
            rezepte_ansehen_nach_Gericht()
            return
        
        else:
            print("Ungültige Auswahl.")

def rezept_einfuegen():
    Rezeptname = input("Wie heißt das Rezept?")
    zutaten_input = input("Welche Zutaten brauch es?( Zutaten bitte mit , trennen[z.B. Enokis 200 g, Salz 2 Prise])")
    Rezeptzubereitung = input("Wie wird es zubereitet?") 

    Rezeptgang = None
    while Rezeptgang is None:
        eingabe = input("Ist es Vorspeise, Hauptspeise oder Dessert? ").strip().lower()
        if service.gang_pruefen(eingabe):
            Rezeptgang = eingabe
        else:
            print("Ungültige Auswahl! Bitte erneut eingeben.") 

    Zutatenliste = []
    for z in zutaten_input.split(","):
        parts = z.strip().split(" ")
        if len(parts) >= 3:
            name = " ".join(parts[:-2])
            menge = parts[-2]
            einheit = parts[-1]
        elif len(parts) == 2:
            name = parts[0]
            menge = parts[1]
            einheit = ""
        else:
            name = parts[0]
            menge = None
            einheit = ""
        Zutatenliste.append(model.Zutaten(name, menge, einheit))

    neues_rezept = model.Rezept(
        name=Rezeptname,
        zutaten=Zutatenliste,
        zubereitung=Rezeptzubereitung,
        notizen="",
        gang=Rezeptgang.title()
    )
    service.rezept_hinzufuegen(neues_rezept)
    print(f"{neues_rezept} wurde eingefügt!")
    return

def rezept_loeschen():
        for zeile in service.alle_rezepte():
            print(zeile.name)
        try:

            rezeptname = input("Welches Rezept soll gelöscht werden?")
            rezept_zum_loeschen = service.rezept_finden(rezeptname)

            if rezept_zum_loeschen is None:
                print("Rezept nicht gefunden.")
                return

            rezept_zum_loeschen.anzeigen()
            rueckversichern = input(f"Sind sie sicher, dass {rezept_zum_loeschen.name} gelöscht werden soll? Ja/Nein").strip().lower()
            if rueckversichern.strip().lower() == "ja":
                    service.rezept_loeschen(rezept_zum_loeschen)
                    print(f"{rezept_zum_loeschen} wurde gelöscht!")
            else:
                print(f"Das {rezept_zum_loeschen} wird nicht gelöscht.")
                return

        except ValueError:
            print("Ungültig!")



while neustart:

    Menueauswahl = input("""Möchten sie ein Rezept 
[ansehen]              [einfügen]              [löschen]?
""")

    if Menueauswahl == "einfügen":

        rezept_einfuegen()




    elif Menueauswahl == "ansehen":

            rezepte_ansehen()





    elif Menueauswahl == "löschen":
        
        rezept_loeschen()
        
        


