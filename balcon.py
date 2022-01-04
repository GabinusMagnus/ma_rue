# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from trait import trait

# Définitions

# Fonction balcon()
def balcon(x,y):
    '''
    Dessine une porte fenêtre de largeur 30 pixels et 50 pixels en hauteur
    avec une vitre de couleur 'Azure' le jour au contour noir,
    devancé d'un balcon constitué de traits noirs d'épaisseur 3 pixels.
    Paramètres :
        x est l'abcisse du milieu de la base de la porte-fenetre
        y est l'ordonnée du sol du niveau de la porte-fenetre
    '''
    # porte-fenetre
    rectangle(x, y, 30, 50, "Azure")
    
    
    # balcon
    rue.line_width = 3
    rue.stroke_rect(x-20, y, 40, -25)
    for i in range(8):
        trait(x-20+5*i, y, x-20+5*i, y-25)
    rue.line_width = 1
    
# Tests
if __name__ == '__main__':
    affiche(rue)
    balcon(rue.width/2,rue.height)