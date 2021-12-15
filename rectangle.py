# Dépendances
from ma_rue import rue, affiche

# Définitions

# Fonction rectangle()
def rectangle(x,y,w,h,c):
    '''
    Dessine un rectangle avec un contour noir et rempli de la couleur passée en paramètre
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
        c : couleur du remplissage
    '''
    rue.fill_style = c
    rue.fill_rect(x-(w/2), y-h, w, h)
    rue.fill_style = "black"
    rue.stroke_rect(x-(w/2), y-h, w, h)
    
# tests    
if __name__ == '__main__':
    affiche(rue)
    rectangle(0, 50,200,100,'YellowGreen')
    rectangle(800, 450,200,100,'plum')
    rectangle(400, 250,200,100,'SkyBlue')
    rectangle(400, 250,100,50,'salmon')