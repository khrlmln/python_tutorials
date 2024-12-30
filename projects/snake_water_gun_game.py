# creating snake water gun game
import random

# Choices for the computer
computer_input = random.choice([1, -1, 0])

# User input
user_input = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Mapping user input to values
choices = {"s": 1, "w": -1, "g": 0}
choices_name = {1: "snake", -1: "water", 0: "gun"}

# Ensure user input is valid
if user_input not in choices:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    user_input_value = choices[user_input]

    print(f"You chose {choices_name[user_input_value]}")
    print(f"Computer chose {choices_name[computer_input]}")

    # Determine the winner
    if computer_input == user_input_value:
        print("It's a draw!")
    elif (
        (computer_input == 1 and user_input_value == -1)
        or (computer_input == 0 and user_input_value == 1)
        or (computer_input == -1 and user_input_value == 0)
    ):
        print("Computer wins!")
    else:
        print("You win!")
