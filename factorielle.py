#Solution non récursive
"""def factorielle(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res
"""
#solution récursive
def factorielle(n):
    if n < 1:
        return 1
    else:
        return n * factorielle(n-1) 
print(factorielle(100))
