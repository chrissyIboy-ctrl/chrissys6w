has_girl = False  # Tracks whether the girl joins your team

def first_challenge():
    print("🧟 A zombie approaches you... What do you do?")
    print("A) Punch it")
    print("B) Kick it")
    print("C) Run away")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("🧟 You punch the zombie... it gets mad and kills you!")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "B":
        print("🥾 You kick the zombie and break its legs. It can't move!")
        print("✅ You survived and move on with the game!")
        second_challenge()
    elif choice == "C":
        print("🏃 You run away, trip, and fall on a machete...")
        print("💀 You died. Game over.\n")
        start_game()
    else:
        print("⚠️ Invalid choice. Please try again.")
        first_challenge()

def second_challenge():
    print("\n👧 You see a tied-up little girl in the middle of the road.")
    print("What do you do?")
    print("A) Beat her up")
    print("B) Help her")
    print("C) Do nothing and leave")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n😱 The girl turns into a giant ogre and kills you!")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "B":
        print("\n😨 You help the little girl. She says 'Thank you!'")
        print("🧟 But then she eats you and turns you into a zombie!")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "C":
        print("\n😐 You walk away, leaving the little girl.")
        print("👹 She gets jumped by zombies and dies.")
        print("✅ You survive and continue the game!\n")
        third_challenge()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        second_challenge()

