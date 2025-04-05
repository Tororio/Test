"""
Seance 1
age = 12
nom = "amine"
taille = 1.78
est_etudiant = False or True
print(age, nom, est_etudiant)
print(type(nom))
"""

""""
"Liste = ["algebre", "Zoolo", "analyse", "proba", "prog"]
print(Liste)
#print(type(Liste))
Liste.append("ho")
print(Liste)
Liste.remove("ho")
print(Liste)
"""


""""
""   seance 3 ""

"fruits = ["Pomme", "Banane", "Orange"]
print(fruits)
fruits.append("Kiwi")
print(fruits)
del fruits[2]
print(fruits)
fruits[1] = "Ananas"
print(fruits)
print(len(fruits))
fruits.sort()
print(fruits)
"""

""""
"dico = {"amine": "12", "Mht" : "10"}
print(dico)
print(dico["amine"])

if "amine" in dico :
    print(dico["amine"])
else :
    print("non trouvé")
# print(dico.get('amine', 'non trouvé'))
print(dico.keys())
print(dico.values())
print(dico.items())"
"""

"""
fruits_dico = {"Pomme" : "Rouge", "Banane" : "Jaune", "Orange" : " Orange"}
fruits_dico["Kiwi"] = "Vert"
print(fruits_dico)
couleur_banane = fruits_dico["Banane"]
#print(fruits_dico["Banane"])
print(couleur_banane)
fruits_dico["Pomme"] = "Vert"
print(fruits_dico)
del fruits_dico["Banane"]
print(fruits_dico.keys())"
"""


""""
"3EME PArtie""

jour = "samedi"

match jour :
    case "Lundi" :
        print("Lundi")
    case "Mardi" :
        print("Mardi")
    case "samedi" :
        print("Bravo : ", jour)
    case _:
        print("Putain !")"

n1 = int(input("Saisir n1 : "))
n2 = input("saisir n2 : ")
print(n2.isnumeric)
print(n1.isnumeric)"
"""
##from Hello import Banque
##Banque.SolderUnCompte

"""
import requests
resultat = requests.get("http://google.fr")
resultat.text


import requests

response = requests.get('https://www.example.com')
print(response.status_code)
"""
import os
print(os.getcwd())


"""
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')
"""


fic = open("Python.txt", "w")
fic.write("Hey à tout le monde")
fic.close()



fic = open("Python.txt", "r+")
conte = fic.read()
print(conte)
# fic.close()

if fic.close() :
    print("fichier fermé")
else :
    print("fichier ouvert")

print("la fin de ma modif")