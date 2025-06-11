def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    return None

def is_board_full(board):
    return " " not in board

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Enter a number (1-9) to make your move:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("\nLet's begin!\n")
    
    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"\nPlayer {winner} wins!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("\nIt's a tie!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for playing! Goodbye.")
            break
        elif play_again == "yes":
            print("\nStarting a new game...\n")
            tic_tac_toe()
        else:
            print("Please enter 'yes' or 'no'.")