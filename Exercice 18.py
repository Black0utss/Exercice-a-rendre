# -*- coding: utf-8 -*-
#Cluedo
#Initialisation tableau

profil = [('Colonel Moutarde', 'CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAA'), ('Mlle Rose', 'CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN'), ('Mme Pervenche', 'AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN'), ('M. Leblanc', 'CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG')]

def enquete (adn) :

    # Initialisation variable
    data1 = "CATA"
    data2 = "ATGC"
    datall1 = "CATATGC"
    datall2 = "ATGCATA"

    for i in range (0,len(profil)):
        if profil[i][1].count(data1) != 0 and profil[i][1].count(data2) != 0 and (profil[i][1].count(datall1) + profil[i][1].count(datall2)) == 0:
            print (profil[i][0] + " est coupable")
            return
        else:
            print (profil[i][0] + " est innocent")

cremier = enquete(profil)
