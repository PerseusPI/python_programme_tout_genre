
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
    print("Vous vous appelez " + str(nomUser) + " vous avez "+ str(ageUser) +" ans")
    if ageUser >= 18:
        print("Vous etes majeur en france")
    else:
        print("Vous etes mineur en france")

nomUser = demander_nom()
ageUser = demander_age(nomUser)


#afficher resultats
afficher_info(nomUser, ageUser)
