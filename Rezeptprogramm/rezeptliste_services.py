import textwrap
from rezeptliste_storage import Gerichte
from rezeptliste_model import Rezept




def zeige_rezeptname(rezepte):
    gueltige_rezepte = []
    for nummer, rezept in enumerate(rezepte, start=1):
        gueltige_rezepte.append(f"{nummer}. {rezept.Name}")
    return gueltige_rezepte

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
        zutatenwahl for zutatenwahl in gerichte
        if any (zutat.lower() in einzelne_zutat.lower() for einzelne_zutat in zutatenwahl.Zutaten) 
    ]

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