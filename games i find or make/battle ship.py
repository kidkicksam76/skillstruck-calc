import random

# Create a 5x5 game board
def create_board():
    return [["~" for _ in range(5)] for _ in range(5)]

# Print the board
def print_board(board):
    print("  0 1 2 3 4")
    for idx, row in enumerate(board):
        print(f"{idx} {' '.join(row)}")

# Place the ships randomly on the board (hidden from player)
def place_ships(board, num_ships=3):
    ships = []
    while len(ships) < num_ships:
        x, y = random.randint(0, 4), random.randint(0, 4)
        if (x, y) not in ships:  # Ensure no two ships are at the same position
            ships.append((x, y))
    return ships

# Check if the player's guess hit a ship
def check_guess(guess, ships):
    return guess in ships

# Main Battleship game function
def play_battleship():
    print("Welcome to Battleship!")
    print("You have to sink 3 ships hidden on a 5x5 grid.")
    
    # Create the player's visible board and the computer's hidden ships
    player_board = create_board()
    enemy_ships = place_ships(player_board, num_ships=3)
    guesses = 0
    max_guesses = 10
    ships_sunk = 0
    
    while guesses < max_guesses and ships_sunk < 3:
        print_board(player_board)
        print(f"\nGuesses remaining: {max_guesses - guesses}")
        
        # Get player's guess (row and column)
        try:
            row = int(input("Enter the row (0-4): "))
            col = int(input("Enter the column (0-4): "))
        except ValueError:
            print("Please enter valid integers for row and column!")
            continue
        
        if row < 0 or row > 4 or col < 0 or col > 4:
            print("Please enter values between 0 and 4.")
            continue
        
        guess = (row, col)
        if check_guess(guess, enemy_ships):
            print("Hit! You sunk a ship!")
            player_board[row][col] = "X"
            ships_sunk += 1
            enemy_ships.remove(guess)
        else:
            print("Miss!")
            player_board[row][col] = "O"
        
        guesses += 1
    
    # End of the game
    if ships_sunk == 3:
        print("Congratulations! You sank all the ships!")
    else:
        print("Out of guesses! You lost.")
    
    print("\nFinal board:")
    print_board(player_board)

# Start the game
play_battleship()
