import rezeptliste_model as model
import rezeptliste_storage as storage

def alle_rezeptnamen():
    return[
        rezepte.Name for rezepte in storage.Gerichte
    ]
  
def alle_rezepte():                                               
    return storage.Gerichte

def gang_pruefen(gang):
    return gang.lower() in storage.gueltige_gaenge
        

"""gültige rezepte = [] erstellt eine leere liste,
    enumerate funktioniert IMMER so, dass die Nummerierung die erste variable
     nutzt. 
    Also wenn man "Gebratene Enoki 1" haben wollen würde, dann müsste man den output
    in einer zweiten funktion umdrehen bzw halt dann (f"{rezept.Name}. {nummer}) appenden"""

def rezept_finden(rezeptname):

    for rezept in storage.Gerichte:
        if rezept.Name.strip().lower() == rezeptname.strip().lower():
            return rezept

    return None 

"""wenn eingegebener name in der rezeptliste zu finden ist > return das rezept. lel"""

def filter_rezepte_nach_gericht(gericht):
    gericht = gericht.strip().lower()
    return [
        rezept for rezept in storage.Gerichte
        if gericht.lower().strip() in rezept.Name.strip().lower()
    ] 

"""wollte eigentlich mit "any" arbeiten, aber teiltreffer ("Bro" eingabe zeigt "Brokkoli" an)
    werden auch durch "in" ermöglicht. any macht kein sinn weil gerichte.Name keine Liste
     sondern ein String ist, bei Zutaten machte es Sinn weil Zutaten eine Liste ist.
      Faustregel > Liste = any() / String = kein any() sondern in oder halt was grade passt. """

def filter_rezepte_nach_gang(gang):
    return [
        rezept for rezept in storage.Gerichte
        if rezept.Gang.strip().lower() == gang.strip().lower()
    ]

"""Siehe filter_rezepte_nach_zutaten, selbe sache nur ohne aus einer liste(gerichte)
    eine weitere liste(wie unten die zutatenliste) aufrufen zu müssen."""

def filter_rezepte_nach_zutaten(zutaten):
    return[
        rezept for rezept in storage.Gerichte
        if all(any (zutat in einzelne_zutat.lower() for einzelne_zutat in rezept.Zutaten)
               for zutat in zutaten
        )
    ]

""" rezept for rezept in storage.Gerichte > geh jedes rezept durch was gespeichert wurde.(s.Gerichte = rezeptsammlung / rezept for rezept = jedes Rezept einzeln durchgehen)
    any(zutat in einzelne_zutat = gibt es die gesuchten Zutaten im Rezept? ///// for einzelne_zutat in rezept.Zutaten) = guck jede Zutat des Rezepts an.
    all(any(bla)for zutat in zutaten) =  sind ALLE gesuchten Zutaten in diesem Rezept?"""
def gang_validieren(gerichte, gang):
    gang = gang.strip().lower()
    return any(
        rezept.Gang.strip().lower() == gang
        for rezept in gerichte
    )

"""wenn irgendwas (any) in rezept.Gang das beinhaltet was der input war dann gibs raus
            any ----> auch wenn man des eingibt zeigt er dessert an weil des dadrin steckt.
            ohne any würde er dann nichts raus geben."""

def rezept_nach_index(rezepte, index):
    if 1 <= index <= len(rezepte):
        return rezepte[index - 1]
    return None

"""index = auswahl der Gerichtnummer im UI.
    wenn die auswahl größer gleich 1 ist und kleiner als die
    gesamtanzahl an rezepten (len(rezepte) nummeriert die einzelnen Objekte in der Liste durch
    ,hier halt die Rezepte in der Liste Gerichte)"""

def rezept_loeschen(rezeptwahl):
    storage.Gerichte.remove(rezeptwahl)
    storage.speichere_rezepte()

"""speichere_rezepte speichert die überarbeitete Liste , quasi die Liste mit dem 
    entfernten Gericht wird gespeichert"""

def rezept_hinzufuegen(rezept):
    storage.Gerichte.append(rezept)
    storage.speichere_rezepte() 

def rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " "):

    Zutatenliste = [z.strip() for z in Rezeptzutaten.split(",")]

    
    # Neues Rezept machen
    neues_rezept = model.Rezept(
        Name=Rezeptname,
        Zutaten=Zutatenliste,
        Zubereitung=Rezeptzubereitung,
        Notizen=Rezeptnotizen,
        Gang=Rezeptgang.title()
    )

    
    return neues_rezept

""" Die Zutatenliste Line ist damit die Zutaten für die Zutatenliste als einzelne Elemente eingefügt werden
und nicht alle Zutaten zusammen als ein langer String gelten statt eine Liste mit einzelnen Zutaten.

leeres neues rezept wird generiert und mit den Daten aus der UI
    gefüllt > neues Rezept AAAABER es ist noch nicht in der Gerichte Liste.
    das geschieht erst durch die Funktion rezept_hinzufuegen. Dann wird in die Liste Gerichte appended."""