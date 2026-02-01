import rezeptliste_model as model
import rezeptliste_storage as storage

######## BASISZUGRIFF - LESEN

def alle_rezeptnamen():
    return[
        rezepte.name for rezepte in storage.Gerichte
    ]
  
def alle_rezepte():                                               
    return storage.Gerichte

def rezept_nach_index(rezepte, index):
    """index = auswahl der Gerichtnummer im UI.
    wenn die auswahl größer gleich 1 ist und kleiner als die
    gesamtanzahl an rezepten (len(rezepte) nummeriert die einzelnen Objekte in der Liste durch
    ,hier halt die Rezepte in der Liste Gerichte)"""
    if 1 <= index <= len(rezepte):
        return rezepte[index - 1]
    return None

def rezept_finden(rezeptname):

    for rezept in storage.Gerichte:
        if rezept.name.strip().lower() == rezeptname.strip().lower():
            return rezept

    return None 


######## VALIDIERUNG

def gang_pruefen(gangeingabe):
    return gangeingabe.lower() in storage.GUELTIGE_GAENGE

def gang_validieren(gerichte, gangeingabe):
    """wenn irgendwas (any) in rezept.Gang das beinhaltet was der input war dann gibs raus
   any ----> auch wenn man "des" eingibt zeigt er dessert an weil des dadrin steckt.
   ohne any würde er dann nichts raus geben."""
    gang = gangeingabe.strip().lower()
    return any(
        rezept.Gang.strip().lower() == gang
        for rezept in gerichte
    )

######## FILTER

def filter_rezepte_nach_gericht(gericht):
    """wollte eigentlich mit "any" arbeiten, aber teiltreffer ("Bro" eingabe zeigt "Brokkoli" an)
    werden auch durch "in" ermöglicht. any macht kein sinn weil gerichte.Name keine Liste
     sondern ein String ist, bei Zutaten machte es Sinn weil Zutaten eine Liste ist.(any = irgendeins aus (der liste)/ in = irgendetwas in (string))
     """
    gericht = gericht.strip().lower()
    return [
        rezept for rezept in storage.Gerichte
        if gericht.lower().strip() in rezept.name.strip().lower()
    ] 

def filter_rezepte_nach_gang(gangeingabe):
    """Siehe filter_rezepte_nach_zutaten, selbe sache nur ohne aus einer liste(gerichte)
   eine weitere liste(wie unten die zutatenliste) aufrufen zu müssen."""
    return [
        rezept for rezept in storage.Gerichte
        if rezept.gang.strip().lower() == gangeingabe.strip().lower()
    ]

def filter_rezepte_nach_zutaten(zutaten):
    """ rezept for rezept in storage.Gerichte > geh jedes rezept durch was gespeichert wurde.(s.Gerichte = rezeptsammlung / rezept for rezept = jedes Rezept einzeln durchgehen)
    any(zutat in einzelne_zutat = gibt es die gesuchten Zutaten im Rezept? ///// for einzelne_zutat in rezept.Zutaten) = guck jede Zutat des Rezepts an.
    all(any(bla)for zutat in zutaten) =  sind ALLE gesuchten Zutaten in diesem Rezept?""" 
    return[
        rezept for rezept in storage.Gerichte
        if all(any (zutat in einzelne_zutat.Name.lower() for einzelne_zutat in rezept.zutaten)
               for zutat in zutaten
        )
    ]


######## ÄNDERUNGEN

def rezepterstellung(rezeptname, zutaten_strings, zubereitung, gang, notizen=""):
    """In die Leere Zutatenliste kommen nachher die Objekte aus der Funktion.
        zs variable für Zutat als Text ( wie das 1. x in x for x in Gerichte )
        teile = zs.split() -> die Sachen werden durch leerzeichen gesplittet(also Name,menge,einheit)
        if not teile -> überspringen von allem was sonst zum error führen würde.

        zutatenname Zeile -> teile (also die Teile der Zutat: Name, menge, einheit)
          [:-2] heißt NICHT geteilt durch -2 sondern : sagt alles und -2 bis auf die letzten beiden! 
          damit wird jeder Input bis auf die letzten beiden zum "teil" Name hinzugefügt.
          wenns bspw [:-1] wär dann würde die Menge noch mit beim Namen stehen.
          und durch .join davor wird die liste von wörtern zu einem String mit Leerzeichen.
        if len(teile) > 2 -> also mach .join(teile[:-2]) insofern mehr als 2 wörter eingegeben werde.
        else teile[0] -> wenn weniger als 2 wörter eingegeben werden, nimm halt das 1 Wort oder die Leerstelle.
        
        menge -> teile[-2] if len(teile) > 1  --> also vorletztes Teil
            wenn es mehr als 1 teil gibt
            else None -> sonst gibts halt keine Menge. 
            (Unfassbar smart, weil es "Salz , Prise" gibt also angaben ohne Menge,
            aber es gibt keine Angaben ohne Einheit aber mit Menge, weil was will jemand mit
            der aussage " du brauchst 150 Salz")
            
        einheit -> teile[-1] also ist das letzte teil
                if len(teile) >= 2 -> insofern es genau oder mehr als 2 teile gibt.
    """
    Zutatenliste = []
    for zs in zutaten_strings:
        teile = zs.split()
        if not teile:
            continue
        zutatenname = " ".join(teile[:-2]) if len(teile) > 2 else teile[0]
        menge = teile[-2] if len(teile) > 2 else None
        einheit = teile[-1] if len(teile) >= 2 else None
        Zutatenliste.append(model.Zutaten(name=zutatenname, menge=menge, einheit=einheit))

    neues_rezept = model.Rezept(
        name=rezeptname,
        zutaten=Zutatenliste,
        zubereitung=zubereitung,
        notizen="",
        gang=gang.title()
    )
    rezept_hinzufuegen(neues_rezept)
    return neues_rezept

def rezept_laden():
    storage.lade_rezepte()

def rezept_loeschen(rezeptwahl):
    """speichere_rezepte speichert die überarbeitete Liste , quasi die Liste mit dem 
    entfernten Gericht wird gespeichert"""
    storage.Gerichte.remove(rezeptwahl)
    storage.speichere_rezepte()

def rezept_hinzufuegen(rezept):
    storage.Gerichte.append(rezept)
    storage.speichere_rezepte() 

def rezept_einfuegen(Rezeptname,Rezeptzutaten,Rezeptzubereitung,Rezeptgang,Rezeptnotizen = " "):
    """ Die Zutatenliste Line ist damit die Zutaten für die Zutatenliste als einzelne Elemente eingefügt werden
und nicht alle Zutaten zusammen als ein langer String gelten statt eine Liste mit einzelnen Zutaten.

leeres neues rezept wird generiert und mit den Daten aus der UI
    gefüllt > neues Rezept AAAABER es ist noch nicht in der Gerichte Liste.
    das geschieht erst durch die Funktion rezept_hinzufuegen. Dann wird in die Liste Gerichte appended."""
    Zutatenliste = [z.strip() for z in Rezeptzutaten.split(",")]

    
    # Neues Rezept machen
    neues_rezept = model.Rezept(
        name=Rezeptname,
        zutaten=Zutatenliste,
        zubereitung=Rezeptzubereitung,
        notizen=Rezeptnotizen,
        gang=Rezeptgang.title()
    )

    
    return neues_rezept
