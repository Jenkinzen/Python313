import rezeptliste_services as service
import rezeptliste_model as model
neustart = True

def filter_auswaehlen():
    return input("Nach welchen Kriterien soll die Rezeptauswahl gefiltert werden?\n"
                 "[Gerichte]\n[Zutaten]\noder\n[Gang]?\n").strip().lower()

def rezepte_ansehen_nach_gang():
    while True:
        gangeingabe = input("Welchen Gang möchten Sie wählen?\n").strip().lower()
        rezepte = service.filter_rezepte_nach_gang(gangeingabe)

        if not rezepte:
            print("Keine Rezepte gefunden.")
            continue

        
        for i, rezept in enumerate(rezepte, start=1):
            print(f"{i}. {rezept.name}")

        while True:
            try:
                nummer = int(input("Nummer wählen:\n"))
                rezept = service.rezept_nach_index(rezepte, nummer)

                if rezept is None:
                    print("Ungültige Nummer.")
                    continue

                for zeile in rezept.anzeigen():
                    print(zeile)

                break

            except ValueError:
                print("Bitte eine Zahl eingeben.")

def rezepte_ansehen_nach_zutaten():
    while True:
        zutat = [z.strip() for z in input("Welche Zutat(en) möchten Sie wählen?\nBitte Zutaten mit , trennen.\n").strip().lower().split(",")]
        rezepte = service.filter_rezepte_nach_zutaten(zutat)

        if not rezepte:
            print("Keine Rezepte gefunden.")
            continue    

        for i, rezept in enumerate(rezepte, start=1):
            print(f"{i}. {rezept.name}")

        while True:

            try:
                nummer = int(input("Nummer wählen:\n"))
                rezept = service.rezept_nach_index(rezepte, nummer)

                if rezept is None:
                    print("Ungültige Nummer.")
                    continue

                for zeile in rezept.anzeigen():
                    print(zeile)
                    #wenn hier break stehen würde bricht er print(zeile) 
                    #nach der ersten zeile ab ( also printet nur namen aber nicht zutaten,zubereitung etc.)
                break    

            except ValueError:
                print("Bitte eine Zahl eingeben.")  
                #hier brauch man kein continue weil die Schleife hier eh endet und dann wieder anfängt
            
                

def rezepte_ansehen_nach_Gericht():
    for i, rezept in enumerate(service.alle_rezeptnamen(), start=1):
        print(f"{i}. {rezept}")
    while True:
        gerichte = service.filter_rezepte_nach_gericht("")
        nummer = int(input("Wählen sie bitte die Nummer des Gerichtes:\n"))
        if nummer > len(gerichte):
            print("Falsche Zahl eingegeben!")
            continue
        rezepte = service.rezept_nach_index(gerichte,nummer)

        if not rezepte:
            print("Kein Rezept passt zu diesen Angaben.")
            continue

        
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
    rezeptname = input("Wie heißt das Rezept?").strip()
    zutaten_input = input("Welche Zutaten in welcher Menge brauch es?( Zutaten bitte mit , trennen[z.B. Enokis 200 g, Salz 2 Prise])")
    zutaten_strings = [z.strip() for z in zutaten_input.split(",")if z.strip()]
    zubereitung = input("Wie wird es zubereitet?") 
    notizen = input("Notizen oder Tipps")
    gangeingabe = None
    while gangeingabe is None:
        eingabe = input("Ist es Vorspeise, Hauptspeise oder Dessert? ").strip().lower()
        if service.gang_pruefen(eingabe):
                gangeingabe = eingabe
        else:
            print("Ungültige Auswahl! Bitte erneut eingeben.") 

    rezept = service.rezepterstellung(rezeptname, zutaten_strings, zubereitung,gangeingabe,notizen)
    
    print(f"{rezept} wurde eingefügt!")
    return

def rezept_loeschen():
        for i, rezept in enumerate(service.alle_rezeptnamen(), start=1):
            print(f"{i}. {rezept}")
        
        while True:
            try:
                gerichte = service.alle_rezepte()
                nummer = int(input("Welche Nummer soll gelöscht werden?"))

                if nummer > len(service.alle_rezepte()):  
                # eigentlich wäre es klüger len(gerichte) zu nutzen weil sonst alle_rezepte 2 mal aufgerufen wird aber für jetzt
                # ist es für mich ein beispiel der Möglichkeiten und für meine Noob-Coder Augen verständlicher herauszulesen.               
                    print("Ungültige Auswahl!")                             
                    continue
                
                rezept_zum_loeschen = service.rezept_nach_index(gerichte,nummer)

                if rezept_zum_loeschen is None:
                    print("Rezept nicht gefunden.")
                    return

                for zeile in rezept_zum_loeschen.anzeigen():
                    print(zeile)
                rueckversichern = input(f"Sind sie sicher, dass {rezept_zum_loeschen.name} gelöscht werden soll? Ja/Nein").strip().lower()
                if rueckversichern.strip().lower() == "ja":
                        service.rezept_loeschen(rezept_zum_loeschen)
                        print(f"{rezept_zum_loeschen} wurde gelöscht!")
                        return
                else:
                    print(f"Das {rezept_zum_loeschen} wird nicht gelöscht.")
                    break

            except ValueError:
                print("Ungültig!")

service.rezept_laden()

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
        
        


