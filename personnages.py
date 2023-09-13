import random

age = 0

argent = 0

SEXES = ["Homme", "Femme"]
sexe = random.choice(SEXES)

PRENOM_MASCULIN = ["Louis","Abdoul","Clément","Pierre","Gaston",
                   "Mathis","Alexendre","Loïc","Philippe","Pedro",
                   "Frédéric","André","Carl","Thomas","Mathieu",
                   "John","IbrahimbapenMohamedAlMustapha"]

PRENOM_FEMININ = ["Inès","Romane","Valentine","coralie","Marie-France",
                  "Nathalie","Anne","Christine","Stéphanie","Léa",
                  "Catherine","Aya","Isabelle","Geronima","Patricia",
                  "Emmy","Fatima"]

if sexe == "Homme":
    prenom = random.choice(PRENOM_MASCULIN)
else:
    prenom = random.choice(PRENOM_FEMININ)

NOMS = ["Murphy"]

nom = random.choice(NOMS)

TALENTS = ["rien","sportif","chant","acteur","criminel","politique"]

talent = random.choices(TALENTS,weights=(0.5,0.1,0.1,0.1,0.1,0.1))

lieux = {"France":["Paris","Toulouse","Marseille"],
        "Angleterre":["Londre"],}

pays = random.choice(list(lieux.keys())) 
ville = random.choice(lieux[pays])  

print("Pays:", pays)
print("Ville:", ville)