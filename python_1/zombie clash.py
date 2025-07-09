print ("hello player welcome to my world")
print("🎮 Welcome to the Game!")

# Ask for age
age = input("How old are you? ")

# Check if it's a number
if age.isdigit():
    age = int(age)
    
    if age < 13:
        print("❌ Sorry, you must be at least 13 to play.")
    else:
        print("✅ You're old enough! Let's continue...\n")

        # Ask for gender
        print("What is your gender?")
        print("1. Male")
        print("2. Female")

        gender = input("Enter 1 or 2: ")

        if gender == "1":
            pronoun = "he/him"
            print("👍 You will be referred to as he/him.")
        elif gender == "2":
            pronoun = "she/her"
            print("👍 You will be referred to as she/her.")
        else:
            pronoun = "they/them"
            print("⚠️ Invalid choice. You'll be referred to as they/them.")

        # Example use of pronoun later in game
        print("\nThe game begins now...")
        print(f"As the adventure starts, {pronoun.split('/')[0]} walks into a dark cave.")
else:
    print("⚠️ Please enter a valid number.")
