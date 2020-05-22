import time
import random


def print_delay(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


def intro():
    print_delay("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_delay(f"Rumor has it that a {enemy} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_delay("In front of you is a house.")
    print_delay("To your right is a dark cave.")
    print_delay("In your hand you hold your trusty (but not very "
                "effective) dagger.")


# Allow player to pickup a sword before entering the game_map()
def cave():
    if "sword" in item:
        print_delay("You peer cautiously into the cave.")
        print_delay("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_delay("You walk back to the field.")
    else:
        print_delay("You peer cautiously into the cave.")
        print_delay("It turns out to be only a very small cave.")
        print_delay("Your eye catches a glint of metal behind a "
                    "rock.")
        print_delay("You have found the magical Sword of Ogoroth!")
        print_delay("You discard your silly old dagger and take "
                    "the sword with you.")
        print_delay("You walk back out to the field.")
        item.append("sword")
    game_map()


# Allow player to fight a battle with an enemy.
def house():
    print_delay("You approach the door of the house.")
    print_delay("You are about to knock when the door "
                f"opens and out steps a {enemy}.")
    print_delay(f"Eep! This is the {enemy}'s house!")
    print_delay(f"The {enemy} attacks you!\n")
    if "sword" not in item:
        print_delay("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?\n")
        if choice2 == "1":
            if "sword" in item:
                print_delay(f"As the {enemy} moves to attack, "
                            "you unsheath your new sword.")
                print_delay(f"The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_delay(f"But the {enemy} takes one look at "
                            "your shiny new toy and runs away!")
                print_delay(f"You have rid the town of the {enemy}."
                            "\nYou are victorious!\n")
            else:
                print_delay("You do your best...")
                print_delay(f"but your dagger is no match for the {enemy}.")
                print_delay("You have been defeated!\n")
            break
        if choice2 == "2":
            print_delay("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.\n")
            game_map()
            break


# Logic to choose between house and cave.
def game_map():
    print_delay("\nEnter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")
    print_delay("\nWhat would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house()
            break
        elif choice1 == "2":
            cave()
            break


# Logic to quit the game.
def play_again():
    again = ""
    while again not in ["y", "n"]:
        again = input("Would you like to play again? (y/n)\n")
        if again == "n":
            print_delay("\nThanks for playing! See you next time.\n")
            return "game_over"
        elif again == "y":
            print_delay("\nExcellent! Restarting the game ...\n")
            return "game_active"


# Logic to start the game with no weapons that can defeat an enemy.
state = 'game_active'
while state == 'game_active':

    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    item = []

    intro()
    game_map()

    state = play_again()
