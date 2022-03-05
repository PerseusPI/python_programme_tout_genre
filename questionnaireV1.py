def lancer_questionnaire(questionnaire:tuple) -> str:
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    return f"Votre score est de : {score}/{len(questionnaire)}"


def demander_reponse_user(min:int, max:int) -> int:
    choixUser = input(f"Votre réponse : entre {min} et {max} : ")
    try:
        choixUser = int(choixUser)
        if min <= choixUser <= max:
            return choixUser
    except:
        print("ERREUR ! Vous devez rentrer un nombre")
   
    return demander_reponse_user(min, max)


def poser_question(question:tuple) -> bool:
    reponseTest = False
    titre = question[0]
    choix = question[1]
    bonne_reponse = question[2]
    print(f"Question : " + titre)
    for i in range(len(choix) ):
        print(f"{i + 1} - {choix[i]}")
    choixUser = demander_reponse_user(1, len(choix))
    if choix[choixUser - 1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        reponseTest = True
    else:
        print("Mauvaise réponse")
    print()
    return reponseTest



questionnaire = (
    ("Quelle est la capitale de la France", ("Paris", "Nantes", "Lyon", "marseille"), "Paris"),
    ("Quelle est la capitale de l'Italie", ("turin", "Rome", "Naples", "Milan", "Vérone"), "Rome"),
    ("Quelle est la capitale de la belgique", ("Bruxelles", "Bruges", "Anvers", "Liège", "Spa", "Gand"), "bruxelles")
)

print(lancer_questionnaire(questionnaire))
