#Initialisation des variables de longueur inegale afin de rentrer dans la condition du While (line 14)
first = ""
second ="0"

# Fonction dist_hamming mesure le nombre de caractere entre les 2 mots et  affiche cette difference
def dist_hamming (first,second):
    distance = 0    # On definis la variable de depart
    for i in range(0, len(first)):  # On effectue une boucle de 0 a la longueur d'un des mots
        if first[i] != second[i] :
          distance += 1    # Si il y a des differences de caractere on ajoute 1 a distance et on affiche cette distance
    print ('la distance entre deux mots est de ' + str(distance))

#   On test si la longueur des 2 chaines est equivalente
#   Saisie des mots
while True  :
    if len(first) != len(second):
        print ("Attention veuillez saisir 2 mots de meme longueur")
        first = str(input("Veuillez saisir un premier mot ").upper().strip()  )  # On passe la chaine de caractere en majuscule et on supprime les espaces
        second = str(input("Veuillez saisir deuxieme mot ").upper().strip() )    # pour eviter tout erreurs
    else :
        break   #  longueur identique donc on quitte le while
dist_hamming(first, second) #appelle de la fonction dist_hamming avec en parametre first et second
