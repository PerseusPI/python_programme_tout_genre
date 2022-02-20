import random as rd

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4

def poser_question():
    a = rd.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = rd.randint(NOMBRE_MIN, NOMBRE_MAX)
    operateur = rd.randint(0,1)

    if operateur == 1:
        operateur = "*"
        resultat = a*b
    
    else:
        operateur = "+"
        resultat = a+b
    
    nbreUser = int(input(f"Calculer {a} {operateur} {b} = "))
    
    if nbreUser == resultat:
        print("Correct")
        return True
    
    else:
        print("incorrect")
        return False

nb_point = 0
for i in range(NB_QUESTIONS):
    print(f"Questions n° {i + 1} sur {NB_QUESTIONS}")
    reponse = poser_question()
    if reponse == True:
        nb_point += 1
    print()
print(f"votre note est {nb_point}/{NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_point == NB_QUESTIONS:
    print("Excellent")
elif nb_point == 0:
    print("Révisez vos maths !")
elif nb_point > moyenne:
    print("Pas mal")
elif nb_point == moyenne:
    print("Vous avez la moyenne")
elif nb_point < moyenne:
    print("Peut mieux faire")
