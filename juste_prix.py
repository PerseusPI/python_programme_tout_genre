import random as rd

juste_prix_find = rd.randint(1,40000)

        
def juste_prix():
    while True:
        nbreUser = input("Entrez un nombre : ")
        try:
            nbreUser = int(nbreUser)
        except:
            print("Error ! il faut rentrez un nombre entier")
        else:
            return nbreUser



petit = int(juste_prix_find / 2)
grand = int(juste_prix_find * 2)
print(f"le prix se situe entre {petit} et {grand}")
nbreUser = 0
test = True
while test == True:
    nbreUser = juste_prix()
    if nbreUser > juste_prix_find:
        print("le nombre est plus petit")
    elif nbreUser < juste_prix_find:
        print("Le nombre est plus grand")
    else:
        print("Bravo")
        test = False
    
