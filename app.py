import random

print("hello world")
# Define the options and their relationships
options = {
    "rock": {"beats": "scissors", "loses_to": "paper"},
    "paper": {"beats": "rock", "loses_to": "scissors"},
    "scissors": {"beats": "paper", "loses_to": "rock"}
}

# Initialize the player's score
player_score = 0

# Game loop
while True:
    # Get player's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check if the player's choice is valid
    if player_choice not in options:
        print("Invalid option. Please choose rock, paper, or scissors.")
        continue

    # Generate opponent's choice randomly
    opponent_choice = random.choice(list(options.keys()))
    print("Opponent's choice:", opponent_choice)
    # Determine the result of the round
    if player_choice == opponent_choice:
        print("It's a tie!")
    elif player_choice == options[opponent_choice]["loses_to"]:
        print("You win!")
        player_score += 1
    else:
        print("You lose!")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "y" and play_again != "yes":
        break

# Display the player's score
print("Your score:", player_score)