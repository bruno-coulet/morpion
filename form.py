import matplotlib.pyplot as plt

def draw_cross(x, y, taille=0.9, couleur='red', epaisseur=5):

    offset = taille / 2
    
    plt.plot([x - offset, x + offset], [y - offset, y + offset], color=couleur, lw=epaisseur)
    
    plt.plot([x - offset, x + offset], [y + offset, y - offset], color=couleur, lw=epaisseur)

def draw_cercle(x, y, taille=0.9, couleur='blue', epaisseur=5):
    
    cercle = plt.Circle((x, y), radius=taille / 2, edgecolor=couleur,facecolor='none', lw=epaisseur)
    
    plt.gca().add_patch(cercle)





