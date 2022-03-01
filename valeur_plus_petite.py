def trouver_minimum(listeUser:list) -> int or float:
    min = listeUser[0]
    for i in range(0, len(listeUser) - 1):
        if listeUser[i] < min:
            min = listeUser[i]
    return min


di = [1.5,2.2,0.4,0.9,7.1,0.2,10]
print(trouver_minimum(di))
