import matplotlib.pyplot as plt
import numpy as np

def draw_cross(x, y, taille=0.9, couleur='red', epaisseur=5):

    offset = taille / 2
    plt.plot([x - offset, x + offset], [y - offset, y + offset], color=couleur, lw=epaisseur)
    plt.plot([x - offset, x + offset], [y + offset, y - offset], color=couleur, lw=epaisseur)

def draw_cercle(x, y, taille=0.9, couleur='blue', epaisseur=5):
    
    cercle = plt.Circle((x, y), radius=taille / 2, edgecolor=couleur,facecolor='none', lw=epaisseur)
    plt.gca().add_patch(cercle)
    
def draw_board():
    """Dessine le plateau de jeu ."""
    #plt.figure(figsize=(5, 5))
    #plt.axis('off')
    plt.plot([0, 3], [2, 2], 'k')
    plt.plot([0, 3], [1, 1], 'k')
    plt.plot([1, 1], [0, 3], 'k')
    plt.plot([2, 2], [0, 3], 'k')
    