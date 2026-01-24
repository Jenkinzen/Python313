from rezeptliste_model import Rezept

import json

DATEI = "rezepte.json"

def lade_rezepte():
    try:
        with open(DATEI, "r") as f:
            daten = json.load(f)
            return [Rezept(**r) for r in daten]
    except FileNotFoundError:
        return[]
    
def speichere_rezepte(rezepte):
    with open(DATEI, "w") as f:
        json.dump([r.__dict__ for r in rezepte],f, indent=2)
        
        """ Rezept wird zu dicts konvertiert
        dicts speichern Daten als Schlüssel-Wert-Paare 
        also bspw. Schlüssel:"Name",Wert:"Gebratene Enokis"""



Gerichte= lade_rezepte()

Gerichte = [Rezept("Gebratene Enokis",
                    ["Enokis","Salz","Bratöl"],
                    "Unteres Stück der Enoki abschneiden und in die mit Bratöl erhitzte " \
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
                    "Reis kochen, währenddessen Stremellachs klein schneiden oder zupfen. " \
                    "Gurken sowie Lauchzwiebeln kleinschneiden. " \
                    "Danach alles in eine Salatschüssel und mit dem gekochten Reis verrühren. " \
                    "Nori Blätter nutzen um die Sushibowl mit den Händen zu essen.",
                    "Keine",
                    "Hauptspeise"),
            Rezept("Tofu Schokomousse",
                    ["Tofu" ,"Kakaopulver" ,"Agaven Dicksaft" ],
                    "Tofu pürieren und mit Agaven Dicksaft und Kakaopulver vermischen. " \
                    "Danach 1-2 Stunden kalt stellen.",
                    "Keine",
                    "Dessert")]

gueltige_gaenge = ["vorspeise", "hauptspeise", "dessert"]