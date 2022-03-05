def calculatrice(a, b, c, d):
    adition = a/b + d/c
    soustraction = a/b - d/c
    multiplication = a/b * d/c
    divisions = a/b / d/c
    return adition, soustraction, multiplication, divisions
print(calculatrice(2, 1, 8, 4))