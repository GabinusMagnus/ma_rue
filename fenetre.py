# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle

# Définitions

# Fonction
def fenetre(x,y):
    '''
    Dessine une fenêtre de taille 30 pixels sur 30 pixels
    avec une vitre de couleur 'Azure' le jour
    et un contour noir. 
    Paramètres :
        x est l'abcisse du milieu de la base de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    '''
    rectangle(x, y, 30, 30, "Azure")
    
# Tests
if __name__ == '__main__':  
    affiche(rue)
    fenetre(rue.width/2,rue.height)