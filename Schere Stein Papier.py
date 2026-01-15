import random
Antwort = ["Ja","ja","Nein","nein"]
Gesten =["Schere","Stein","Papier"]
computer_geste = random.choice(Gesten)

print("Willkommen zu: \n\nSchere,Stein,Papier!\n")

weiter = True

while weiter == True:
    Spieler_Geste = None
    while Spieler_Geste not in Gesten:
        print("Verfügbare Gesten:\n\n","\n".join(Gesten),"\n", sep="") # ohne sep="" Leerzeichen nach Absatz "Verfügbare Gesten" ( kann man auch einfach ohne sep mit + trennen statt ,)
        Spieler_Geste = input("Bitte wählen sie ihre Eingabe:\n\n")
        if Spieler_Geste not in Gesten:
            print("\nDiese Auswahl ist ungültig!\n")
            break
            
        print(f"\nSie haben {Spieler_Geste} gewählt,\nder Computer {computer_geste}.\n")

        if Spieler_Geste == computer_geste:
            print("Unentschieden!")
        elif(
            (Spieler_Geste == "Schere" and computer_geste == "Papier")
            or(Spieler_Geste == "Papier" and computer_geste == "Stein")
            or(Spieler_Geste == "Stein" and computer_geste == "Schere")
            ):
            print("Herzlichen Glückwunsch, sie haben gewonnen!")      
        else:
            print("Leider verloren!")

        nochmal = None
        while nochmal == None:          
            nochmal = input("Möchten sie das Spiel wiederholen? Ja / Nein ?")
            if nochmal == "Nein":
                print("Vielen Dank für das Nutzen des Programmes!")
                Spieler_Geste = "Papier"
                weiter = False
            elif nochmal == "Ja":
                continue
            else:
                print("Ungültige Auswahl")
                nochmal = None
                
                
                    
            

        