from rezeptliste_model import Rezept
import json
from pathlib import Path
from typing import List

# Globale Liste für alle Rezepte
Gerichte: List[Rezept] = []

# Pfad zur JSON
DATEI = Path("rezepte.json")

# Standardrezepte
STANDARD_REZEPTE = [
    Rezept(
        "Gebratene Enokis",
        ["Enokis", "Salz", "Bratöl"],
        "Unteres Stück der Enoki abschneiden und in die Pfanne geben. Anbraten bis sie knusprig und hellbraun sind.",
        "Vorspeise",
        ""
    ),
    Rezept(
        "Kokoscurry mit Pilzen",
        ["200 ml Kokosmilch", "Currypaste", "Pilze", "Udon Nudeln"],
        "Alles in den Wok geben und garen.",
        "Hauptspeise",
        ""
    ),
    Rezept(
        "Sushibowl",
        ["Reis", "Nori Blätter", "Frischkäse", "Stremellachs", "Gurke", "Lauchzwiebeln"],
        "Reis kochen, Zutaten klein schneiden, alles in einer Schüssel mischen.",
        "Hauptspeise",
        ""
    ),
    Rezept(
        "Tofu Schokomousse",
        ["Tofu", "Kakaopulver", "Agavendicksaft"],
        "Tofu pürieren, mit Kakaopulver und Agavendicksaft vermischen, kalt stellen.",
        "Dessert",
        ""
    )
]

# Gültige Gänge
gueltige_gaenge = ["vorspeise", "hauptspeise", "dessert"]

# JSON-Schema für Validierung
REZEPT_SCHEMA = {
    "Name": str,
    "Zutaten": list,
    "Zubereitung": str,
    "Gang": str,
    "Notizen": str
}

def rezept_validieren(rezept: dict) -> bool:
    """Prüft, ob ein Rezept alle erforderlichen Felder hat und die richtigen Typen nutzt."""
    try:
        for feld, typ in REZEPT_SCHEMA.items():
            if feld not in rezept:
                print(f"Fehlendes Feld: {feld}")
                return False
            if not isinstance(rezept[feld], typ):
                print(f"Falscher Typ für {feld}. Erwartet {typ}, gefunden {type(rezept[feld])}")
                return False

        if rezept["Gang"].strip().lower() not in gueltige_gaenge:
            print(f"Ungültiger Gang: {rezept['Gang']}")
            return False

        return True
    except Exception as e:
        print("Validierungsfehler:", e)
        return False

def lade_rezepte():
    """Lädt Rezepte aus JSON oder benutzt Standardrezepte"""
    global Gerichte
    if DATEI.exists():
        with open(DATEI, "r", encoding="utf-8") as f:
            daten = json.load(f)

        validierte_rezepte = []
        for d in daten:
            if rezept_validieren(d):
                neues_rezept = Rezept(
                    Name=d["Name"],
                    Zutaten=d["Zutaten"],
                    Zubereitung=d["Zubereitung"],
                    Gang=d["Gang"],
                    Notizen=d.get("Notizen", "")
                )
                validierte_rezepte.append(neues_rezept)
            else:
                print(f"Ungültiges Rezept übersprungen: {d.get('Name', 'Unbekannt')}")

        Gerichte = validierte_rezepte
    else:
        # JSON existiert noch nicht -> Standardrezepte nutzen
        Gerichte = STANDARD_REZEPTE.copy()

def speichere_rezepte():
    """Speichert alle Rezepte in der JSON-Datei"""
    daten = []
    for r in Gerichte:
        rezept_dict = {
            "Name": r.Name,
            "Zutaten": r.Zutaten,
            "Zubereitung": r.Zubereitung,
            "Gang": r.Gang,
            "Notizen": r.Notizen
        }

        if rezept_validieren(rezept_dict):
            daten.append(rezept_dict)
        else:
            print(f"Ungültiges Rezept nicht gespeichert: {r.Name}")

    # Optional Backup erstellen
    if DATEI.exists():
        backup = DATEI.with_suffix(".json.bak")
        DATEI.replace(backup)

    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)

# JSON beim Start laden
lade_rezepte()