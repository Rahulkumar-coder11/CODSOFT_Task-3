#1.ROCK,PAPER,SCISSORS GAME
import random

# Options
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0


def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"


def play_game():
    global user_score, computer_score

    print("\nWelcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")

    while True:
        # User input
        user_choice = input("Your choice: ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer input
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        winner = get_winner(user_choice, computer_choice)

        # Display result
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Show scores
        print(f"Score => You: {user_score} | Computer: {computer_score}")

        # Play again?
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


# Start the game
play_game()