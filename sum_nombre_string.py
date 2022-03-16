def sum_string(k: str) -> int:
    return sum(int(i.strip(".")) or int(i.strip(",")) for i in k.split() if i.strip(".").isdigit() or i.strip(",").isdigit())


k = "La première usine dispose de 32469 employés. La deuxième usine en compte 529. L'unité de Los Angeles dispose quant à elle de 918 employés."
print(sum_string(k))
