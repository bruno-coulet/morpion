import matplotlib.pyplot as plt
from module.grid_draw import grid_draw


def draw_cross(taille=0.9, couleur='red', epaisseur=5):

    x = int(input("Choisissez la colonne du x: ")) - 1
    y = int(input("Choisissez la ligne du x: ")) - 1
    offset = taille / 2
    
    plt.plot([x - offset, x + offset], [y - offset, y + offset], color=couleur, lw=epaisseur)
    
    plt.plot([x - offset, x + offset], [y + offset, y - offset], color=couleur, lw=epaisseur)

 

def draw_circle(taille=0.9, couleur='blue', epaisseur=5):

    x = int(input("Choisissez la colonne du o : ")) - 1
    y = int(input("Choisissez la ligne du o : ")) - 1
    cercle = plt.Circle((x, y), radius=taille / 2, edgecolor=couleur,facecolor='none', lw=epaisseur)
    
    plt.gca().add_patch(cercle)
