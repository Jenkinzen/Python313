import json
from pathlib import Path
from typing import List
from rezeptliste_model import Rezept, Zutaten

DATEI = Path("rezepte.json")

Gerichte: List[Rezept] = []



GUELTIGE_GAENGE = ["vorspeise", "hauptspeise", "dessert"]

def lade_rezepte():
    global Gerichte

    if not DATEI.exists():
        Gerichte = []
        return

    with open(DATEI, "r", encoding="utf-8") as f:
        daten = json.load(f)

    Gerichte = []

    for r in daten:
        zutaten = [
            Zutaten(
                z["name"],
                z.get("menge"),
                z.get("einheit")
            )
            for z in r.get("zutaten", [])
        ]

        rezept = Rezept(
            name=r["name"],
            zutaten=zutaten,
            zubereitung=r["zubereitung"],
            gang=r["gang"],
            notizen=r.get("notizen", "")
        )

        Gerichte.append(rezept)

def speichere_rezepte():
    daten = []

    for r in Gerichte:
        daten.append({
            "name": r.name,
            "gang": r.gang,
            "zubereitung": r.zubereitung,
            "notizen": r.notizen,
            "zutaten": [
                {
                    "name": z.name,
                    "menge": z.menge,
                    "einheit": z.einheit
                }
                for z in r.zutaten
            ]
        })

    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=2, ensure_ascii=False)


def rezept_hinzufuegen(rezept: Rezept):
    global Gerichte
    Gerichte.append(rezept)
    speichere_rezepte()

def rezept_loeschen(rezept: Rezept):
    global Gerichte
    Gerichte.remove(rezept)
    speichere_rezepte()

