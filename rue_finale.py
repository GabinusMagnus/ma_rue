# Dépendances
from sol import sol
from immeuble import *

# Définitions


def rue_finale(canvas):
    
    # Affichage de ma rue
    affiche(canvas)

    # Dessin des immeubles
    a = 0
    for loop in range (4):
        immeuble(115+a)
        a = a+190

    # Dessin du sol de la rue
    sol()
    
# Tests
if __name__ == '__main__':
    rue_finale(rue)