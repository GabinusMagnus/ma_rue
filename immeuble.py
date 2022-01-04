# Dépendances
from ma_rue import rue, affiche
from couleur_aleatoire import couleur_aleatoire
from rdc import rdc
from etage import etage
from toits import toits
from random import randint

# Définitions

def immeuble(x):
    '''
    Dessine un immeuble selon les règles urbanistiques imposées
    
    Paramètres
        x : abscisse du milieu de la base de l'immeuble
        
    '''
    # Nombre d'étage (aléatoire)
    nombre = randint(1, 4)
    
    #Couleur facade (aléatoire)
    couleur = couleur_aleatoire()
    
    # Dessin du RDC
    rdc(x, couleur)

    # Dessin des étages
    for i in range (nombre):
        etage(x, couleur, 1+i)
    

    # Dessin du toit
    toits(x, nombre+1)
    
# Tests
if __name__ == '__main__':
    affiche(rue)
    immeuble(rue.width/3)
    immeuble(2*rue.width/3)