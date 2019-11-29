class film :

    def __init__(self,a ="unknow",b = "unknow",c = 0,d = 0000, e = 0000, f =[]) :
        self.titre = a
        self.anneeSortie = b
        self.numerodepisode = c
        self.cout = d
        self.recette = e
        self.acteur = f


    def  get__Titre(self):
        return self.titre
    def set__Titre(self,a):
        self.titre = a

    def  get__AnneeSortie(self):
        return self.anneeSortie
    def set__AnneeSortie(self,b):
        self.anneeSortie = b

    def get__numerodepisode(self):
        return self.numerodepisode
    def set__numerodepisode(self,c):
        self.numerodepisode = c

    def  get__Cout(self):
        return self.cout
    def set__Cout(self,d):
        self.cout = d

    def  get__Recette(self):
        return self.recette
    def set__Recette(self,e):
        self.recette = e

    def set__Acteur(self, f):
        self.acteur = f
    def get_Acteur(self):
        return self.acteur

    def set_personnage(self,perso):
        self.personnage = perso
    def get_personnage(self):
        return self.personnage

    def malisttostr(self):

        chainestr = ""
        for i in self.acteur:
            chainestr += i.__str__()
        return chainestr

    def Estbeneficaireounon(self):
        resultat  = self.recette - self.cout
        if resultat < 0 :
            return [False, "Le film est en deficite de " + str(resultat)]
        else:
            return [True, "Le film est en benefice de " + str(resultat)]

    def isBefore(self):

         truc = int(input("Entrer une annee a tester"))
         if self.anneeSortie < truc :
             return True
        # else:
        #     return False

    def nbPersonnage(self):
        compteur = 0
        for i in self.acteur:
            compteur += i.nbPersonnage()
        return compteur

    def triacteur(self):
        sorted(self.acteur,key=lambda self:self.nom)
        return self.acteur


    def __str__(self):
        return "Nom de l'instance : Film" + "\n" "Titre du Film "+(self.titre) + "\n" " Annee de Sortie :" + str(self.anneeSortie) + "\n" " Cout :" + str(self.cout) + "\n" " Recette :" + str(self.recette) + "\n"  "Le nombre d acteur est de : " + str(len(self.acteur)/2) +"\n" "Le nombre de personnage est de " + str(self.nbPersonnage()) + " Compose de " + self.malisttostr() + "\n" + str(self.Estbeneficaireounon())