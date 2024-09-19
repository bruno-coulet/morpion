import numpy as np
import matplotlib.pyplot as plt

# Grille de jeu
def grid_draw():
    plt.figure()

    plt.plot([0, 3], [2, 2], 'k')  # x
    plt.plot([0, 3], [1, 1], 'k')  # x
    plt.plot([1, 1], [0, 3], 'k')  # y
    plt.plot([2, 2], [0., 3], 'k')

    plt.show()