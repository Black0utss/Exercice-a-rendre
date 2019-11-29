from StarWars import *
from Acteur import *
from Personnage import *
#from Gentil import *
#from Mechant import *


perso1 = Personnage("Dark", " Small")
perso2 = Personnage("BB"," 8")

acteur1 = Acteur("REEVES","Keanu", [perso1])
acteur2 = Acteur("YO","DA",[perso2])

# titre = str(raw_input("entrer le titre du film"))
# Ads = str(raw_input("entrer l'annee de sortie"))
# Nde = str(raw_input("Entrer le numeros de l'episode"))
# cost =str( raw_input("Entrer le cout"))
# rctt = str(raw_input("Entrer la recette"))
# act = str(raw_input("Entrer le nom d'un acteur"))
#
# film1 = film(titre,Ads,Nde,cost,rctt,act)

film2 = film(a="Star Wars", b=1999, c="episode I : La Menace fantome", d= 25874525, e=12687455,f = [acteur1, acteur2])

acteur1.set__perso(["Jhon Wick", "Neo"])
print (film2.nbPersonnage())
film2.triacteur()
print (film2.malisttostr())

film1 = film("SuperMan",1978, 100000000,20000000)
film2 = film(a ="La Couleur Pourpre")

film2.set__AnneeSortie(1985)

film1.estBenificiaire()

mon_dico = {str(film2.get__AnneeSortie()) : film2, str(film1.get__AnneeSortie()) : film1}

def makeBackUp(mon_dico):
    for values in mon_dico.values():
        benefice = values.estBeneficiare
    return "{}, {} , {} ".format(values, benefice)

makeBackUp(mon_dico)