def third_challenge():
    print("\n🏃 You're getting chased by 100 zombies, some are fast and some are giants.")
    print("What do you do?")
    print("A) Keep running")
    print("B) Hide")
    print("C) Fight back")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n😰 You try to keep running but run out of energy.")
        print("⚡ A fast zombie tackles you and rips your face off.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "B":
        print("\n😌 You successfully hide in an alleyway.")
        print("✅ You passed the challenge and survive!\n")
        fourth_challenge()
    elif choice == "C":
        print("\n🗡️ You fight back and kill 5 zombies,")
        print("👹 but then you get stomped by a giant zombie.")
        print("💀 You died. Game over.\n")
        start_game()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        third_challenge()

def fourth_challenge():
    print("\n🏚️ You find an abandoned building. What do you do?")
    print("A) Go in")
    print("B) Keep walking")
    print("C) Start dancing")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n🏠 You go in and look around cautiously.")
        print("✅ It's safe! You rest and survive!\n")
        fifth_challenge()
    elif choice == "B":
        print("\n😱 A group of zombies catch you off guard!")
        print("🧟 They rip your limbs off and eat you alive.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "C":
        print("\n🕺 You start dancing in the open like it's a party...")
        print("👧 The little girl from earlier falls off the roof onto you.")
        print("💀 You died. Game over.\n")
        start_game()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        fourth_challenge()

def fifth_challenge():
    print("\n🧟 You see a bunch of zombies in the room with you!")
    print("What do you do?")
    print("A) Run to the roof")
    print("B) Stay back and fight")
    print("C) Run out the building")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n🏃 You quickly run to the roof and outrun them.")
        print("✅ You survive again!\n")
        sixth_challenge()
    elif choice == "B":
        print("\n🩸 You fight them all off like a champ...")
        print("😵 But notice a cut on your side. You bleed out and die.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "C":
        print("\n🚪 You run out the building into the street...")
        print("👧 The girl from earlier falls off the building onto you.")
        print("💔 You feel so guilty that you cut your own neck.")
        print("💀 You died. Game over.\n")
        start_game()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        fifth_challenge()

def sixth_challenge():
    print("\n🧟 You see the little girl from earlier… but now she's a zombie!")
    print("What do you do?")
    print("A) Beat her up and throw her off the building")
    print("B) Look for a cure")
    print("C) Go back inside")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n😨 You throw her off the building...")
        print("👧 But she grabs you on the way down and takes you with her.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "B":
        print("\n🔬 You search frantically... and find a cure!")
        print("💉 You cure the little girl and save her life!")
        print("✅ You survive and continue your journey!\n")
        seventh_challenge()
    elif choice == "C":
        print("\n🚪 You go back inside...")
        print("😵 You trip down the stairs and can't move.")
        print("🐒 Zombie monkeys show up and beat you up.")
        print("💀 You died. Game over.\n")
        start_game()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        sixth_challenge()

def seventh_challenge():
    global has_girl
    print("\n👧 The little girl thanks you and asks to join your team.")
    print("What do you do?")
    print("A) Yes")
    print("B) No")
    print("C) Kill her")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        has_girl = True
        print("\n🤝 You agree and let her join.")
        print("✅ She joins your team. You both survive together!\n")
        eighth_challenge()
    elif choice == "B":
        has_girl = False
        print("\n😢 You say no. She sadly walks away...")
        print("😬 Then trips, hits her head, and dies.")
        print("✅ You survive, but it's kinda awkward.\n")
        eighth_challenge()
    elif choice == "C":
        print("\n🔪 You try to kill her...")
        print("😵 But you miss and accidentally stab yourself in the heart.")
        print("💀 You died. Game over.\n")
        start_game()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        seventh_challenge()

def eighth_challenge():
    global has_girl
    print("\n🧟 You see a bunch of zombies ahead...")
    print("What do you do?")
    print("A) Fight them")
    print("B) Run away")
    print("C) Pretend to be a zombie")

    choice = input("Choose A, B, or C: ").strip().upper()

    if has_girl:
        if choice == "A":
            print("\n⚔️ You and the girl fight fiercely...")
            print("🩸 You beat all the zombies and steal their swords!")
            print("✅ You survive together. Nice job!\n")
            print("🏁 END OF CHAPTER 1 COMPLETE!")
        elif choice == "B":
            print("\n🏃 You both try to run...")
            print("😵 But trip, fall, and get eaten alive.")
            print("💀 You died. Game over.\n")
            start_game()
        elif choice == "C":
            print("\n🧟 You pretend to be zombies...")
            print("😐 But the horde notices you're not one of them and eats you both.")
            print("💀 You died. Game over.\n")
            start_game()
        else:
            print("\n⚠️ Invalid choice. Please try again.")
            eighth_challenge()
    else:
        if choice == "A":
            print("\n🗡️ You try to fight them alone...")
            print("👹 They jump on you and cut you up with swords.")
            print("💀 You died. Game over.\n")
            start_game()
        elif choice == "B":
            print("\n🏃 You run but trip...")
            print("🧠 Crack your head open and your brain falls out.")
            print("💀 You died. Game over.\n")
            start_game()
        elif choice == "C":
            print("\n🧟 You pretend to be a zombie...")
            print("😈 They see through your disguise and painfully kill you.")
            print("💀 You died. Game over.\n")
            start_game()
        else:
            print("\n⚠️ Invalid choice. Please try again.")
            eighth_challenge()

def ninth_challenge():
    print("\n📢 The Master Zombie plays an alert across the city...")
    print("🧟‍♂️ He warns everyone that he will rule the world with his zombie army!")

    print("\nWhat do you do?")
    print("A) Start hiding")
    print("B) Make an army of nice zombies")
    print("C) Sneak up on him")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n🏚️ You go into hiding...")
        print("⏳ 30 years later... they finally find you and the little girl.")
        print("🧟 They eat you both like leftovers.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "B":
        print("\n🧠 You try to build an army of nice zombies...")
        print("👑 But the Master Zombie gets mad and launches a brutal attack.")
        print("💀 Your zombies turn on you and eat you alive. Game over.\n")
        start_game()
    elif choice == "C":
        print("\n🕶️ You sneak up behind the Master Zombie...")
        print("🔪 You hide in the shadows, getting ready to attack...\n")
        tenth_challenge()
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        ninth_challenge()

def tenth_challenge():
    print("\n🧟 You're right behind the Master Zombie King.")
    print("What do you do?")
    print("A) 1000th years of death")
    print("B) Make a truce")
    print("C) Start break dancing")

    choice = input("Choose A, B, or C: ").strip().upper()

    if choice == "A":
        print("\n💥 You yell '1000th years of death!' and strike...")
        print("💣 But he explodes in rage, killing everyone on Earth.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "B":
        print("\n🤝 You try to make a truce with him...")
        print("👣 He laughs and stomps you into the ground.")
        print("💀 You died. Game over.\n")
        start_game()
    elif choice == "C":
        print("\n🕺 You start break dancing like your life depends on it...")
        print("😳 The Master Zombie watches in horror.")
        print("😵 He kills himself because you're so bad at dancing!")
        print("🧟 All the other zombies brutally end themselves too.")
        print("👧 You and the little girl are the last humans left... until more people come out of hiding.")
        print("🎉 YOU WIN! THE END. 🌎")
    else:
        print("\n⚠️ Invalid choice. Please try again.")
        tenth_challenge()

def start_game():
    global has_girl
    has_girl = False  # Reset each time game restarts

    print("🎮 Welcome to the Game!")

    # Get player's name
    name = input("What's your name? ")
    print(f"Hello, {name}!")

    # Get age
    age = input(f"How old are you, {name}? ")

    if age.isdigit():
        age = int(age)
        if age < 13:
            print(f"❌ Sorry {name}, you must be at least 13 to play.")
            return
        else:
            print(f"✅ You're old enough, {name}! Let's continue...\n")

            # Get gender
            print("What is your gender?")
            print("1. Male")
            print("2. Female")

            gender = input("Enter 1 or 2: ")
            if gender == "1":
                pronoun = "he/him"
            elif gender == "2":
                pronoun = "she/her"
            else:
                pronoun = "they/them"
                print("⚠️ Invalid choice. You'll be referred to as they/them.")

            print(f"\nAlright {name}, you'll be referred to as {pronoun}. Let's begin the game!\n")
            first_challenge()
    else:
        print(f"⚠️ {name}, please enter a valid number for your age.")
        start_game()

# Start the game
start_game()
