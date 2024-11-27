import random

# Constants
BOARD_SIZE = 100
SNAKES = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll):
    position += roll
    if position > BOARD_SIZE:
        position -= roll  # If the move exceeds 100, don't move
    return position

def check_snake_or_ladder(position):
    if position in SNAKES:
        print(f"Oops! You landed on a snake at {position}. Go down to {SNAKES[position]}.")
        return SNAKES[position]
    elif position in LADDERS:

        print(f"Yay! You climbed a ladder from {position} to {LADDERS[position]}.")
        return LADDERS[position]
    return position

def play_game():
    player1_position = 0
    player2_position = 0
    turn = 0  # 0 for player 1, 1 for player 2

    while player1_position < BOARD_SIZE and player2_position < BOARD_SIZE:
        if turn == 0:
            input("Player 1's turn. Press Enter to roll the dice.")
            roll = roll_dice()
            print(f"Player 1 rolled a {roll}.")
            player1_position = move_player(player1_position, roll)
            player1_position = check_snake_or_ladder(player1_position)
            print(f"Player 1 is now on square {player1_position}.\n")
            turn = 1
        else:
            input("Player 2's turn. Press Enter to roll the dice.")
            roll = roll_dice()
            print(f"Player 2 rolled a {roll}.")
            player2_position = move_player(player2_position, roll)
            player2_position = check_snake_or_ladder(player2_position)
            print(f"Player 2 is now on square {player2_position}.\n")
            turn = 0

    if player1_position >= BOARD_SIZE:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

if __name__ == "__main__":
    play_game()