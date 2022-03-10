def extraire(extension: list[str], definition: tuple[tuple[str]]) -> str:
    l = [i.split(".") for i in extension]
    d = [i[0].lower() for i in definition]
    for i in range(len(l)):
        if l[i][-1].lower() in d:
            for j in definition:
              #retirer les lower() si vous voulez exactement le meme nom dans def extensions et vos extensions ici EXE == exe si vous retirer EXE != exe
                if j[0].lower() == l[i][-1].lower():
                    print(f"{extension[i]} ({j[-1]})")
        elif not (l[i][-1].lower() in d) and len(l[i]) > 1:
            print(f"{extension[i]} (Extension Inconnu)")
        else:
            print(f"{extension[i]} (Aucune Extension)")


extensions = ["notepad.dat", "data.exe", "planning.txt", "vac", "intra.txt", "moc.exe"]

definitions_extensions = (
    ("exe", "Executable"),
    ("doc", "Document word"),
    ("txt", "Document texte"),
    ("jpeg", "Image JPEG")
)

extraire(extensions, definitions_extensions)
