# IMPORTS
import time
import random
# IMPORTS

# PARAMETERS
min = input("Enter the minimum value: ")
max = input("Enter the maximum value: ")
try:
    min = int(min)
    max = int(max)
except:
    print("You didn't enter the right values, so I'll go with 1 as min and 6 as max.")
    min = 1
    max = 6

if min > max:
    print("You didn't enter the right values, so going with 1 as min and 6 as max.")
    min = 1
    max = 6
else:
    print("Thanks for entering the correct inputs!")

# PARAMETERS

# UTILITY FUNCTIONS
def print_sleep(message, delay=0.1):
    print(message)
    time.sleep(delay)


def random_choice(min, max):
    return int(random.randint(min, max))


def get_play_again():
    print_sleep("Would you like to play again?", 0.2)
    print_sleep("Enter 0 for no and 1 for yes:")
    play = input("Play again [0/1] > ")
    if play == str(0):
        played = False
    elif play == str(1):
        played = True
    else:
        print("I don't know that, so bye!")
        exit()
    return played
# UTILITY FUNCTIONS

# RANDOMIZED VARIABLES
random_choice = int(random_choice(min, max))
random_choice_half = (random_choice / 2)
# RANDOMIZED VARIABLES

# GAME FUNCTION
def game():
    if random_choice <= random_choice_half:
        print_sleep(
            "You find yourself standing in a open field, filled with grass and yellow wildflowers.")
        print_sleep(
            "Rumor has it that a gorgon is somewhere around here, and has been terrifying the nearby village.")
        print_sleep("In front of you is a house.")
        print_sleep("To your right is a dark cave.")
        print_sleep(
            "In your hand you hold your trusty (but not very effective) dagger.")
        print_sleep("\nEnter 0 to knock on the door of the house.")
        print_sleep("Enter 1 to peer into the cave.")
        inputd = input("Enter 0 or 1 [0/1] > ")
        try:
            inputd = int(inputd)
        except:
            print(
                "You didn't enter the correct input, I'm asking you if you want to play again!")
            result = get_play_again()
            if result == True:
                game()
            else:
                exit()
        if inputd == 0:
            print_sleep("You are about to knock and the troll attacks you!")
            print_sleep("Since you died, I'm asking you if you want to play again!")
            result = get_play_again()
            if result == True:
                game()
            else:
                exit()
        else:
            print_sleep("Oh no! Something attacked you and you died. For that, I'm asking you if you want to play again.")
            result = get_play_again()
            if result == True:
                game()
            else:
                exit()

    else:
        print_sleep("You find yourself in a dark dungeon.")
        print_sleep("In your pocket is a shiny Swiss Knife.")
        print_sleep("In the cave, you hear angry bears screaming.")
        try:
            response_choice = int(input(
                "If you want to stay in the cave, enter 0, if you want to get out of the cave through the exit that is far away, enter 1: [0/1] > "))
        except:
            print(
                "Since you didn't enter the right input (0/1), I'm asking you if you want to play again.")
            result = get_play_again()

        if response_choice == 0:
            print_sleep("Great choice! You found an awesome sword!")
            print_sleep(
                "Now, would you like to exit the cave or build a shelter in the cave?")
            try:
                response_choice = int(
                    input("Enter 0 to exit the cave or 1 to build a shelter [0/1] > "))
            except:
                print_sleep("Oops! You didn't enter the right input!")
                result = get_play_again()
                if result == True:
                    game()
                else:
                    exit()
            if response_choice == 0:
                print_sleep(
                    "Oops, since the cave exit is too far away, you're stranded!")
                result = get_play_again()
                if result == True:
                    game()
                else:
                    exit()
            else:
                print_sleep(
                    "Oops, since the bears found you, you're stuck in the cave forever!")
                result = get_play_again()
                if result == True:
                    game()
                else:
                    exit()

        else:
            print_sleep(
                "Oops! Since the cave's exit is to far away, your food ran out and you're stranded.")
            result = get_play_again()
            if result == True:
                game()
            else:
                exit()
# GAME FUNCTION

# MAIN CALL
if __name__ == "__main__":
    game()
# MAIN CALL