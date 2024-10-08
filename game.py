import random 

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()  
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check if the user input is valid
if youstr in youDict:
    you = youDict[youstr]

    # Now we have two numbers: 'you' and 'computer'
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a Draw")
    else:
        if computer == -1 and you == 1:
            print("You win!")
        elif computer == -1 and you == 0:
            print("You lose!")
        elif computer == 1 and you == -1:
            print("You lose!")
        elif computer == 1 and you == 0:
            print("You win!")
        elif computer == 0 and you == -1:
            print("You win!")
        elif computer == 0 and you == 1:
            print("You lose!")
        else:
            print("Something went wrong!")
else:
    print("Invalid input! Please enter 's', 'w', or 'g'.")

