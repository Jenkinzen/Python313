import rezeptliste_services as service
import rezeptliste_storage as storage

neustart = True
while neustart:

    Menueauswahl = input("""Möchten sie das Rezept 
[ansehen]              [einfügen]              [löschen]?
""")

    if Menueauswahl == "einfügen":

        Rezeptname = input("Wie heißt das Rezept?")
        Rezeptzutaten = input("Welche Zutaten brauch es?( Zutaten bitte mit , trennen)")
        Rezeptzubereitung = input("Wie wird es zubereitet?")       
        Rezeptgang = None
        while Rezeptgang is None:
            eingabe = input("Ist es Vorspeise, Hauptspeise oder Dessert? ").strip().lower()
            if eingabe in storage.gueltige_gaenge:
                Rezeptgang = eingabe
            else:
                print("Ungültige Auswahl! Bitte erneut eingeben.")                    
        neues_rezept = service.rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " ")
        service.rezept_hinzufuegen(neues_rezept)
        print("Rezept wurde eingefügt!")
        continue





    elif Menueauswahl == "ansehen":
        while True:

            filter_auswahl = input("""Nach welchen Kriterien soll die Rezeptauswahl gefiltert werden,
        [Zutaten]                        [Gang]?
""").strip().lower()
            

            if filter_auswahl == "zutaten":
                zutatenwahl = input("Nach welchen Zutaten möchten sie filtern?\n")

                passende_rezepte = service.filter_rezepte_nach_zutaten(storage.Gerichte,zutatenwahl)
                if not passende_rezepte:
                    print("Ungültige Auswahl.")
                    continue

                rezeptname = service.zeige_rezeptname(passende_rezepte)
                for variable in rezeptname:
                    print(variable)
                try:                   
                    auswahl = int(input("Nummer wählen:\n"))
                    rezept = service.rezept_nach_index(passende_rezepte, auswahl)
                    
                    

                    if rezept is None:
                        print("Ungültige Nummer.")
                        continue
                                
                    for zeile in rezept.anzeigen():
                        print(zeile)

                    continue

                except ValueError:
                    print("Bitte eine Zahl eingeben.")


            if filter_auswahl == "gang":
                gangwahl = input("Möchten sie Vorspeise, Hauptspeise oder ein Dessert zubereiten?\n")

                passende_rezepte = service.filter_rezepte_nach_gang(storage.Gerichte,gangwahl)

                if not passende_rezepte:
                    print("Ungültige Auwahl.")
                    continue

                rezeptname = service.zeige_rezeptname(passende_rezepte)
                for variable in rezeptname:
                    print(variable)

                try:
                    auswahl = int(input("Nummer wählen:\n"))
                    rezept = service.rezept_nach_index(passende_rezepte, auswahl)
                    
                    

                    if rezept is None:
                        print("Ungültige Nummer.")
                        continue
                                
                    for zeile in rezept.anzeigen():
                        print(zeile)

                    continue

                except ValueError:
                    print("Bitte eine Zahl eingeben.")








        

    elif Menueauswahl == "löschen":
        print([v.Name for v in storage.Gerichte])
        try:

            rezeptname = input("Welches Rezept soll gelöscht werden?")
            rezept_zum_loeschen = service.rezept_finden(storage.Gerichte, rezeptname)

            if rezept_zum_loeschen is None:
                print("Rezept nicht gefunden.")
                continue

            rezept_zum_loeschen.anzeigen()
            rueckversichern = input(f"Sind sie sicher, dass {rezept_zum_loeschen.Name} gelöscht werden soll? Ja/Nein").strip().lower()
            if rueckversichern.strip().lower() == "ja":
                    service.rezept_loeschen(storage.Gerichte,rezept_zum_loeschen)
                    print("Rezept wurde gelöscht!")
            else:
                print("Das Rezept wird nicht gelöscht.")
                continue

            break

        except ValueError:
            print("Ungültig!")

        
        


