def sum_string(k: str) -> int:
    return sum(int(i.strip(".") or i.strip(",")) for i in k.split() if (i.strip(".") or i.strip(",")).isdigit())


k = "j'ai 100 bonbon j'enleve 50 bonbons il m'en reste 50, je suis 150."
print(sum_string(k))
