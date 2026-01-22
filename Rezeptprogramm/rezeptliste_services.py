import textwrap
from rezeptliste_storage import Gerichte
from rezeptliste_model import Rezept




def zeige_rezeptname(rezepte):
    gueltige_rezepte = []
    for nummer, rezept in enumerate(rezepte, start=1):
        gueltige_rezepte.append(f"{nummer}. {rezept.Name}")
    return gueltige_rezepte

"""gültige rezepte = [] erstellt eine leere liste"""

def rezept_finden(Gerichte,rezeptname):

    for rezept in Gerichte:
        if rezept.Name.strip().lower() == rezeptname.strip().lower():
            return rezept

    return None 
            
def filter_rezepte_nach_gang(gerichte, gang):
    return [
        gangwahl for gangwahl in gerichte
        if gangwahl.Gang.strip().lower() == gang.strip().lower()
    ]

def filter_rezepte_nach_zutaten(gerichte, zutat):
    return[
        rezeptwahl for rezeptwahl in gerichte
        if any (zutat.lower() in einzelne_zutat.lower() for einzelne_zutat in rezeptwahl.Zutaten) 
    ]

"""Uff.... also durch die [] Klammern wird das ergebnis der funktion innerhalb in eine Liste 
übernommen.
     erstes rezeptwahl(variable) sagt welches Objekt übernommen wird.
    das "for rezeptwahl in gerichte" sagt, das alle "rezeptwahl" Elemente die die funktion
       in gerichte(Parametervariable)"""
                        
      # -[Parameter = die dinger rechts vom Funktionsnamen], 
      # wird in der UI durch bspw "filter_rezepte_nach_zutaten(storage.Gerichte, XXXXX)
      #  definiert. )-
           
"""besitzen in die liste rein kommt die durch das erste rezeptwahl entsteht-

     if any = wenn es dort irgendetwas gibt ,dass: """

    # zutat.lower() = der zweite Parameter , also quasi platzhhalter für den Input durch UI.
    # hier bspw > "filter_rezepte_nach_zutaten(storage.Gerichte, zutatenwahl)
    # wobei "zutatenwahl" die variable ist in der im UI die gesuchte Zutat gespeichert wird.
    #(zutatenwahl = input("Nach welcher Zutat möchten sie filtern")

""" Zutat(Parameter) 
    in einzelne_zutat (wie oben rezeptwahl for rezeptwahl)
     for einzelne_zutat in rezeptwahl.Zutaten 
     also das einzelne Element was dem Suchkriterium aus Zutaten entspricht
    in die liste rezeptwahl einfügen.
      """
    # Zusammengefasst : "Schreib mir auf die liste Rezeptwahl alle Gerichte von denen die Strings
    #                     (einzelne_zutat) der Liste "Zutaten" irgendwie
    #                    -gesuchtes Kriterium- in der rezeptwahl.Zutaten erfüllen "


def gang_validieren(gerichte, gang):
    gang = gang.strip().lower()
    return any(
        rezept.Gang.strip().lower() == gang
        for rezept in gerichte
    )

def zutat_validieren(gerichte, zutat):
    zutat = zutat.strip().lower()
    return any(
        (zutatliste.lower()for zutatliste in rezept.Zutaten)
        for rezept in gerichte
        )

def rezept_nach_index(rezepte, index):
    if 1 <= index <= len(rezepte):
        return rezepte[index - 1]
    return None

def rezept_loeschen(gerichte,rezeptwahl):
    gerichte.remove(rezeptwahl)

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
    Gerichte.append(rezept)