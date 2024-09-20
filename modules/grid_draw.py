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
    
def draw_mark(x, y, mark= 'X'):

    """Dessine une croix ou un cercle à la position spécifiée.
    Args:
        x (int): Coordonnée x de la case.
        y (int): Coordonnée y de la case.
        mark (str): 'X' ou 'O'.
    """
    if mark == 'X':
        draw_cross(x + 0.5, y + 0.5)
    elif mark == 'O':
        draw_cercle(x + 0.5, y + 0.5)

def is_winner(board, mark):
    """Verifica si jueur à gagne.

    Args:
        board (np.array): Matriz que representa el tablero.
        mark (str): 'X' o 'O'.

    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
    """

    # Verificar filas
    for row in range(3):
        if np.all(board[row] == mark):
            return True

    # Verificar columnas
    for col in range(3):
        if np.all(board[:, col] == mark):
            return True

    # Verificar diagonales
    if np.all(np.diag(board) == mark) or np.all(np.diag(np.fliplr(board)) == mark):
        return True

    return False

def is_board_full(board):
    """Verifica si el tablero de tic-tac-toe está completamente lleno.
    Args:
        board (np.array): Una matriz NumPy que representa el tablero de juego.
    Returns:
        bool: True si todas las casillas del tablero están ocupadas, False en caso contrario.
    """
    # Utiliza np.all() para verificar si todos los elementos del tablero son diferentes de vacío ('')
    return np.all(board != '')
def play_game():
    plt.ion()
    #fig, ax = plt.subplots(figsize=(5, 5))
    plt.figure(figsize=(5, 5))
    plt.axis('off')

    board = np.zeros((3, 3), dtype=str)
    player = 'X'
    draw_board()

    while True:
        while True:
            try:
                row, col = map(int, input("Entrez la ligne et la colonne (1-3): ").split())
                row -= 1
                col -= 1
                if 0 <= row <= 2 and 0 <= col <= 2:
                    break
                else:
                    print("nombres de 1 à 3.")
            except ValueError:
                print("nombres entiere.")

        if board[row, col] != '':
            print("Casee ocupée.")
            continue

        board[row, col] = player
        plt.clf()
        #ax.clear()
        draw_board()
        for i in range(3):
            for j in range(3):
                if board[i, j] == 'X':
                    draw_cross(j + 0.5, i + 0.5)
                elif board[i, j] == 'O':
                    draw_cercle(j + 0.5, i + 0.5)
        #fig.canvas.draw()
        plt.pause(0.1)
        #plt.show()
        if is_winner(board, player):
            print(f"¡El jugador {player} ha ganado!")
            break
        elif is_board_full(board):
            print("¡Empate!")
            break

        player = 'O' if player == 'X' else 'X'
    #plt.ioff()  # Desactive
    plt.show() 

play_game()