# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint

# Définitions

# Fonction portes()
def portes(x,y):
    '''
    Dessine une porte de 30 pixels en largeur et 50 pixels en hauteur
    La forme du haut de la porte est aléatoirement rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte  
    '''
    couleur = couleur_aleatoire()
    porte = randint(1, 2)
    if porte == 1:
        rectangle(x, y, 30, 50, couleur)
    
    elif porte == 2:
        rectangle(x, y, 30, 35, couleur)
        rue.fill_style = couleur
        rue.fill_rect(x-14, y-1, 28, -35)
        rue.fill_arc(x, y-35, 15, 0, pi, True)
        rue.stroke_style = "black"
        rue.stroke_arc(x, y-35, 15, 0, pi, True)
        
# Tests
if __name__ == '__main__':  
    affiche(rue)
    for i in range(21) :
        portes(0 + i * 40,rue.height)