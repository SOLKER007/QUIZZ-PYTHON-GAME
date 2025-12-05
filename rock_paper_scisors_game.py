import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input(
        "Type rock, paper, scissors or quit to end the game: ").lower()
    if user_input == "quit":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input, please try again.")
        continue

    random_number = random.randint(0, 2)
    # 0 - rock, 1 - paper, 2 - scissors
    if random_number == 0:
        computer_choice = "rock"
    elif random_number == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")

    elif (user_input == "rock" and computer_choice == "scissors"):
        print("You win!")
        user_wins += 1
    elif (user_input == "paper" and computer_choice == "rock"):
        print("You win!")
        user_wins += 1
    elif (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1
print("You won " + str(user_wins) + " times.")
print("Computer won " + str(computer_wins) + " times.")
if user_wins > computer_wins:
    print("Overall, you are the champion!")
elif computer_wins > user_wins:
    print("Overall, the computer is the champion!")
else:
    print("Overall, it's a tie!")
