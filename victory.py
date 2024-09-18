import numpy as np
import matplotlib.pyplot as plt

# Grille vide
# grid = np.ones((3,3), dtype=int)
# print(grid)

# grille de test
grid = [[1, 1,'o'],
 [1,'o', 1],
 ['o', 1, 1]]

x=0
o=0
winner = None
print(f'au départ, x = {x}')
print(f'au départ, o = {o}')

def victory():
    
    global x, o, winner
    # meme symbole sur toute une ligne
    for row in grid:
        if all(case == 'x' for case in row):
            x += 3
        if all(case == 'o' for case in row):
            o += 3
    # meme symbole sur toute une colonne, len(grid) = 3
    for column in range(3):
        if all(row[column] == 'x' for row in grid):
            x += 3
        if all(row[column] == 'o' for row in grid):
            o += 3
    # meme symbole sur  une diagonale
    if all(grid[i][i] == 'x' for i in range(len(grid))):
        x += 3
    if all(grid[i][i] == 'o' for i in range(len(grid))):
        o += 3
    if all(grid[i][len(grid)-1-i] == 'x' for i in range(len(grid))):
        x += 3
    if all(grid[i][len(grid)-1-i] == 'o' for i in range(len(grid))):
        o += 3
    
    if o == 3:
        print("Joueur o à gagné")
        winner = 'joueur o'
        return winner
    
    if x == 3:
        print("Joueur x à gagné")
        winner = 'joueur x'
        return winner



victory()
print (f'grid : {grid}')
print(f'à la fin, x : {x}')
print(f'à la fin, o : {o}')
