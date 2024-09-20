import matplotlib.pyplot as plt
import numpy as np

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