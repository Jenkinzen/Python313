# storage.py
from rezeptliste_model import Rezept
import json
from pathlib import Path
from typing import List
# Globale Liste für alle Rezepte
Gerichte: List[Rezept] = []

# Pfad zur JSON-Datei
DATEI = Path("rezepte.json")

# Standardrezepte, falls JSON noch leer ist
STANDARD_REZEPTE = [
    Rezept(
        "Gebratene Enokis",
        ["Enokis", "Salz", "Bratöl"],
        "Unteres Stück der Enoki abschneiden und in die Pfanne geben. "
        "Anbraten bis sie knusprig und hellbraun sind.",
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

# Gueltige Gänge
gueltige_gaenge = ["vorspeise", "hauptspeise", "dessert"]


def lade_rezepte():
    """Lädt Rezepte aus JSON oder benutzt Standardrezepte"""
    global Gerichte
    if DATEI.exists():
        with open(DATEI, "r", encoding="utf-8") as f:
            daten = json.load(f)
        Gerichte = [
            Rezept(
                Name=d["Name"],
                Zutaten=d["Zutaten"],
                Zubereitung=d["Zubereitung"],
                Gang=d["Gang"],
                Notizen=d.get("Notizen", "")
            )
            for d in daten
        ]
    else:
        # JSON existiert noch nicht -> Standardrezepte nutzen
        Gerichte = STANDARD_REZEPTE.copy()


def speichere_rezepte():
    """Speichert alle Rezepte in der JSON-Datei"""
    daten = [
        {
            "Name": r.Name,
            "Zutaten": r.Zutaten,
            "Zubereitung": r.Zubereitung,
            "Gang": r.Gang,
            "Notizen": r.Notizen
        }
        for r in Gerichte
    ]

    # Optional Backup erstellen
    if DATEI.exists():
        backup = DATEI.with_suffix(".json.bak")
        DATEI.replace(backup)

    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)


# JSON beim Start laden
lade_rezepte()