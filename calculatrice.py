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

#Exercice 2, Partie 2:
def calculatrice_2(fraction1, fraction2):
    #Partie addition:
    adition = fraction1 + fraction2
    #Partie soustration:
    soustraction = fraction1 - fraction2
    #Partie multiplication:
    multiplication = fraction1 * fraction2
    #Partie division:
    divisions = fraction1 / fraction2
    #Retoune chaque valeur des operations:
    return adition, soustraction, multiplication, divisions
#Affriche le résultat de la function calculatrice2 en attribuent les int disiré dans les paramètres de la function:
print(calculatrice_2(2/5, 7/9))
