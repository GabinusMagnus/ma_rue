# Dépendances
from ma_rue import rue, affiche
from facade import facade
from fenetre import fenetre
from balcon import balcon 
from random import randint

# Définitions

# Fonction etage()
def etage(x, couleur, niveau):
    '''
    Dessine sur une facade un étage avec 3 éléments choisis aléatoirement
    parmi une fenêtre ou une porte fenêtre avec balcon.  
    
    Paramètres
        x : abscisse du milieu de la base de l'étage
        couleur : couleur fixée par l'immeuble
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    y = rue.height - niveau * 60 # ordonnée de la base de l'etage
    
    # Murs
    facade(x, couleur, niveau)
        
        
    # Eléments
    a = -40
    for loop in range (3):
        element = randint(1, 2)
        if element == 1:
            fenetre(x+a, y-20)
        elif element == 2:
            balcon(x+a, y)
        a = a+40
        
# Tests
if __name__ == '__main__':
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    couleur = couleur_aleatoire()
    for n in range(6) :
        etage(rue.width/2,couleur,n)