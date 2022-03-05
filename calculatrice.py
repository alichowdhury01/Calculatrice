#Fonction calculatrice
def calculatrice(a, b, c, d):
    #Partie addition
    adition = a/b + d/c
    #Partie soustration
    soustraction = a/b - d/c
    #Partie multiplication 
    multiplication = a/b * d/c
    #Partie division 
    divisions = a/b / d/c
    #Retoune chaque valeur des operations
    return adition, soustraction, multiplication, divisions
#Affriche la function calculatrice en attribuent le int disiré dans le print aux paramètre de la function 
print(calculatrice(2, 1, 8, 4))