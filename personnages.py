import random

sexe = ["Homme", "Femme"]

prenom_masculin = ["Louis","Abdoul","Clément","Pierre","Gaston",
                   "Mathis","Alexendre","Loïc","Philippe","Pedro",
                   "Frédéric","André","Carl","Thomas","Mathieu",
                   "John","IbrahimbapenMohamedAlMustapha"]

prenom_feminin = ["Inès","Romane","Valentine","coralie","Marie-France",
                  "Nathalie","Anne","Christine","Stéphanie","Léa",
                  "Catherine","Aya","Isabelle","Geronima","Patricia",
                  "Emmy","Fatima"]

nom = ["Murphy"]

talent = ["rien","sportif","chant","acteur","criminel","politique"]

pays = {"France":["Paris","Toulouse","Marseille"]}

age = (0)

argent = (0)

print(age +1, random.choice(list(prenom_feminin)))
print(random.choices(list(talent),weights=(0.5,0.1,0.1,0.1,0.1,0.1)))
for valeur in pays.values():
    print(valeur[0])



