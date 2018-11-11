#!/usr/bin/env python3
# 1b_dic
# creer une liste des prenoms rentré
# 11/11/2018
# Bordas Matthieu
import re
# on creer une regex pour verifier l'entré utilisateur
reg = re.compile('^[a-zA-Z]+$')
# on creer notre fonction
def dic():
    prenoms = []
    prenom = input("lol entre tes trucs 1 par ligne\n")
    while prenom != "q":
        if reg.match(prenom):
            prenoms.append(prenom)
        else:
            print("n'est pas un prenom")
        prenom = input("")
    prenoms.sort()
    print(", ".join(prenoms))
#appele de la fonction
dic()
