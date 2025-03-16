import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
computer_choose = random.randint(1, 100)

# Define attempt limits
attempt_hard = 5
attempt_easy = 10

# Get user difficulty level
choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Set attempts based on difficulty level
attempts = attempt_easy if choose_level == 'easy' else attempt_hard

# Game loop
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    # Get user input
    user_input = int(input("Guess the number: "))

    if user_input == computer_choose:
        print(f"Congratulations! You guessed the number {computer_choose} correctly! 🎉")
        break
    elif user_input < computer_choose:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    # Reduce attempts
    attempts -= 1

    if attempts == 0:
        print(f"Sorry, you're out of attempts! The number was {computer_choose}. Better luck next time! 😢")
