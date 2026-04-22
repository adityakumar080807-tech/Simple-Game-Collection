import random


# ================== GAME 1 ==================
def stone_paper_scissors():
    print("\n--- Stone Paper Scissors ---")
    choices = ["stone", "paper", "scissors"]

    while True:
        user = input("Enter stone/paper/scissors (or 'exit' to go back): ").lower()

        if user == "exit":
            break

        if user not in choices:
            print("Invalid choice!")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a draw!")
        elif (user == "stone" and computer == "scissors") or \
             (user == "paper" and computer == "stone") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("Computer wins!")


# ================== GAME 2 ==================
def dice_game():
    print("\n--- Dice Roll Game ---")

    while True:
        user_input = input("Press Enter to roll dice (or type 'exit' to go back): ")

        if user_input.lower() == "exit":
            break

        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print(f"You rolled: {user_roll}")
        print(f"Computer rolled: {computer_roll}")

        if user_roll > computer_roll:
            print("You win!")
        elif user_roll < computer_roll:
            print("Computer wins!")
        else:
            print("It's a draw!")


# ================== MAIN MENU ==================
def main():
    while True:   # Infinite loop (required)
        print("\n===== GAME MENU =====")
        print("1. Stone Paper Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            stone_paper_scissors()

        elif choice == '2':
            dice_game()

        elif choice == '3':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()