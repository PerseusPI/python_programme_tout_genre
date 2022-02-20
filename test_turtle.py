import turtle

t = turtle.Turtle()

def creer_Escalier(taille,nb):
    for i in range(nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 10


def creer_carre(taille):
    for i in range(4):
        t.forward(taille)
        t.left(90)


def plusieurs_carree(taille_depart,nb):
    taille = 0
    for i in range(nb):
        creer_carre(taille)
        taille = taille_depart * (i + 1)


taille = 10

plusieurs_carree(taille,10)

creer_Escalier(taille,11)



turtle.done()
