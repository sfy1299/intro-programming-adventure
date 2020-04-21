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


def get_play_again():
    print_sleep("Would you like to play again?")
    print_sleep("Enter 1 for no\nEnter 2 for yes")
    play = int(input("(Please enter 1 or 2.)\n"))

    if play == 1:
        exit()
    else:
        game()
# UTILITY FUNCTIONS


# RANDOMIZED VARIABLES
random_choice = random_choice_func(1, 6)
random_test = random_choice_func(1, 6)
# RANDOMIZED VARIABLES


# GAME FUNCTION
def game():
    if random_choice <= random_test:
        print_sleep("You find yourself standing in a field, with wildflowers.")
        print_sleep(
            "Rumor has that gorgon somewhere here, and terrifying the village."
        )
        print_sleep("In front of you is a house.")
        print_sleep("To your right is a dark cave.")
        print_sleep(
            "In your hand you hold your trusty (but not effective) dagger."
        )
        print_sleep(
            "\nEnter 1 to knock on the door.\nEnter 2 to go into the cave."
        )
        inputd = int(input("(Please enter 1 or 2.)\n"))
        if inputd == 1:
            print_sleep("You are about to knock and the troll attacks you!")
            print_sleep(
                "Since you died, I'm asking you if you want to play again!"
            )
            get_play_again()
        else:
            print_sleep(
                "Oh no! You died! :( Asking you if you want to play again."
            )
            get_play_again()

    else:
        print_sleep("You find yourself in a dark dungeon.")
        print_sleep("In your pocket is a shiny Swiss Knife.")
        print_sleep("In the cave, you hear angry bears screaming.")
        print_sleep("Enter 1 to stay in cave\nEnter 2 to get out of cave.")
        response_choice = int(input("(Please enter 1 or 2.)\n"))

        if response_choice == 1:
            print_sleep("Great choice! You found an awesome sword!")
            print_sleep("Exit cave or build a shelter in the cave?")
            print_sleep("Enter 1 to exit cave\nEnter 2 to build shelter.")
            response_choice = int(input("(Please enter 1 or 2.)\n"))

            if response_choice == 1:
                print_sleep(
                    "Oops, the cave exit is too far away, you're stranded!"
                )
                print_sleep("Enter 1 to exit cave\nEnter 2 to build a shelter")
                response_choice = int(input("(Please enter 1 or 2.)\n"))
                if response_choice == 1:
                    print_sleep("The cave exit is far away, you're stranded!")
                    get_play_again()
                else:
                    print_sleep("Bears found you, stuck in the cave forever!")
                    get_play_again()
            else:
                print_sleep(
                    "The bears found you, you're stuck in the cave forever!"
                )
                get_play_again()

        else:
            print_sleep(
                "Oops! Since the cave's exit is to far, your food ran out."
            )
            get_play_again()
# GAME FUNCTION


# MAIN CALL
if __name__ == "__main__":
    game()
# MAIN CALL
