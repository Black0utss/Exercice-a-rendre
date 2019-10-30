#Palindrome
#   Saisie du mot
first = raw_input("Veuillez saisir un premier mot ")

#   Fonction Palindrome qui mesure la longueur de la chaine et test si le caractere i et sont inverse -1-i identique
def palindrome(first) :
    for i in range(len(first)):
        if first[i] != first[-1-i]:
            print ("non ce n est pas un palindrome")
            return  #   Le mot n est pas un palindrome pas la peine de continuer

    print ("Whoa harry mais c est un palindrome 2000")

#   Appelle fonction
palindrome(first)

