from Ville import *
from Capitale import *

v1 = Ville("Toulouse")
v2 = Ville("Strasbourg", 272975)

print (v1)
print (v2)
print ("/n")

c1 = Capitale("Paris", "France")
c2 = Capitale("Rome", "Italie", 2700000)
c1.set__nbHabitants(2181371)


print (c1)
print (c2)
print ("\n")

print ("Categorie de la Ville de " + v1.get__nom() + " : " + v1.categorie())

print ("Categorie de la Ville de " + v2.get__nom() + " : " + v2.categorie())

print ("Categorie de la Ville de " + c1.get__nom() + " : " + c1.categorie())
print ("\n")

