import random

def play_game():
    print("\n🎮 Welcome to the Advanced Number Guessing Game!")

    # Difficulty levels
    print("Choose difficulty level:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard (1–100, 10 attempts)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        number = random.randint(1, 10)
        attempts = 5
        max_range = 10
    elif choice == "2":
        number = random.randint(1, 50)
        attempts = 7
        max_range = 50
    elif choice == "3":
        number = random.randint(1, 100)
        attempts = 10
        max_range = 100
    else:
        print("Invalid choice. Defaulting to Easy level.")
        number = random.randint(1, 10)
        attempts = 5
        max_range = 10

    print(f"\nI have chosen a number between 1 and {max_range}. You have {attempts} attempts!")

    # Game loop
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess → "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if guess == number:
            print(f"🎉 Correct! You guessed the number in {attempt} attempts!")
            score = attempts - attempt + 1
            print(f"🏆 Your score: {score}")
            break
        elif guess < number:
            print("⬇ Too low!")
        else:
            print("⬆ Too high!")
    else:
        print(f"😢 Out of attempts! The number was {number}.")

# Main game loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break
