import pytest
import numpy as np
from modules.verif_board import is_winner  

def test_winner_row():
    # Caso de prueba: Ganador en una fila
    board = np.array([
        ['X', 'X', 'X'],
        ['O', 'O', 'X'],
        ['O', 'X', 'O']
    ])
    assert is_winner(board, 'X') == True

def test_winner_column():
    # Cas de test : Gagnant dans une colonne
    board = np.array([
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['X', 'O', 'X']
    ])
    assert is_winner(board, 'X') == True

def test_winner_diagonal():
    # Test case : Gagnant sur une diagonale
    board = np.array([
        ['X', 'O', 'O'],
        ['O', 'X', 'O'],
        ['O', 'O', 'X']
    ])
    assert is_winner(board, 'X') == True

def test_no_winner():
    # Test de cas : pas de gagnant
    board = np.array([
        ['X', 'O', 'O'],
        ['O', 'X', 'X'],
        ['X', 'O', 'O']
    ])
    assert is_winner(board, 'X') == False

def test_tie():
    # Cas de test Tie
    board = np.array([
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ])
    assert is_winner(board, 'X') == False 

