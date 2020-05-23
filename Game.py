import time
import random


# Add delay to the text-based adventure game.
def print_delay(text):
    print(text)
    time.sleep(1)


# Start game with introduction.
def intro():
    print_delay("You find yourself standing in an open field, filled with "
                + "grass and yellow wildflowers.")
    print_delay(f"Rumor has it that a {enemy} is somewhere around here, and "
                + "has been terrifying the nearby village.")
    print_delay("In front of you is a house")
    print_delay("To your right is a dark cave.")
    print_delay("In your hand you hold your trusty (but not very effective) "
                + "dagger.")


# Cave scene.
def cave():
    # Use global scope to fix local variable * referenced before assignment
    global weapon
    if weapon == "sword":
        print_delay("Your peer cautiously into the cave.")
        print_delay("You've been here before, and gotten all the good stuff. "
                    + "It's just an empty cave now.")
        print_delay("You walk back to the field.")
    else:
        print_delay("You peer cautiously into the cave.")
        print_delay("Your eye catches a glint of metal behind a rock.")
        print_delay("You have found the magical Sword of Ogoroth!")
        print_delay(f"You discard your silly old dagger and take the sword "
                    + "with you.")
        print_delay("You walk back out to the field.")
        # Add sword to the weapon variable.
        weapon = "sword"
    fieldDecision()


# House scene.
def house():
    print_delay("You approach the door of the house.")
    print_delay("You are about to knock when the door opens and out steps "
                + f"a {enemy}.")
    print_delay(f"Eep! This is the {enemy}'s house!")
    battle()


def battle():
    print_delay(f"The {enemy} attacks you!")

    # Check if ready to battle with sword.
    if weapon != "sword":
        print_delay(f"You feel a bit under-prepared for this, what with only "
                    + "having a tiny dagger.")

    # Offer choice
    choice = input("Would you like to (1) fight or (2) run away?")

    if choice == "1":  # fight
        if weapon == "sword":  # happy path
            print_delay(f"As the {enemy} moves to attack, you unsheath your "
                        + "new sword.")
            print_delay(f"The Sword of Ogoroth shines brightly in your hand "
                        + "as you brace yourself for the attack.")
            print_delay(f"But the {enemy} takes one look at your shiny new "
                        + "toy and runs away!")
            print_delay(f"You have rid the town of the {enemy}. You are "
                        + "victorious!")
        else:  # sad path
            print_delay(f"You do your best...")
            print_delay(f"but your dagger is no match for the {enemy}.")
            print_delay(f"You have been defeated!")
    elif choice == "2":  # run
        print_delay("You run back into the field. Luckily, you don't seem "
                    + "to have been followed.")
        fieldDecision()


# Logic to choose between house and cave.
def fieldDecision():
    print_delay("\nEnter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")
    print_delay("What would you like to do?")

    while True:
        isCaveOrHouse = input("(Please enter 1 or 2.)\n")
        if isCaveOrHouse == "1":
            house()
            break
        elif isCaveOrHouse == "2":
            cave()
            break


# Logic to quit the game.
def play_again():
    again = ""
    choicesArray = ["y", "n"]
    while again not in choicesArray:
        again = input("Would you like to play again? (y/n)\n")
        if again == "n":
            print_delay("\nThanks for playing! See you next time.")
            return "game_over"
        elif again == "y":
            print_delay("Excellent! Restarting the game ...")
            return "game_active"


# Logic to start the game with no weapons that can defeat an enemy.
state = 'game_active'
while state == 'game_active':
    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon = ""  # Initial with no weapons
    intro()
    fieldDecision()
    state = play_again()
