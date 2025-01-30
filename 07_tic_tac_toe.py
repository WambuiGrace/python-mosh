''''
    Create and display board
    loop
        ask user for input
        check if input is valid
        update board
        check winner == true print message and break
        check if board == full print message and break
        switch players
'''
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def color_cell(cell):
    if cell == 'x':
        return Fore.GREEN + cell + Style.RESET_ALL
    elif cell == 'o':
        return Fore.RED + cell + Style.RESET_ALL
    else:
        return cell

# Display board with colored cells
def display_board(board):
    lines = '---+---+---'
    print(lines)
    for row in board:
        # Apply color to each cell in the row
        colored_row = [color_cell(cell) for cell in row]
        print(f' {colored_row[0]} | {colored_row[1]} | {colored_row[2]} ')
        print(lines)

# Check for the winner
def check_winner(board, current_player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    
    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

# Check if board is full
def check_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    display_board(board)

    current_player = 'x'

    while True:
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0-2): "))
        column = int(input("Enter column (0-2): "))

        if board[row][column] == ' ':
            board[row][column] = current_player
            display_board(board)
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_full(board):
            print('The board is full. It is a tie!')
            break

        # Switch players
        current_player = 'o' if current_player == 'x' else 'x'

if __name__ == "__main__":
    main()