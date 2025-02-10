import pytest
from tic_tac_toe import (
    print_board,
    check_winner,
    get_available_moves,
    player_move,
    computer_move,
    is_board_full
)

@pytest.fixture
def empty_board():
    """Creates an empty Tic-Tac-Toe board."""
    return [[" " for _ in range(3)] for _ in range(3)]

@pytest.fixture
def winning_board():
    """Creates a board where 'X' has already won."""
    return [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "]
    ]

def test_get_available_moves(empty_board):
    """Tests if available moves are correctly retrieved."""
    moves = get_available_moves(empty_board)
    assert len(moves) == 9  # Initially, all 9 spaces should be available

def test_player_move(monkeypatch, empty_board):
    """Tests if a player move updates the board correctly."""
    monkeypatch.setattr('builtins.input', lambda _: "1 1")  # Simulate user entering "1 1"
    player_move(empty_board, "X")
    assert empty_board[1][1] == "X"  # Player's move should be recorded

def test_computer_move(empty_board):
    """Tests if the computer makes a valid move."""
    initial_moves = len(get_available_moves(empty_board))
    computer_move(empty_board, "O")
    assert len(get_available_moves(empty_board)) == initial_moves - 1  # One move should be taken

def test_check_winner(winning_board):
    """Tests if the function correctly detects a winning condition."""
    assert check_winner(winning_board, "X") is True
    assert check_winner(winning_board, "O") is False

def test_is_board_full():
    """Tests if the board is correctly identified as full or not."""
    full_board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert is_board_full(full_board) is True

    not_full_board = [
        ["X", "O", " "],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert is_board_full(not_full_board) is False
