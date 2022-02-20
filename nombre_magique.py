import random as rd

NOMBRE_MIN = 1
NOMBRE_MAX = 10
nombre_vie = 5
NOMBRE_MAGIQUE = rd.randint(NOMBRE_MIN, NOMBRE_MAX)
print(f"Vous avez {nombre_vie} vies")
print(NOMBRE_MAGIQUE)


def verif(nbreUser):
    test = False
    while test != True:
        try:
            nbreUser = int(nbreUser)
            test = True
        except:
            print("ERROR ! Il faut entrez un nombre")
            nbreUser = input("rentrez un nombre compris entre 1 et 10 : ")
    return nbreUser


def demander_nombre(nbre_min, nbre_max):
    nbreUser = input("rentrez un nombre compris entre 1 et 10 : ")
    nbreUser = verif(nbreUser)
    while nbre_min > nbreUser or nbreUser > nbre_max:
        nbreUser = input("rentrez un nombre compris entre 1 et 10 : ")
        nbreUser = verif(nbreUser)

    return nbreUser


nbreUser = 0
while nbreUser != NOMBRE_MAGIQUE:
    nbreUser = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    if nbreUser > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        nombre_vie-=1
        print(f"Il vous restes {nombre_vie} vies")
    
    elif nbreUser < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")
        nombre_vie-=1
        print(f"Il vous restes {nombre_vie} vies")
    else:
        print(f"Bravo ! Vous avez gagné, il vous restait {nombre_vie} vies")
        if nombre_vie == 5:
            print("C'est un sans fautes")
    if nombre_vie == 0:
        print("Plus de vie ! Game Over")
        break
