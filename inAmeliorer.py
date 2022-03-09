def element_dans_liste(element: str, liste: list[str]) -> bool:
    liste_lower = [i.lower() for i in liste]
    return element.lower() in liste_lower


noms = ["Jean", "Sophie", "Martin", "Christophe" , "Zoe", "Martin"]

if element_dans_liste("jean",noms):
    print("Jean est là")
else:
    print("pas la")
