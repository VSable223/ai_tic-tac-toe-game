import math
import os

# Clear the terminal screen for a cleaner UI
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the game board in a clean format
def print_board(board):
    clear_screen()
    print("\n🎮  Tic-Tac-Toe")
    print("You (X) vs AI (O)\n")
    print("   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  " + "---+---+---")
    print()

# Check all possible winning combinations
def check_winner(board):
    lines = board + [list(col) for col in zip(*board)]  # rows + columns
    lines.append([board[i][i] for i in range(3)])        # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])    # anti-diagonal

    for line in lines:
        if line == ['X'] * 3:
            return 'X'
        elif line == ['O'] * 3:
            return 'O'

    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'

    return None
