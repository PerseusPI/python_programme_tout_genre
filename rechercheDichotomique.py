def dichotomie(a: int, l: list) -> bool:
    l.sort()
    debut = 0
    fin = len(l) - 1
    milieu = 0
    while debut <= fin:
        milieu = (debut + fin) // 2
        if l[milieu] == a:
            return True
        elif l[milieu] > a:
            fin = milieu - 1
            milieu = (debut + fin) // 2
        else:
            debut = milieu + 1
            milieu = (debut + fin) // 2
    return False
print(dichotomie(9,[1,4,3,2,9]))
