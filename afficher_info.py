
#demander l'age
def demander_age(nomUser):
    age = 0
    while age == 0:
        age_str = input(str(nomUser) + " quel est votre age ? ")
        try:
            age = int(age_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return int(age)


#demander le nom
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom ? ")
    return str(nom)


#afficher informations
def afficher_info(nomUser, ageUser):
    return "Vous vous appelez " + str(nomUser) + " vous avez "+ str(ageUser) +" ans"


nomUser = demander_nom()
ageUser = demander_age(nomUser)


#afficher resultats
print(afficher_info(nomUser, ageUser))
