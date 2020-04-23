# IMPORTS
import time
import random
# IMPORTS

# PARAMETERS


# UTILITY FUNCTIONS
def print_sleep(message, delay=0.1):
    print(message)
    time.sleep(delay)


def random_choice_func(min, max):
    return random.randint(min, max)


def ask_question_again():
    print_sleep("\nWhat would you like to do?")


def get_play_again():
    play = input("\nWould you like to play again? (y/n)")

    if play == "n":
        print_sleep("\nThanks for playing! See you next time.")
        exit()
    elif play == "y":
        game()
    else:
        get_play_again()

# UTILITY FUNCTIONS


def setupHouseScene(isSkip=False):
    if isSkip:
        ask_question_again()
        inputHouse = ask_question()
    else:
        inputHouse = house()

    if inputHouse == "1":
        print_sleep("You do your best...")
        print_sleep("But your dagger is no match for the pirate.")
        print_sleep("You have been defeated!")
        get_play_again()
    elif inputHouse == "2":
        print_sleep(
            "Run back into the field, don't seem to have been followed.")
        setupScene1()
    else:
        setupHouseScene(True)


def setupCaveScene(isSkip=False):
    if isSkip:
        ask_question_again()
        inputCave = ask_question()
    else:
        inputCave = cave()

    if inputCave == "1":
        setupHouseScene()
    elif inputCave == "2":
        print_sleep("You peer cautiously into the cave.")
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep(
            "You discard your silly old dagger and take the sword with you.")
        print_sleep("You walk back out to the field.")

        setupScene1()
    else:
        setupCaveScene(True)


def setupFieldScene(isSkip=False):
    if isSkip:
        ask_question_again()
        inputField = ask_question()
    else:
        inputField = field()

    if inputField == "1":
        print_sleep("You do your best...")
        print_sleep("You have been defeated by the monster!")
        get_play_again()
    elif inputField == "2":
        setupCaveScene()
    else:
        setupFieldScene(True)


def setupScene1(isSkip=False):
    if not isSkip:
        print_sleep("\nEnter 1 to knock on the door of the house.")
        print_sleep("Enter 2 to peer into the cave.")

    inputd = ask_question()

    if inputd == "1":
        setupHouseScene()
    elif inputd == "2":
        setupCaveScene()
    else:
        setupScene1(True)


def setupScene2(isSkip=False):
    if isSkip:
        print_sleep("Enter 1 to stay in cave\nEnter 2 to get out of cave.")

    inputd = ask_question()

    if inputd == "1":
        setupCaveScene()
    elif inputd == "2":
        setupFieldScene()
    else:
        setupScene2(True)


def house():
    # Things that happen to the player in the house
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock when the door opens")
    print_sleep("Eep! This is the pirate's house!")
    print_sleep("The pirate attacks you!")
    print_sleep("You feel a bit under-prepared for this, what would you do?")
    print_sleep("Would you like to (1) fight or (2) run away?")

    return ask_question()


def cave():
    # Things that happen to the player in the cave
    print_sleep("You peer cautiously into the cave.")
    print_sleep("It turns out to be only a very small cave.")
    print_sleep("Your eye catches a glint of metal behind a rock.")
    print_sleep("You have found the magical Sword of Ogoroth!")
    print_sleep("You discard silly old dagger and take the sword")
    print_sleep("You walk back out to the field.")
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")

    return ask_question()


def field():
    # Things that happen to the player in the field
    print_sleep("Beautiful empty field is right in front of you")
    print_sleep("Suddenly, a monster show up and try to attack you")
    print_sleep("You lost the magical Sword while you are running")
    print_sleep("Enter 1 to fight with the monster")
    print_sleep("Enter 2 to run back into the cave.")
    print_sleep("What would you like to do?")

    return ask_question()


def ask_question():
    return input("(Please enter 1 or 2.)\n")


# RANDOMIZED VARIABLES
random_choice = random_choice_func(1, 6)
random_test = random_choice_func(1, 6)
# RANDOMIZED VARIABLES

# GAME FUNCTION


def game():
    if random_choice <= random_test:
        print_sleep(
            "Standing in a field, with grass and wildflowers.")
        print_sleep(
            "Gorgon somewhere may be here, and terrifying the village.")
        print_sleep("In front of you is a house.")
        print_sleep("To your right is a dark cave.")
        print_sleep(
            "In your hand you hold your trusty dagger.")

        setupScene1()

    else:
        print_sleep("You find yourself in a dark dungeon.")
        print_sleep("In your pocket is a shiny Swiss Knife.")
        print_sleep("In the cave, you hear angry bears screaming.")
        print_sleep("Enter 1 to stay in cave\nEnter 2 to get out of cave.")

        setupScene2()
# GAME FUNCTION


# MAIN CALL
if __name__ == "__main__":
    game()
# MAIN CALL
