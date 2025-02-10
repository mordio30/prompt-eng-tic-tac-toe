import random

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    """Returns a list of available moves."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def player_move(board, player):
    """Handles the human player's move."""
    while True:
        try:
            row, col = map(int, input("Enter your move as 'row col' (0-2): ").split())
            if (row, col) in get_available_moves(board):
                board[row][col] = player
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Enter two numbers separated by space!")

def computer_move(board, computer):
    """Generates a random move for the computer."""
    row, col = random.choice(get_available_moves(board))
    board[row][col] = computer
    print(f"Computer placed '{computer}' at ({row}, {col})")

def is_board_full(board):
    """Checks if the board is full (tie condition)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Ask the user to choose X or O
    player = input("Do you want to be X or O? ").upper()
    while player not in ["X", "O"]:
        player = input("Invalid choice! Pick X or O: ").upper()
    
    computer = "O" if player == "X" else "X"
    print(f"You are '{player}', Computer is '{computer}'")
    
    # Decide who goes first (Player always starts)
    turn = "Player"
    
    while True:
        print_board(board)
        
        if turn == "Player":
            player_move(board, player)
            if check_winner(board, player):
                print_board(board)
                print("Congratulations! You win!")
                break
            turn = "Computer"
        else:
            computer_move(board, computer)
            if check_winner(board, computer):
                print_board(board)
                print("Computer wins! Better luck next time.")
                break
            turn = "Player"
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Run the game
#tic_tac_toe()
