def print_board(board):
    print("\n")
    print(f"                                                    {board[0]} | {board[1]} | {board[2]} ")
    print("                                                   ---|---|---")
    print(f"                                                    {board[3]} | {board[4]} | {board[5]} ")
    print("                                                   ---|---|---")
    print(f"                                                    {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
                      [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
                      [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return True
    return False

def check_draw(board):
    return all(space in ["X", "O"] for space in board)

def tic_tac_toe():
    # Initialize the board with numbers 1-9
    board = [str(i) for i in range(1, 10)]
    
    # Take player names as input
    name1 = input("Enter name for Player 1 (X): ")
    name2 = input("Enter name for Player 2 (O): ")
    player1_name=name1.upper()
    player2_name=name2.upper()
    # Map symbols to names to keep track of turns easily
    player_names = {"X": player1_name, "O": player2_name}
    
    current_player = "X"
    game_over = False

    print("\n                                             WELCOME TO TIC TAC TOE !!")

    while not game_over:
        print_board(board)

        # Get and validate input using the current player's actual name
        try:
            choice = int(input(f"{player_names[current_player]}, Choose a position (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
            if board[choice] in ["X", "O"]:
                print("That spot is already taken! Try another one.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Place the move (still uses 'X' or 'O' on the board)
        board[choice] = current_player

        # Check game status
        if check_win(board):
            print_board(board)
            print(f"                                    CONGRATULATIONS !!!! {player_names[current_player]} WINS THE GAME !!!!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
