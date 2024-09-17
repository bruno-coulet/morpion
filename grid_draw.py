import numpy as np
import matplotlib.pyplot as plt

# Grille de jeu
plt.figure()

plt.plot([0, 0.8], [.55, .55], 'k')  # x
plt.plot([0, 0.8], [0.25, 0.25], 'k')  # x
plt.plot([0.25, 0.25], [0, 0.8], 'k')  # y
plt.plot([.55, .55], [0., 0.8], 'k')

plt.show()