def questionnaire(pays, ville1, ville2, ville3, ville4, bonne_reponse):
    global score
    print(f"Question : Quelle est la capitale de la/le/l' {pays} ?")
    print(f"(a) {ville1}")
    print(f"(b) {ville2}")
    print(f"(c) {ville3}")
    print(f"(d) {ville4}")
    
    choixUser = input("Votre réponse : ")
    
    if choixUser == bonne_reponse:
        print("Bonne réponse")
        score+=1
    else:
        print("Mauvaise réponse")
    #score+=1 if choixUser == bonne_reponse else print("Mauvaise réponse")
    print()

score = 0

questionnaire("France", "Marseille", "Nice" , "Paris", "Nantes", 'c')
questionnaire("Italie", "Turin", "Rome" , "Florence", "Venise", 'b')

print(f"Votre score est de : {score}")
