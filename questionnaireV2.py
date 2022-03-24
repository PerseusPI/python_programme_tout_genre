class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse


    def demander_reponse_numerique_utlisateur(self, min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return self.demander_reponse_numerique_utlisateur(min, max)


    def poser_questions(self):
        for i in range(len(self.choix)):
            print(" ", i+1, "-", self.choix[i])
        resultat_response_correcte = False
        reponse = self.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse-1].lower() == self.bonne_reponse.lower():
            resultat_response_correcte = True
        return resultat_response_correcte
        

class Questionnaire:
    def __init__(self, questions):
        self.questions = questions


    def lancer_questionnaire(self):
        score = 0
        for questions in self.questions:
            if questions.poser_questions():
                score+=1
        print("Score final :", score, "sur", len(self.questions))




questionnaire = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

                
q = Questionnaire(questionnaire)
q.lancer_questionnaire()
