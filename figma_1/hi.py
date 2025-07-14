import random

print("Hello person, type 'random' to get a random number.")

while True:
    user_input = input("Type 'random' to get a random number (or anything else to quit): ").lower()
    if user_input == "random":
        number = random.randint(1, 100)
        print("Your random number is:", number)
    else:
        print("You didn't type 'random'. Goodbye!")
        break
