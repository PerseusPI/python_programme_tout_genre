
def afficher_table(n, operateur_str, operation_cbk):
    print(f"table de {n} : ")
    for i in range(0,11):
        print(i, operateur_str, n,"= ",operation_cbk(i,n))




afficher_table(2, "x", lambda a, b : a * b)
print()
afficher_table(3, "+", lambda a, b : a + b)
print()
afficher_table(4, "-", lambda a, b : a - b)
print()
afficher_table(5, "/", lambda a, b : a / b)
print()
afficher_table(6, "^", lambda a, b : pow(a,b))
