import numpy as np
import random
import matplotlib.pyplot as plt


# les joueur n'ont aucun symbole aligné, il n'y a pas encore de gagnant
x=0
o=0
winner = None

# Initialise une grille  (3 lignes, 3 colonnes) de chiffres 1
grid = np.ones((3,3), dtype=int)


# Retourne winner= 'joueur o' ou  'joueur x' si un joueur à gagné (si x ou o = 3)
def victory():
        
    global x, o, winner
    # meme symbole sur toute une ligne
    for row in grid:
        if all(cell == 'x' for cell in row):
            x = 3
        if all(cell == 'o' for cell in row):
            o = 3
    # meme symbole sur toute une colonne, len(grid) = 3
    for column in range(3):
        if all(row[column] == 'x' for row in range(3)):
            x = 3
        if all(row[column] == 'o' for row in range(3)):
            o = 3
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
    
    if x == 3:
        print("Joueur x à gagné")
        winner = 'joueur x'

    return winner


# Crée les joueurs, sélectionne un joueur
players = ["joueur o", "joueur x"]
actual_player = random.randint(0, 1)
# print(f"C'est au tour de {players[actual_player]} de jouer.")


# Alterne les joueurs
def switch_player():
    global actual_player
    actual_player = 1 - actual_player  # Alterne entre 0 et 1
    print(f"Maintenant, c'est au tour de {players[actual_player]}.")


def draw_circle(x,y,taille=0.9, couleur='blue', epaisseur=5):

    # grid : lignes horizontales y=1 puis y=2
    plt.plot([0, 3], [1, 1], 'k')
    plt.plot([0, 3], [2, 2], 'k')
    # grid : lignes verticales x = 1 puis  x = 2
    plt.plot([1, 1], [0, 3], 'k')
    plt.plot([2, 2], [0., 3], 'k')

    cercle = plt.Circle((x, y), radius=taille / 2, edgecolor=couleur,facecolor='none', lw=epaisseur)
    
    plt.gca().add_patch(cercle)

def draw_cross(x,y,taille=0.9, couleur='red', epaisseur=5):

    offset = taille / 2

    # grid : lignes horizontales y=1 puis y=2
    plt.plot([0, 3], [1, 1], 'k')
    plt.plot([0, 3], [2, 2], 'k')
    # grid : lignes verticales x = 1 puis  x = 2
    plt.plot([1, 1], [0, 3], 'k')
    plt.plot([2, 2], [0., 3], 'k')
    
    plt.plot([x - offset, x + offset], [y - offset, y + offset], color=couleur, lw=epaisseur)
    plt.plot([x - offset, x + offset], [y + offset, y - offset], color=couleur, lw=epaisseur)


# dessine le symbole du joueur si la cell est vide
# def available(x,y):
#     # lignes
#     for x in range(grid.shape[0]):  
#         # colonnes
#         for y in range(grid.shape[1]):
#             if grid[x, y] == 1:
#                 available = True
#             else:
#                 available = False

#     if available and actual_player == 0:
#             draw_circle(x,y)
#     if available and actual_player == 1:
#             draw_cross(x,y)

#     if not available:
#         print("Ces coordonnées ne sont pas disponibles\nRéessayez !")
#         x = int(input("Choisissez la colonne : ")) -0.5
#         y = int(input("Choisissez la ligne : ")) -0.5

#     # return available

def is_available(x,y):
    return grid[x][y] == 1



# Si la cell est vide, dessine le symbole du joueur
def draw_symbol():

    global actual_player
    while True:
        try:
            x = int(input("Choisissez la colonne (1 à 3) : ")) -1
            y = int(input("Choisissez la ligne (1 à 3) : ")) -1

            # dessine le symbole du joueur si la case est libre
            if is_available(x,y):
                grid[y][x] = 'x' if actual_player ==1 else 'o'

                draw_x = x + 0.5
                draw_y = y + 0.5

                #  efface et redessine la grille
                plt.clf()
                plt.plot([0,3], [1,1], 'k')
                plt.plot([0,3], [2,2], 'k')
                plt.plot([1,1], [1,1], 'k')
                plt.plot([2,2], [0,3], 'k')


                if actual_player == 0:
                    draw_circle(draw_x,draw_y)
                else:
                    draw_cross(draw_x,draw_y)

                plt.axis('equal')
                plt.pause(0.1)
                # plt.show()
                break
            else:
                print("coordonnées indisponiubles, réessayez")
        except ValueError:
            print("Veuillez entrer un nombre entre 1 et 3")



    # x = int(input("Choisissez la colonne : ")) -0.5
    # y = int(input("Choisissez la ligne : ")) -0.5

    # available(x,y)

    # # if available :
    # #     if actual_player == 0:
    # #         draw_circle(x,y)
    # #     if actual_player == 1:
    # #         draw_cross(x,y)

    # # if not available:
    # #     print("Ces coordonnées ne sont pas disponibles\nRéessayez !")
    # #     x = int(input("Choisissez la colonne : ")) -0.5
    # #     y = int(input("Choisissez la ligne : ")) -0.5

#  active le mode interactif de matplotlib
plt.ion()
while winner is None:

    # Un joueur joueur joue puis on change de joueur
    print(f'actual_player : {actual_player}')

    draw_symbol()
    victory()
    if winner:
        break
    switch_player()

# désactive le mode interactif
plt.ioff()
#  affiche le pgraph final
plt.show()


