from Ville import Ville

class Capitale(Ville):

    def __init__(self, nom, nompays,nbHabitants=0) :

        Ville.__init__(self, nom,nbHabitants=0)
        self.nom = nom
        self.nompays = str(nompays).upper()
        self.nbHabitants = nbHabitants

    def get__nompays(self):
        return self.nompays
    def set__nompays(self,nompays):
        self.nompays = nompays
    def categorie(self):
        if self.nompays != "" :
            return "Categorie C"
        else:
            Ville.categorie()

    def __str__(self):
        return "Nom de la Ville :" + self.nom + "\n" " Nom du Pays est " + self.nompays +"\n" " Nombre de population : " + str(self.nbHabitants)


