class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        print("Clonage de la personne")


    def SePresenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age}")
        if self.estMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
    
    
    def estMajeur(self):
        return self.age >= 18


personne1 = Personne("Sam", 17)
personne1.SePresenter()
