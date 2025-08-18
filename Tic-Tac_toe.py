import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear terminal screen for better UX"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Prints a neat game banner"""
    print(Fore.CYAN + Style.BRIGHT + "\n========= TIC TAC TOE =========\n" + Style.RESET_ALL)

def print_board(board):
    """Prints the Tic Tac Toe board with colors"""
    clear_screen()
    print_banner()

    print("   " + "   ".join([Fore.YELLOW + str(i) + Style.RESET_ALL for i in range(3)]))
    print("  " + "-" * 11)

    for idx, row in enumerate(board):
        colored_row = []
        for cell in row:
            if cell == "X":
                colored_row.append(Fore.RED + "X" + Style.RESET_ALL)
            elif cell == "O":
                colored_row.append(Fore.GREEN + "O" + Style.RESET_ALL)
            else:
                colored_row.append(" ")
        print(Fore.YELLOW + str(idx) + Style.RESET_ALL + " | " + " | ".join(colored_row) + " |")
        print("  " + "-" * 11)


def check_winner(board, player):
    """Check if the given player wins"""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full (draw)"""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(Fore.MAGENTA + f"Player {current_player}'s turn." + Style.RESET_ALL)

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print(Fore.RED + "Invalid input! Enter numbers 0, 1, or 2." + Style.RESET_ALL)
            time.sleep(1)
            continue

        if row not in range(3) or col not in range(3):
            print(Fore.RED + "Invalid position! Try again." + Style.RESET_ALL)
            time.sleep(1)
            continue
        if board[row][col] != " ":
            print(Fore.YELLOW + "That spot is already taken! Try again." + Style.RESET_ALL)
            time.sleep(1)
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(Fore.GREEN + Style.BRIGHT + f"Player {current_player} wins!" + Style.RESET_ALL)
            break

        if is_full(board):
            print_board(board)
            print(Fore.CYAN + Style.BRIGHT + "It's a draw! Well played both!" + Style.RESET_ALL)
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    # Replay option
    again = input(Fore.YELLOW + "\nDo you want to play again? (y/n): " + Style.RESET_ALL).strip().lower()
    if again == "y":
        tic_tac_toe()
    else:
        print(Fore.CYAN + "Thanks for playing! Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    tic_tac_toe()
