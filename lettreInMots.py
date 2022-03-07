def lettreInMots(noms: (str or list[str]) ,lettre: str) -> bool:
    lettrePres = [True if lettre.lower() in mots.lower() else False for mots in noms]
    return any(lettrePres)



noms = ["Hello", "Sophie", "Machin"]
print(lettreInMots(noms, "h"))
