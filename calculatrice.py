#Exercice 2, Partie 1:

#Fonction calculatrice:
def calculatrice(a, b, c, d):
    #Partie addition:
    adition = a/b + d/c
    #Partie soustration:
    soustraction = a/b - d/c
    #Partie multiplication:
    multiplication = a/b * d/c
    #Partie division:
    divisions = a/b / d/c
    #Retoune chaque valeur des operations:
    return adition, soustraction, multiplication, divisions
#Affriche le résultat de la function calculatrice en attribuent les int disiré dans les paramètres de la function:
print(calculatrice(2, 1, 8, 4))