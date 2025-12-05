name = input("Enter your name: ")
print(f"Welcome, {name}, to Solker's adventureous game!")

answer = input(
    "You're at a crossroad in a forest nested in Uganda, do you want to go left or right? ").lower()

if answer == "left":
    answer = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if answer == "wait":
        answer = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if answer == "yellow":
            print("You found the treasure! You Win!")
        elif answer == "red":
            print("It's a room full of fire. Game Over.")
        elif answer == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
