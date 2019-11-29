
class Acteur :

    def __init__(self,nom,prenom,pe=[]):
        self.nom = nom
        self.prenom = prenom
        self.perso = pe

    def get__nom(self):
        return self.nom
    def set__nom(self,nom):
        self.nom = nom

    def get__prenom(self):
        return self.prenom
    def set__prenom(self,prenom):
        self.prenom = prenom

    def get__perso(self):
        return self.perso
    def set__perso(self, pe):
        self.perso = pe

    def nbPersonnage(self):
        return len(self.perso)

    def malisttostr(self):
        chainestr = ""
        for i in self.perso:
            chainestr += i.__str__()
        return chainestr

    def __str__(self):
        return "Nom de l'instance : Acteur "+ "\n"  "Nom Acteur : " + str(self.nom) + "\n"  "Prenom Acteur :" + str(self.prenom) +"\n" "Personnage jouer : " + self.malisttostr() + "\n" "Le nombre de personage incarnee par " + (self.prenom) + " " + (self.nom) + " est de " + str(self.nbPersonnage())
