import textwrap
import rezeptliste_model as model


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

def rezept_hinzufuegen(rezept):
    model.Gerichte.append(rezept)

def rezept_loeschen(Gerichte,rezeptname):

    for rezept in Gerichte:
        if rezept.Name.strip().lower() == rezeptname.strip().lower():
            return rezept

    return None 
            
def filter_rezepte_nach_gang(gerichte, gang):
    return [
        rezept for rezept in gerichte
        if rezept.Gang.strip().lower() == gang.strip().lower()
    ]

def zeige_rezeptliste(rezepte):
    for i, rezept in enumerate(rezepte, start=1):
        print(f"{i}. {rezept.Name}")


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

def rezept_wirklich_loeschen(gerichte,rezeptwahl):
    gerichte.remove(rezeptwahl)