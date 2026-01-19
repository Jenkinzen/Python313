import random
import textwrap


class Rezept():
    def __init__(self,Name,Zutaten,Zubereitung,Notizen,Gang):
        self.Name = Name
        self.Zutaten = Zutaten
        self.Zubereitung = Zubereitung
        self.Notizen = Notizen
        self.Gang = Gang

    def format_multiline(self,label, value, width=60):
        lines = []                                          # leere liste namens "lines" wird erstellt
        label_width = 13                                    # die variable "label_width" wird auf 13 gesetzt
        wrapper = textwrap.TextWrapper(                     # textwrap ist ein Modul für Textformation
            width=width,                                    # setzt den width befehl aus dem Modul textwrap auf die 60 oben in der klammer.
            subsequent_indent=" " * label_width             # subsequent_indent ist der command von textwrap damit es weiß das es um die nachfolgenden Zeilen geht (subsequent indent = nachfolgende einrückung)
        )                                                   # initial indent = erstzeilige Einrückung.

        if isinstance(value, list):                                     # if isinstance prüft ob value vom Typ Liste ist(wie es bei den Zutaten der Fall ist)                                                                   #
            first = True                                                # first auch ein platzhalter für eine Variable, kann man auch Zauberpeter oder KönigJensJudithDerOderDieDritte nennen.
            for item in value:                                          # item = die einzelnen Zutaten (nur ein platzhalter! kann man auch Smittywerbenjaggermanjensen oder Nasenbein nennen)
                if first:                                               # Value = die ganze Zutatenliste (Aber value auch nur ein random austauschbarer platzhalter)
                    wrapper.initial_indent = f"{label:<{label_width}}"  # initial indent , also erste Einrückung ist gleich erst Label, dann : als Start , < heißt rechtsbündig und {label_width} sagt aus das es 13 Zeichenstellen vom linken Zeilenbeginn aus eingerückt wird.
                    first = False                                       # damit die Schleife nach dem ersten einrücken weiter geht
                else:
                    wrapper.initial_indent = " " * label_width          # damit in allen folgenden Zeilen das Label (also bspw "Zutaten:" nicht immer wieder rechts steht sondern nur rechts untereinander die folgenden Zutaten ohne das Label links)

                lines.extend(wrapper.wrap(item))                        # wrapper wrap item macht, dass falls ein item name mehr buchstaben als die width hat, er umgebrochen wird.
                                                                        # lines.extend fügt die zeilen dann so umgebrochen und formatiert in die leere "lines" liste ein die oben definiert wurde.
        else:                                                         
            wrapper.initial_indent = f"{label:<{label_width}}"          # Einrückung für alles was keine "list" beinhaltet.        
            lines.extend(wrapper.wrap(value))                           # .extend = entpackt den inhalt(items) der Liste(value) und fügt sie in die leere Liste "lines"                  
                                                                        # .append = würde theoretisch das gleiche machen, aber den inhalt von value als Liste übergeben, dann gäb es quasi in der liste "lines" nochmal eine liste "value"mit den items drin.
        return lines                                                    
    
    def anzeigen(self):
        output = []
        output += self.format_multiline("Gericht:",self.Name)
        output += self.format_multiline("Zutaten:",self.Zutaten)
        output += self.format_multiline("Zubereitung:",self.Zubereitung)
        output += self.format_multiline("Notizen",self.Notizen)
        return iter(output)                                              

       
Gerichte = [Rezept("Gebratene Enokis",
                    ["Enokis","Salz","Bratöl"],
                    "Unteres Stück der Enoki abschneiden und in die mit Bratöl erhitzte" \
                    "Pfanne geben. Die Enoki anbraten bis sie knusprig und hellbraun sind.",
                    "Keine",
                    "Vorspeise"),
            Rezept("Kokoscurry mit Pilzen",
                    ["200 ml Kokosmilch","Currypaste", "Pilze", "Udon Nudeln"],
                    "Alles in den Wok und dann gib ihm!",
                    "Keine",
                    "Hauptspeise"),
            Rezept("Sushibowl",
                    ["Reis","Nori Blätter","Frischkäse","Stremellachs","Gurke","Lauchzwiebeln"],
                    "Reis kochen, währenddessen Stremellachs klein schneiden oder zupfen." \
                    "Gurken sowie Lauchzwiebeln kleinschneiden. " \
                    "Danach alles in eine Salatschüssel und mit dem gekochten Reis verrühren. " \
                    "Nori Blätter nutzen um die Sushibowl mit den Händen zu essen.",
                    "Keine",
                    "Hauptspeise"),
            Rezept("Tofu Schokomousse",
                    ["Tofu" ,"Kakaopulver" ,"Agaven Dicksaft" ],
                    "Tofu pürieren und mit Agaven Dicksaft und Kakaopulver vermischen." \
                    "Danach 1-2 Stunden kalt stellen.",
                    "Keine",
                    "Dessert")]
 
def rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " "):

    Zutatenliste = [z.strip() for z in Rezeptzutaten.split(",")]

    
    # Neues Rezept machen
    neues_rezept = Rezept(
        Name=Rezeptname,
        Zutaten=Zutatenliste,
        Zubereitung=Rezeptzubereitung,
        Notizen=Rezeptnotizen,
        Gang=Rezeptgang.title()
    )

    
    return neues_rezept

def rezept_loeschen(Gerichte,rezeptname):

    for rezept in Gerichte:
        if rezept.Name.strip().lower() == rezeptname.strip().lower():
            return rezept

    return None 
            
