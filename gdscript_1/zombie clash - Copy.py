# Global variable to track if the little girl joins your team
has_girl = False

# Function to start the game and collect player info
def start_game():
    global has_girl  # Access the global variable to modify it here
    has_girl = False  # Reset the girl joining status at the start of the game

    print("Welcome to the Zombie Survival Game!")  # Display welcome message

    name = input("What's your name? ")  # Ask player for their name and store it
    print(f"Hello, {name}!")  # Greet the player by their name

    age = input("How old are you? ")  # Ask for player's age as text input

    if age.isdigit():  # Check if the input is all digits (valid number)
        age = int(age)  # Convert the age from string to integer
        if age < 14:  # Check if the player is younger than 14
            print("Sorry, you're too young to play.")  # Deny access for underage
            return  # End the function and game here
        else:
            print("You're old enough to play.")  # Confirm player is old enough

            print("What is your gender?")  # Ask for gender options
            print("1. Male")  # Option 1: Male
            print("2. Female")  # Option 2: Female
            gender = input("Enter 1 or 2: ")  # Get the gender choice input

            if gender == "1":  # If player chose Male
                pronoun = "he/him"  # Set pronoun to he/him
            elif gender == "2":  # If player chose Female
                pronoun = "she/her"  # Set pronoun to she/her
            else:
                pronoun = "they/them"  # Invalid input: set pronoun to they/them
                print("Invalid choice. You will be referred to as they/them.")  # Notify player

            print(f"Let's begin, {name}. You will be referred to as {pronoun}.")  # Show pronoun info
            first_challenge()  # Start the first challenge
    else:
        print("Please enter a valid number for your age.")  # Error message for invalid age input
        start_game()  # Restart game input process

# Function for the first challenge: zombie attacks
def first_challenge():
    print("\nA zombie approaches you... What do you do?")  # Describe the situation
    print("A) Punch it")  # Option A
    print("B) Kick it")  # Option B
    print("C) Run away")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Get choice, remove spaces, capitalize

    if choice == "A":  # If player chooses to punch
        print("You punch the zombie... it gets mad and kills you!")  # Consequence message
        print("You died. Game over.")  # Player death message
        start_game()  # Restart game
    elif choice == "B":  # If player chooses to kick
        print("You kick the zombie and break its legs. It can't move!")  # Success message
        print("You survived and move on.")  # Continue message
        second_challenge()  # Proceed to second challenge
    elif choice == "C":  # If player chooses to run away
        print("You run away, trip, and fall on a machete.")  # Failure message
        print("You died. Game over.")  # Death message
        start_game()  # Restart game
    else:
        print("Invalid choice.")  # Invalid input message
        first_challenge()  # Ask again for input

# Function for the second challenge: tied-up girl
def second_challenge():
    print("\nYou see a tied-up little girl in the road.")  # Scenario description
    print("A) Beat her up")  # Option A
    print("B) Help her")  # Option B
    print("C) Do nothing and leave")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Get and sanitize input

    if choice == "A":  # Player beats girl
        print("The girl turns into a giant ogre and kills you!")  # Consequence
        print("You died. Game over.")  # Death message
        start_game()  # Restart game
    elif choice == "B":  # Player helps girl
        print("You help the girl. She says thank you... and eats you.")  # Negative outcome
        print("You died. Game over.")  # Death message
        start_game()  # Restart game
    elif choice == "C":  # Player leaves girl
        print("You walk away. She gets attacked by zombies.")  # Narrative detail
        print("You survive and continue.")  # Continue message
        third_challenge()  # Proceed to third challenge
    else:
        print("Invalid choice.")  # Invalid input
        second_challenge()  # Repeat input prompt

# Function for the third challenge: zombie chase
def third_challenge():
    print("\nYou're being chased by 100 zombies.")  # Scenario setup
    print("A) Keep running")  # Option A
    print("B) Hide")  # Option B
    print("C) Fight back")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Get choice input

    if choice == "A":  # Keep running
        print("You run out of energy. A fast zombie kills you.")  # Consequence
        print("You died. Game over.")  # Death message
        start_game()  # Restart game
    elif choice == "B":  # Hide
        print("You hide successfully. You survive.")  # Success
        fourth_challenge()  # Proceed
    elif choice == "C":  # Fight
        print("You fight back but get stomped by a giant zombie.")  # Death scenario
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    else:
        print("Invalid choice.")  # Input error
        third_challenge()  # Repeat input

