class Personnage :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get__nom(self):
        return self.nom
    def set__nom(self,nom):
        self.nom = nom
    def get_prenom(self):
        return self.prenom
    def set_prenom(self,prenom):
        self.prenom = prenom
    def __str__(self):
        return "Nom de l'instance : Personnage "+ self.nom + self.prenom