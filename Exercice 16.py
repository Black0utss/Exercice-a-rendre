# Saisie des mots
first = raw_input("Veuillez saisir un premier mot ").upper()
second = raw_input("Veuillez saisir deuxieme mot ").upper()

# Fonction dist_hamming mesure le nombre de caractere entre les 2 mots et  affiche cette difference
def dist_hamming (first,second):
    distance = 0    # On definis la variable de depart
    for i in range(0, len(first)):  # On effectue une boucle de 0 a la longueur d'un des mots
        if first[i] != second[i] :
          distance = distance +1    # Si il y a des differences de caractere on ajoute 1 a distance et on affiche cette distance
    print ('la distance entre deux mots est de ' + str(distance))

#   On test si la longueur des 2 chaines est equivalente
#   Peut etre ameliorer car on multiplie les demandes de saisie, il faut integre la premiere demande dans le while
while len(first) != len(second):
    print ("Attention veuillez saisir 2 mots de meme longueur")
    first = raw_input("Veuillez saisir un premier mot ")
    second = raw_input("Veuillez saisir deuxieme mot ")

dist_hamming(first, second) #appelle de la fonction dist_care avec en parametre first et second