# Function for the fourth challenge: abandoned building
def fourth_challenge():
    print("\nYou find an abandoned building.")  # Description
    print("A) Go in")  # Option A
    print("B) Keep walking")  # Option B
    print("C) Start dancing")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Input

    if choice == "A":  # Enter building
        print("You go in and it's safe. You rest and survive.")  # Success
        fifth_challenge()  # Continue
    elif choice == "B":  # Keep walking
        print("Zombies catch you off guard and eat you.")  # Death scenario
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    elif choice == "C":  # Dance
        print("You start dancing. The girl from earlier falls off the roof onto you.")  # Death scenario
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    else:
        print("Invalid choice.")  # Invalid input
        fourth_challenge()  # Retry input

# Function for the fifth challenge: zombies inside building
def fifth_challenge():
    print("\nYou see a bunch of zombies inside with you.")  # Scene setup
    print("A) Run to the roof")  # Option A
    print("B) Stay and fight")  # Option B
    print("C) Run out the building")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Input

    if choice == "A":  # Run to roof
        print("You run to the roof and survive.")  # Success
        sixth_challenge()  # Continue
    elif choice == "B":  # Stay and fight
        print("You fight like a champ but bleed out.")  # Death outcome
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    elif choice == "C":  # Run outside
        print("The girl falls off the roof onto you again. You feel guilty and die.")  # Death scenario
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    else:
        print("Invalid choice.")  # Invalid input
        fifth_challenge()  # Retry

# Function for the sixth challenge: zombie girl encounter
def sixth_challenge():
    print("\nYou see the little girl again... but she's a zombie.")  # Description
    print("A) Beat her up and throw her off the building")  # Option A
    print("B) Look for a cure")  # Option B
    print("C) Go back inside")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Input

    if choice == "A":  # Beat and throw off building
        print("You throw her off the building but she takes you with her.")  # Death scenario
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    elif choice == "B":  # Find cure
        print("You find a cure and save her. You both survive.")  # Success
        seventh_challenge()  # Continue
    elif choice == "C":  # Go back inside
        print("You trip down the stairs. Zombie monkeys beat you up.")  # Death outcome
        print("You died. Game over.")  # Death message
        start_game()  # Restart
    else:
        print("Invalid choice.")  # Invalid input
        sixth_challenge()  # Retry

# Function for the seventh challenge: girl asks to join your team
def seventh_challenge():
    global has_girl  # Access global variable
    print("\nThe girl asks to join your team.")  # Scenario
    print("A) Yes")  # Option A
    print("B) No")  # Option B
    print("C) Kill her")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Input

    if choice == "A":  # Accept girl
        has_girl = True  # Set flag true
        print("She joins your team. You survive together.")  # Success message
        eighth_challenge()  # Proceed to last challenge
    elif choice == "B":  # Reject girl
        has_girl = False  # Set flag false
        print("She walks away and dies. You survive alone.")  # Narrative message
        eighth_challenge()  # Continue without girl
    elif choice == "C":  # Try to kill her
        print("You try to kill her but stab yourself.")  # Death scenario
        print("You died. Game over.")  # Death message
        start_game()  # Restart game
    else:
        print("Invalid choice.")  # Input error
        seventh_challenge()  # Retry input

# Function for the eighth and final challenge: zombie horde encounter
def eighth_challenge():
    global has_girl  # Access global variable to check if girl joined
    print("\nYou see a horde of zombies ahead.")  # Scenario description
    print("A) Fight them")  # Option A
    print("B) Run away")  # Option B
    print("C) Pretend to be a zombie")  # Option C
    choice = input("Choose A, B, or C: ").strip().upper()  # Input

    if has_girl:  # If girl joined team
        if choice == "A":  # Fight with girl
            print("You and the girl fight and win. You both survive.")  # Win message
        elif choice == "B":  # Run away
            print("You both run but trip and get eaten.")  # Death scenario
            print("You died. Game over.")  # Death message
            start_game()  # Restart game
        elif choice == "C":  # Pretend zombie
            print("Zombies notice you're fake and eat you.")  # Death scenario
            print("You died. Game over.")  # Death message
            start_game()  # Restart game
        else:
            print("Invalid choice.")  # Input error
            eighth_challenge()  # Retry
    else:  # If girl did not join team
        if choice == "A":  # Fight alone
            print("You fight alone but get cut up.")  # Death outcome
            print("You died. Game over.")  # Death message
            start_game()  # Restart
        elif choice == "B":  # Run alone
            print("You run, trip, and your brain falls out.")  # Death scenario
            print("You died. Game over.")  # Death message
            start_game()  # Restart
        elif choice == "C":  # Pretend zombie
            print("They see through your disguise and kill you.")  # Death scenario
            print("You died. Game over.")  # Death message
            start_game()  # Restart
        else:
            print("Invalid choice.")  # Input error
            eighth_challenge()  # Retry

# Start the game by calling the start_game function
start_game()
