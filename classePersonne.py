class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        if nom == "":
            self.nom = self.demanderNom()
        self.age = age
        print("Clonage de la personne")


    def demanderNom(self):
        nameUser = input("Votre nom : ")
        return nameUser


    def SePresenter(self):
        if self.age == 0:
            print(f"Je m'appelle {self.nom}")
        else:
            print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
            if self.estMajeur():
                print("je suis majeur")
            else:
                print("Je suis mineur")

    

    def estMajeur(self):
        return self.age >= 18


personne1 = Personne("",18)
personne1.SePresenter()

