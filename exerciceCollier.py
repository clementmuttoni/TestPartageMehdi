# -*-coding: iso-8859-1 -*-
""" Ce fichier contient le code du module 1 (collier de perles)"""

import os
from fonctionsModuleCollier import *

#Déclaration des variables de départ : 
Nombre_perles_exercice = 5 #Le nbr de perles doit pouvoir être paramétrable

afficheCours()

dict_voyelles = dict()
dict_voyelles = {'O': "Rouge", 'E': "Gris", 'A': "Vert", 'U':"Bleu", 'I':"Jaune", 'é':"Marron"} # On utilise la voyelle comme clé !

print("\n")

i=0
reponse= str()
while i < Nombre_perles_exercice: # Tant que i est strictement inférieur à ...
    v = voyelle_alea()
    print("De quelle couleur est {0} ? (Rouge,Gris,Vert,Bleu, Jaune ou Marron ?)".format(v))
    reponse = raw_input()
    if reponse == dict_voyelles[v]:
        i=i+1
        print("Oui !  C'est ça !")
    else: 
        print("Faux! {0} est {1} ! Recommencez".format(v,dict_voyelles[v]))
print("Bravo, tu as réussi l'exercice ! ")
		


		

os.system("pause")
