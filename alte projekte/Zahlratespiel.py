import random
erneut = True
gesuchte_zahl = random.randint(1,100)
print(gesuchte_zahl)
ratezahl = None
while erneut:
    versuche = 7 

    while versuche > 0:
        try: 
            ratezahl = int(input("Wir suchen eine Zahl zwischen 1 und 100, geben sie eine Zahl ein!:"))

        except ValueError:
            print("\033[31;47mSIE BEN\033[0mehmen sich kindisch! \033[31;47mACHT\033[0men sie darauf nur Zahlen einzugeben sonst \033[31;47mVIER\033[0mt das zu nichts. ")
            continue

        versuche -= 1 

        if ratezahl > gesuchte_zahl:
            print("Die gesuchte Zahl ist kleiner!\n Noch "+ str(versuche) +" Versuche!")
        elif ratezahl < gesuchte_zahl:
            print("Die gesuchte Zahl ist größer!\n Noch "+ str(versuche) +" Versuche!")
        else: 
            print("Glückwunsch!\nSie haben die Zahl erraten!")
            while ratezahl in range(1,101):
                wiederholen = input("Möchten sie nochmal spielen, Ja oder Nein?")
                if wiederholen == "Ja":   
                    erneut = True
                    versuche = 7
                    gesuchte_zahl = random.randint(1,100)
                    break

                elif wiederholen == "Nein":
                    erneut = False
                    break

                else:
                    print("Ungültige Auswahl, Ja oder Nein?")
                    continue

        
            
            

        
        while versuche == 0:
            nochmal = input("Schade, sie haben alle Versuche aufgebraucht! \n Nochmal, Ja oder Nein?")
            if nochmal == "Ja":
                versuche = 7
                gesuchte_zahl = random.randint(1,100)
                erneut = True
                break

            elif nochmal == "Nein":
                erneut = False
                break

            else:
                print("Ungültige Auswahl, Ja oder Nein?")
                continue

            
        
        
        
