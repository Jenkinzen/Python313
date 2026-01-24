import rezeptliste_services as service

neustart = True



def filter_auswaehlen():
    return input("Nach welchen Kriterien soll die Rezeptauswahl gefiltert werden?\n"
                 "[Zutaten]\noder\n[Gang]?\n").strip().lower()

def rezepte_ansehen_nach_gang():
    auswahl = input("Welchen Gang möchten sie wählen?\n")
    rezepte_nach_gang = service.filter_rezepte_nach_gang(auswahl)
    for zeile in service.zeige_rezeptname(rezepte_nach_gang):
        print(zeile)

def rezepte_ansehen_nach_zutat():
    auswahl = input("Welche Zutat(en) möchten sie wählen?\n")
    rezepte_nach_zutat = service.filter_rezepte_nach_zutaten(auswahl)
    for zeile in service.zeige_rezeptname(rezepte_nach_zutat):
        print(zeile)    

def rezepte_ansehen():
    while True:
        filterwahl = filter_auswaehlen()

        if filterwahl == "zutaten":
            rezepte_ansehen_nach_zutat()
            return
        
        elif filterwahl == "gang":
            rezepte_ansehen_nach_gang()
            return
        else:
            print("Ungültige Auswahl.")


def rezept_einfuegen():
    Rezeptname = input("Wie heißt das Rezept?")
    Rezeptzutaten = input("Welche Zutaten brauch es?( Zutaten bitte mit , trennen)")
    Rezeptzubereitung = input("Wie wird es zubereitet?")       
    Rezeptgang = None
    while Rezeptgang is None:
        eingabe = input("Ist es Vorspeise, Hauptspeise oder Dessert? ").strip().lower()
        if service.gang_pruefen(eingabe):
            Rezeptgang = eingabe
        else:
            print("Ungültige Auswahl! Bitte erneut eingeben.")                    
    neues_rezept = service.rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " ")
    service.rezept_hinzufuegen(neues_rezept)
    print("Rezept wurde eingefügt!")
    return

while neustart:

    Menueauswahl = input("""Möchten sie das Rezept 
[ansehen]              [einfügen]              [löschen]?
""")

    if Menueauswahl == "einfügen":

        rezept_einfuegen()




    elif Menueauswahl == "ansehen":

            rezepte_ansehen()





    elif Menueauswahl == "löschen":
        for zeile in service.alle_rezepte():
            print(zeile.Name)
        try:

            rezeptname = input("Welches Rezept soll gelöscht werden?")
            rezept_zum_loeschen = service.rezept_finden(rezeptname)

            if rezept_zum_loeschen is None:
                print("Rezept nicht gefunden.")
                continue

            rezept_zum_loeschen.anzeigen()
            rueckversichern = input(f"Sind sie sicher, dass {rezept_zum_loeschen.Name} gelöscht werden soll? Ja/Nein").strip().lower()
            if rueckversichern.strip().lower() == "ja":
                    service.rezept_loeschen(rezept_zum_loeschen)
                    print("Rezept wurde gelöscht!")
            else:
                print("Das Rezept wird nicht gelöscht.")
                continue

            break

        except ValueError:
            print("Ungültig!")

        
        


