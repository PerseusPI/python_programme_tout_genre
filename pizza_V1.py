def afficher(collection:list, nb_pizza_afficher:int = 0) -> str:
    if len(collection) != 0:
        collection.sort()
        print(f"---- LISTE DES PIZZAS ({len(collection)}) ----")
        if nb_pizza_afficher > 0:
            print(*collection[:nb_pizza_afficher], sep='\n')
        else:
            print(*collection, sep='\n')
        print()
        print(f"Première pizza : {collection[0]}")
        print(f"Dernière pizza : {collection[-1]}")
    else:
        print("AUCUNE PIZZA")


def ajouter_pizza_user(collection:list) -> input:
    ajoutUser = input("Pizza à ajouter: ")
    if ajoutUser.lower() in collection:
        print("ERREUR PIZZA déjà dans la liste")
        return 
    else:
        collection.append(ajoutUser)




pizzas = ["4 fromages","végetarienne","hawai","calzone"]

afficher(pizzas,3)
ajouter_pizza_user(pizzas)
afficher(pizzas)
