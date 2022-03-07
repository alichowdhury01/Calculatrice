#Exercice 1:

#Function modulo:
from fractions import Fraction


def modulo(x):
    #retourne le paramètre de x modulo 5
    return x % 5
#le paramètre est 51
print(modulo(67))

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
print(calculatrice(8, 5, 76, 4))

#Exercice 2, Partie 2:

#Fonction calculatrice_2:
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


#Exercice 2, Partie 3:

#Fonction calculatrice_3:
def calculatrice_3(fraction1, fraction2):
    #Partie addition:
    adition = fraction1 + fraction2
    #Partie soustration:
    soustraction = (fraction1 - fraction2)
    #Partie multiplication:
    multiplication = fraction1 * fraction2
    #Partie division:
    divisions = fraction1 / fraction2
    #Retoune chaque valeur des operations:
    return adition, soustraction, multiplication, divisions
#Affriche le résultat de la function calculatrice3 en attribuent les int disiré dans les paramètres de la function:
print(calculatrice_3(float(3/4), float(67/23)))
print(calculatrice_3(Fraction('3/4'), Fraction('67/23')))



#Exercice 3:

#Fonction puissance:
def puissance(x, y=2, z=1):
    return x**y/z
   
#Affiche la fonction puissance avec les valeurs désiré pour les paramètre:
print(puissance(56, 5, 4))
print(puissance(56, 5))
print(puissance(56))
