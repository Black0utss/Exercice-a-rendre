class Ville:

    def __init__(self, nom, nbHabitants = 0):
        self.nom = nom.capitalize()
        self.nbHabitants =nbHabitants

    def get__nom(self):
        return self.nom
    def set__nom(self,nom):
        self.nom = nom

    def get__nbHabitants(self):
        return self.nbHabitants
    def set__nbHabitants(self,nbHabitant):
        if nbHabitant > 0:
            self.nbHabitants = nbHabitant
    def  nbHabitantsConnu(self):
        if self.nbHabitants > 0:
            return True
        else:
            return False

    def categorie(self):

        if self.nbHabitants == 0:
            return "Categorie ?"
        elif self.nbHabitants < 500000:
            return "Categorie A"
        else:
            return "Categorie B"

    def __str__(self):
        return "Nom de la Ville :" + self.nom + "\n" " Nombre de population : " + str(self.nbHabitants)


