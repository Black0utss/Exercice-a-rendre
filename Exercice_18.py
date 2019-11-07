# -*- coding: utf-8 -*-
#Cluedo
#Initialisation variable
data1 = "CATA"
data2 = "ATGC"
datall1 = "CATATGC"
datall2 = "ATGCATA"

profil = [('Colonel Moutarde', 'CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAA'), ('Mlle Rose', 'CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN'), ('Mme Pervenche', 'AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN'), ('M. Leblanc', 'CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG')]

#Utiliser find(chaine de caractere) a lieu de count

def enquete (adn) :

    if adn.count(data1) != 0:
        print ("etape 1")
        if adn.count(data2) != 0:
            print ("coupable")
            return # a faire aved la list pour return le nom du coupable
        else:
            print ("innocent")
    else:
        print ("innocent")

def enquete2 (adn) :

    if adn.count(data1) and adn.count(data2) != 0:
            print ("coupable")
            return # a faire aved la list pour return le nom du coupable
    else:
        print ("innocent")

def enquete2_5 (adn) :

    if adn.count(data1) and adn.count(data2) != 0 and adn.count(datall1) == 0:
            print ("coupable")
            return # a faire aved la list pour return le nom du coupable
    else:
        print ("innocent")

def enquete3 (adn) :

    if adn.count(data1) != 0 and adn.count(datall1) == 0:
            print ("coupable")
            return # a faire aved la list pour return le nom du coupable
    else:
        print ("innocent")

def enquete4 (adn) :

    if adn.count(data1) != 0 and adn.count(datall1) ==0 and adn.count(datall2) == 0:
            print ("coupable")
            return # a faire aved la list pour return le nom du coupable
    else:
        print ("innocent")

cremier = enquete2_5('CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN')
# Pour l'instant le mieux est le 2_5