import matplotlib.pyplot as plt
import numpy as np
from modules.desinee_grid import draw_board, draw_cercle, draw_cross  
from modules.verif_board import is_winner, draw_mark, is_board_full

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