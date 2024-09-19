import numpy as np
import matplotlib.pyplot as plt

# Grille de jeu
grid = np.ones((3,3))
print(grid)

# Utiliser Pyplot pour dessiner les lignes de la grille.
def draw_grid():
    pass
# La case est-elle disponible ?
def available(grid):
    for row in grid:
        for case in row:
            if case == 1:
                return True
            else:
                return False
    


# fonction condition de victoire
def victory():
    pass

# Dessine une croix
def draw_cross():
    if case=0 alors tu peux mettre une croix
    pass

# dessine un rond
def draw_circle():
    pass

# alterner les joueurs
while not victoire and 0 in grid:
    joueur 1
else:
    joueur 2

