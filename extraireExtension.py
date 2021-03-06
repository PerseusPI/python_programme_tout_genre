def extraire(extension: list[str], definition: tuple[tuple[str]]) -> list[str]:
    l = [i.split(".") for i in extension]
    d = [i[0].lower() for i in definition]
    res = []
    for i in range(len(l)):
        if l[i][-1].lower() in d:
            for j in definition:
                 #retirer les lower() si vous voulez exactement le meme nom dans def extensions et vos extensions ici EXE == exe si vous retirer EXE != exe
                if j[0].lower() == l[i][-1].lower():
                    res.append(f"{extension[i]} ({j[-1]})")
        elif not (l[i][-1].lower() in d) and len(l[i]) > 1:
            res.append(f"{extension[i]} (Extension Inconnu)")
        else:
            res.append(f"{extension[i]} (Aucune Extension)")
    return res


extensions = ["notepad.exe", "data.txt", "planning.doc", "vacances.jpeg", "intra", "virus.exe"]

 #ajouter d'autre extensions si vous le souhaiter
definitions_extensions = (
    ("exe", "Executable"),
    ("doc", "Document word"),
    ("txt", "Document texte"),
    ("jpeg", "Image JPEG")
)

res = extraire(extensions, definitions_extensions)
for i in res:
    print(i)
          

