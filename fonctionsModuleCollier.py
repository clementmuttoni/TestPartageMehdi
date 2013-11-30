# -*-coding: iso-8859-1 -*-
"""Ce fichier définit des fonctions utiles pour le programme exerciceCollier."""
 
import os
import random
 
 
 #Explication du code couleur :
def afficheCours():
	print("Voici le fonctionnement du code couleur : ")
	print("Une couleur est associée à chaque voyelle,\n -Le O est ROUGE \n -Le E est GRIS \n -Le A est VERT \n -Le U est BLEU \n -le I est JAUNE \n -Le é est MARRON")
	print("\n")
	print("\n")
	print("Nous allons maintenant commencer l'exercice : Collier de perles !")
	
	
#1 =>'O': "Rouge", 2=>'E': "Gris", 3=> 'A': "Vert", 4=> 'U':"Bleu", 5=>'I':"Jaune", 6=>'é':"Marron"

def voyelle_alea(): 
	n = random.randint(1,6)
	voyelle=''
	
	if n==1:
		voyelle='O'
	elif n==2:
		voyelle='E'
	elif n==3:
		voyelle='A'	
	elif n==4:
		voyelle='U'
	elif n==5:
		voyelle='I'
	else:
		voyelle='é'
  
	return voyelle
	