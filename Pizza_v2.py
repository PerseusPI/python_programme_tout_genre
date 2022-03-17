class Pizza:
    def __init__(self, nom, prix, ingredients, vege=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vege = vege

    def AfficherPizza(self):
        pizza = ""
        if self.vege:
            pizza += "- vegetarienne"
        print(f"PIZZA {self.nom} : {self.prix} euros {pizza}")
        print(", ".join(self.ingredients))
        
        
class PizzaPersonnaliser(Pizza):
    numero = 0
    def __init__(self,nom,prix):
        super().__init__(nom, prix, False)
        PizzaPersonnaliser.numero += 1
        self.numero = PizzaPersonnaliser.numero
        self.ingredients = []
    def AfficherPizza(self):
        d = int(input(f"Combien voulez vous d'ingredients pour la pizza numero {self.numero}: "))
        self.ingredients = [int(input("""ingredients : 
                                              Liste Ingredients:
                                              - Brie (taper 1[reference de l'ingredient])
                                              - emmental(taper 2[reference ""])
                                              - tomate (taper 3[reference ""]) 
                                              Votre choix : """)) 
        for i in range(d)]

        for i in range(len(self.ingredients)):
            if self.ingredients[i] == 1:
                self.prix += 1
                self.ingredients[i] = "Brie"
            
            elif self.ingredients[i] == 2:
                self.prix += 2
                self.ingredients[i] = "Emmental"
            
            else:
                self.prix += 0.50
                self.ingredients[i] = "Tomate"
        super().AfficherPizza()


pizzas = [
    Pizza("4 fromages", 10.5, ("brie", "emmental", "comté", "tomate"), True),  
    Pizza("Vege", 9.5, ("brie", "emmental"), True),  
    Pizza("cannibal", 8, ("emmental",))
]




pizzas.sort(key=lambda e : e.prix)
print()
for i in pizzas:
    pizzaPerso = PizzaPersonnaliser("4 fromages", 10.5)
    pizzaPerso.AfficherPizza()
