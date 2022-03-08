def dichotomie(nbreATrouver:int, liste: list[int]) -> bool:
    liste.sort()
    debut = 0
    fin = len(liste) - 1
    milieu = 0
    trouver = False
    while debut <= fin and trouver == False:
        milieu = (debut + fin) // 2
        if liste[milieu] == nbreATrouver:
            trouver = True
        elif liste[milieu] > nbreATrouver:
            fin = milieu - 1
            milieu = (debut + fin) // 2
        else:
            debut = milieu + 1
            milieu = (debut + fin) // 2
    return trouver

print(dichotomie(4, [1,2,3,4,8]))
