import rezeptliste_services as service
import rezeptliste_model as model

neustart = True
while neustart:

    Menueauswahl = input("Möchten sie ein Rezept [einfügen], [ansehen] oder [löschen]?")

    if Menueauswahl == "einfügen":

        Rezeptname = input("Wie heißt das Rezept?")
        Rezeptzutaten = input("Welche Zutaten brauch es?( Zutaten bitte mit , trennen)")
        Rezeptzubereitung = input("Wie wird es zubereitet?")       
        Rezeptgang = None
        while Rezeptgang is None:
            eingabe = input("Ist es Vorspeise, Hauptspeise oder Dessert? ").strip().lower()
            if eingabe in model.gueltige_gaenge:
                Rezeptgang = eingabe
            else:
                print("Ungültige Auswahl! Bitte erneut eingeben.")                    
        neues_rezept = service.rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " ")
        service.rezept_hinzufuegen(neues_rezept)
        print("Rezept wurde eingefügt!")
        continue

    elif Menueauswahl == "ansehen":
        while True:
            wahl = input("Möchten sie Vorspeise, Hauptspeise oder ein Dessert zubereiten?")
            
            if not service.gang_validieren(model.Gerichte,wahl):
                print("Ungültige Auswahl.")
                continue

            passende_rezepte = service.geb_rezepte_nach_gang(wahl)
            break 


        try:
            auswahl = int(input("Nummer wählen:"))
            rezept = service.rezept_nach_index(passende_rezepte, auswahl)
            
            

            if rezept is None:
                print("Ungültige Nummer.")
                continue
            
            rezept.anzeigen()
            
            continue

        except ValueError:
            print("Bitte eine Zahl eingeben.")

        

    elif Menueauswahl == "löschen":
        print([v.Name for v in model.Gerichte])
        try:

            rezeptname = input("Welches Rezept soll gelöscht werden?")
            rezept_zum_loeschen = service.rezept_finden(model.Gerichte, rezeptname)

            if rezept_zum_loeschen is None:
                print("Rezept nicht gefunden.")
                continue

            rezept_zum_loeschen.anzeigen()
            rueckversichern = input(f"Sind sie sicher, dass {rezept_zum_loeschen.Name} gelöscht werden soll? Ja/Nein").strip().lower()
            if rueckversichern.strip().lower() == "ja":
                    service.rezept_loeschen(model.Gerichte,rezept_zum_loeschen)
                    print("Rezept wurde gelöscht!")
            else:
                print("Das Rezept wird nicht gelöscht.")
                continue

            break

        except ValueError:
            print("Ungültig!")

        
        


