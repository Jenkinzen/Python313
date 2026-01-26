


"""ergebnis = []

for rezept in storage.Gerichte:
    if kriterium:
        ergebnis.append(rezept)"""

# erst als normale schleife denken

"""def filter_rezepte_nach_zutaten(zutat):
    treffer = []

    for rezept in storage.Gerichte:
        for einzelne_zutat in rezept.Zutaten:
            if zutat.lower() in einzelne_zutat.lower():
                treffer.append(rezept)
                break

    return treffer"""

#DAS ist die eigentliche Logik.
#Die List Comprehension ist nur eine Kurzschrift davon.

"""
✅ Liste → for
[b for b in buecher]

✅ Filtern → if
[b for b in buecher if ...]

✅ Liste im Objekt → any()
any(x in element for element in liste)

❌ String → KEIN any()
"du" in titel.lower()   # richtig"""

####################################################################
"""
🧠 Merksatz (wichtig!)

all() und any() liefern EIN Bool → niemals in eine Liste packen

❌ Nicht:
return [all(...)]

✅ Sondern:
return all(...)
"""
#######################ÜBUNGSGEBIET#################################
"""
class Rezept:
    def __init__(self, name, zutaten, gang):
        self.Name = name
        self.Zutaten = zutaten      # Liste von Strings
        self.Gang = gang            # String

rezepte = [
    Rezept("Spaghetti Bolognese", ["Nudeln", "Tomaten", "Hackfleisch"], "hauptspeise"),
    Rezept("Brokkoli Suppe", ["Brokkoli", "Sahne", "Zwiebeln"], "vorspeise"),
    Rezept("Pfannkuchen", ["Mehl", "Eier", "Milch"], "dessert"),
    Rezept("Tomatensalat", ["Tomaten", "Zwiebeln", "Olivenöl"], "vorspeise"),
]
#normale Schleife

def alle_rezeptnamen_als_liste():
    rezeptnamen = []
    for x in rezepte:
        rezeptnamen.append(x.Name)
    return rezeptnamen
    
# LC

rezeptnamen =[
    x.Name for x in rezepte
]

for lines in alle_rezeptnamen_als_liste():
    print(lines)

#################################################################

#normale Schleife

def alle_tomatenrezepte(auswahl):
    tomatenrezeptee = []
    for x in rezepte:
        if auswahl.strip().lower() in x.Name.lower():
            tomatenrezeptee.append(x)
    return tomatenrezeptee
     
#LC

def alle_tomatenrezeptee(auswahl):
    return[
        x for x in rezepte
        if auswahl.lower() in x.Name.lower()
]
        
auswahl = input("tomate")
for lines in alle_tomatenrezepte(auswahl):
    print(lines.Name)
for lines in alle_tomatenrezeptee(auswahl):
    print(lines.Name)
    
###############################################################

#direkt LC
def brokkoligerichte_finden(auswahl2):
    return [
    x for x in rezepte if any
    (auswahl2.lower().strip() in brokkoliwahl.lower() for brokkoliwahl in x.Zutaten)
    ]
             
auswahl2 = input("brokkoli oder bro oder kkoli")
for lines in brokkoligerichte_finden(auswahl2):
    print(lines.Name,lines.Zutaten,lines.Gang)


################################################################

def alle_vorspeisen_geben(auswahl3):
    return[
        x for x in rezepte if
        auswahl3.lower().strip() == x.Gang.lower().strip()
    ]

auswahl3 = input("vorspeise")
for lines in alle_vorspeisen_geben(auswahl3):
    print(lines.Name)

#################################################################
"""

class Buch:
    def __init__(self, titel, autor, seiten, genre, gelesen):
        self.titel = titel        # str
        self.autor = autor        # str
        self.seiten = seiten      # int
        self.genre = genre        # str
        self.gelesen = gelesen    # bool

buecher = [
    Buch("Der Hobbit", "Tolkien", 310, "Fantasy", True),
    Buch("1984", "Orwell", 328, "Dystopie", True),
    Buch("Clean Code", "Martin", 464, "Sachbuch", False),
    Buch("Dune", "Herbert", 800, "Sci-Fi", False),
]

#alle buchtitel als liste

def alle_buchtitel():
    return [
        x.titel for x in buecher
        ]

for lines in alle_buchtitel():
    print(lines)

#alle autoren als liste

def alle_autoren():
    return[
        x.autor for x in buecher
    ]

for lines in alle_autoren():
    print(lines)

#buecher die gelesen wurden

def alle_gelesenen():
    return[
        x.titel for x in buecher if x.gelesen == True 
    ]

for lines in alle_gelesenen():
    print(lines)

#buecher über 400 seiten

def buecher_ueber_400_seiten():
    return[
        x.titel for x in buecher if x.seiten > 400
    ]

for lines in buecher_ueber_400_seiten():
    print(lines)

#alle fantasy bücher

def alle_fantasy_buecher():
    return[
        x.titel for x in buecher if x.genre.lower() == "fantasy"
    ]

for lines in alle_fantasy_buecher():
    print(lines)

#buecher in denen der titel "du" enthält

def alle_buecher_mit_du():
    return[
        x.titel for x in buecher if "du" in x.titel.lower()
    ]

for lines in alle_buecher_mit_du():
    print(lines)

#titel und seiten als string

def titel_und_seiten_string():
    return[
        f"{x.titel},{x.seiten}Seiten" for x in buecher
    ]

for lines in titel_und_seiten_string():
    print(lines)

#titel ungelesener bücher

def ungelesene_buecher():
    return[
        x.titel for x in buecher if x.gelesen == False
    ]
# oder x.titel for x in buecher if not x.gelesen

for lines in ungelesene_buecher():
    print(lines)

#buch mit mehr als 700 seiten

def buch_mehr_als_700():
    return[
        x.titel for x in buecher if x.seiten > 700
    ]

# oder any(b.seiten > 700 for b in buecher) > sagt dann einfach per True / False ob es auf das jeweilige buch zutrifft

def buch_mehr_als_700_pruef():
    return[
        x.seiten > 700 for x in buecher
    ]

for lines in buch_mehr_als_700():
    print(lines)

for lines in buch_mehr_als_700_pruef():
    print(lines)

#sind alle bücher gelesen? 

#def buecher_gelesen():
#    return[
#        x.gelesen == True for x in buecher
#    ]

#for lines in buecher_gelesen():
#    print(lines)

#eigentlich falsch, das würde eher sagen : welche bücher sind gelesen und welche nicht?

#richtig:

def buecher_gelesen_richtig():
    return all(x.gelesen for x in buecher)


print(buecher_gelesen_richtig())

# antwort > ein False weil nicht alle bücher gelesen wurden
# brauch kein "for lines in" weil nur "False" oder "True" gecheckt werden soll

# alle sci fi titel

def sci_fi_titel():
    return[
        x.titel for x in buecher if x.genre.lower() == "sci-fi"
    ]

for lines in sci_fi_titel():
    print(lines)


#titel von büchern unter 350 seiten

def buecher_unter_350_seiten():
    return[
        x.titel for x in buecher if x.seiten < 350
    ]

for lines in buecher_unter_350_seiten():
    print(lines)

# gibt es ungelesene fantasy bücher?

def ungelesene_fantasy_buecher():
    return any(
        x.genre.lower() == "fantasy" and not x.gelesen for x in buecher
        ) 
    

print(ungelesene_fantasy_buecher())
    

#brauch wieder kein "for lines in" weil einfach nur True oder False gecheckt wird.s