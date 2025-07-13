print("Welcome to the Number Guessing Game! \nI'm thinking of number between 1 and 100")
print("You have 5 chances to guess the correct number.\n")

import random
random_number = random.randint(1, 100)

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)\n")

# I forgot include the int for integer
choice = int(input("Enter your choice: "))

if choice == 1:
    print("\nGreat! You have selected the Easy difficulty level\nLet's start the game!")
    # Reminder: userchoice1 is our varible for choice 1 only
    userchoice1 = int(input("\nEnter your guess: "))

    x = 0

    while userchoice1 != random_number:
        x += 1
        # --------------------------------------------------------------------------------------

        if random_number < userchoice1:
            print("Incorrect! The number is less than", userchoice1)
            userchoice1 = int(input("\nEnter your guess: "))

        elif random_number > userchoice1:
            print("Incorrect! The number is greater than", userchoice1)
            userchoice1 = int(input("\nEnter your guess: "))

        # ---------------------------------------------------------------------------------------
        if x >= 9:
            print("Max attemps :(")
            break

    else:
        print("Congratulations! You guessed the correct number in", x, "attempts.")



if 2 == choice:
    print("\nGreat! You have selected the Medium difficulty level\nLet's start the game!")
    #Reminder: userchoice2 is our varible for choice 2 only
    userchoice2 = int(input("\nEnter your guess: "))

    #If the user’s guess is incorrect, the game should display
    #a message indicating whether the number is greater or less than the user’s guess.

    x = 0

    while userchoice2 != random_number:
        x += 1
        #--------------------------------------------------------------------------------------

        if random_number < userchoice2:
            print("Incorrect! The number is less than", userchoice2)
            userchoice2 = int(input("\nEnter your guess: "))

        elif random_number > userchoice2:
            print("Incorrect! The number is greater than", userchoice2)
            userchoice2 = int(input("\nEnter your guess: "))


        #---------------------------------------------------------------------------------------
        if x >= 4:
            print("Max attemps :(")
            break

    else:
        print("Congratulations! You guessed the correct number in", x, "attempts.")


    # for x in range(4):
    #     if userchoice2 == random_number:
    #         print("Congratulations! You guessed the correct number in", x, "attempts.")
    #     else:
    #         userchoice2 = int(input("Incorrect!\n\nEnter your guess: "))



if 3 == choice:
    print("\nGreat! You have selected the Hard difficulty level\nLet's start the game!")
    # Reminder: userchoice3 is our varible for choice 3 only
    userchoice3 = int(input("\nEnter your guess: "))

    x = 0

    while userchoice3 != random_number:
        x += 1
        # --------------------------------------------------------------------------------------

        if random_number < userchoice3:
            print("Incorrect! The number is less than", userchoice3)
            userchoice3 = int(input("\nEnter your guess: "))

        elif random_number > userchoice3:
            print("Incorrect! The number is greater than", userchoice3)
            userchoice3 = int(input("\nEnter your guess: "))




        # --------------------------------------------------------------------------------------
        # This how we stop for going on ∞ (infinity)
        if x >= 2:
            print("\nMax attemps :(")

    else: #userchoice3 == random_number
        print("Congratulations! You guessed the correct number in", x, "attempts.")



    # Extra credit:
    # Allow the user to play multiple rounds of the game (i.e., keep playing until the user decides to quit). You can do this by asking the user if they want to play again after each round.
    # Add a timer to see how long it takes the user to guess the number.
    # Implement a hint system that provides clues to the user if they are stuck.
    # Keep track of the user’s high score (i.e., the fewest number of attempts it took to guess the number under a specific difficulty level).
    #