"""def zeige_rezeptliste(Gerichte):
    for i, rezept in enumerate(Gerichte, start=1):      # start=1 damit die aufzählung nicht bei 0 beginnt
        print(f"{i}. {rezept.Name}")                    # enumerate python befehl zum durchnummerieren
                                                        # i ist ein random platzhalter, kann auch "schnörkeljörg" oder "klababnschnab" genannt werden
                                                        # rezept ist eine Variable die in dieser Definition erstellt wird
                                                        # hätte auch x, banane oder asdfsdfkg heißen können , ein temporärer Name für ein Objekt aus der Liste ( hier der Rezeptname)
                                                        # i = platzhalter für die Nummerierung der angezeigten rezepte(an wievielter Stelle steht das Rezept?) | rezept = welches Rezept?  i = 1. | rezept = Tofu Schokomousse
"""

"""def zeige_rezeptliste_nach_gang(Gerichte, gangwahl):
    # Filtere die Liste nach der gewählten Kategorie
    passende_rezepte = [r for r in Gerichte if r.Gang.strip().lower() == gangwahl]          # r ist eine temporäre Variable in die dann die Gerichte die gang == gangwahl haben
                                                                            # einsortiert werden. Hier schreibt man sich quasi die Gerichte die zur Auswahl passen
    # Nummerierte Anzeige                                                   # auf einen neuen Zettel den man einfach "r" nennt um eine neue Liste zu haben(r ist einfach ein platzhalter, kann auch "qasdewr" oder "blablablubb" genannt werden)
    for i, rezept in enumerate(passende_rezepte, start=1):                  # die nur die gesuchten Gerichte beinhaltet. | "(r) for r in Gerichte" = gehe über alle Elemente in Gerichte (und pack sie in r).
        print(f"{i}. {rezept.Name}")
    
    return passende_rezepte  # zurückgeben, damit man ein Rezept auswählen kann"""

def filter_rezepte_nach_gang(gerichte, gang):
    return [
        rezept for rezept in gerichte
        if rezept.Gang.strip().lower() == gang.strip().lower()
    ]

def zeige_rezeptliste(rezepte):
    for i, rezept in enumerate(rezepte, start=1):
        print(f"{i}. {rezept.Name}")

"""def rezept_auswaehlen(passende_rezepte):                                                        
    try:
        auswahl = int(input("Welches Rezept möchten Sie auswählen? (Nummer): "))

        if 1 <= auswahl <= len(passende_rezepte):           # len gibt die Anzahl von Sachen an (buchstaben in wörtern oder einzelne Positionen in Listen ( wie hier bei Gerichte))
            return passende_rezepte[auswahl - 1]            # also wenn auswahl größer gleich 1 und kleiner gleich maximale anzahl an gerichten ist sagt zeile 63 aus, dass es dann valide ist.

        else:
            print("Bitte eine gültige Nummer eingeben.")

    except ValueError:
        print("Bitte eine Zahl eingeben.")"""

def gang_validieren(gerichte, gang):
    gang = gang.strip().lower()
    return any(
        rezept.gang.strip().lower() == gang
        for rezept in gerichte
    )

def rezept_nach_index(rezepte, index):
    if 1 <= index <= len(rezepte):
        return rezepte[index - 1]
    return None


#Kann nicht oben zu den anderen Funktionen da dort "Gerichte" noch nicht deklariert ist.
neustart = True
while neustart:

    Menueauswahl = input("Möchten sie ein Rezept [einfügen], [ansehen] oder [löschen]?")

    if Menueauswahl == "einfügen":

        Rezeptname = input("Wie heißt das Rezept?")
        Rezeptzutaten = input("Welche Zutaten brauch es?( Zutaten bitte mit , trennen)")
        Rezeptzubereitung = input("Wie wird es zubereitet?")       
        gueltige_gaenge = ["vorspeise", "hauptspeise", "dessert"]
        Rezeptgang = None
        while Rezeptgang is None:
            eingabe = input("Ist es Vorspeise, Hauptspeise oder Dessert? ").strip().lower()
            if eingabe in gueltige_gaenge:
                Rezeptgang = eingabe
            else:
                print("Ungültige Auswahl! Bitte erneut eingeben.")                    
        neues_rezept = rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " ")
        Gerichte.append(neues_rezept)
        print("Rezept wurde eingefügt!")
        continue

    elif Menueauswahl == "ansehen":
        while True:
            wahl = input("Möchten sie Vorspeise, Hauptspeise oder ein Dessert zubereiten?")
            
            if not gang_validieren(Gerichte,wahl):
                print("Ungültige Auswahl.")
                continue

            passende_rezepte = filter_rezepte_nach_gang(Gerichte,wahl)
            break

        for i, rezept in enumerate(passende_rezepte, start=1):
            print(f"{i}. {rezept.Name}")

        try:
            auswahl = int(input("Nummer wählen:"))
            rezept = rezept_nach_index(passende_rezepte, auswahl)
            
            

            if rezept is None:
                print("Ungültige Nummer.")
                continue
            
            rezept.anzeigen()
            
            break

        except ValueError:
            print("Bitte eine Zahl eingeben.")

        

    elif Menueauswahl == "löschen":
        print([v.Name for v in Gerichte])
        rezeptname = input("Welches Rezept soll gelöscht werden?")
        rezept_zum_loeschen = rezept_loeschen(Gerichte, rezeptname)
        if rezept_zum_loeschen is None:
            print("Rezept nicht gefunden.")
            continue
        rueckversichern = input(f"Sind sie sicher, dass {rezept_zum_loeschen.Name} gelöscht werden soll? Ja/Nein").strip().lower()
        if rueckversichern.strip().lower() == "ja":
                Gerichte.remove(rezept_zum_loeschen)
                print("Rezept wurde gelöscht!")
        else:
            print("Das Rezept wird nicht gelöscht.")
            
        continue



