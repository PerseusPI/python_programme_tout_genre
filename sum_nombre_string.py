k = "La première usine dispose de 324 employés. La deuxième usine en compte 529. L'unité de Los Angeles dispose quant à elle de 918 employés."
l = sum(int(i.strip(".")) for i in k.split() if i.strip(".").isdigit())
print(l)
