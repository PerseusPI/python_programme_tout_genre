def trouver_minimum(listeUser:list) -> int or float:
    listeUser.sort()
    min = listeUser[len(listeUser) - 1] + 1
    for i in range(0, len(listeUser) - 1):
        if listeUser[i] < min:
            min = listeUser[i]
            print(f"max: {min}")
    return min


di = [1.5,2.2,0.4,0.9,7.1,1.1,10]
print(trouver_minimum(di))
