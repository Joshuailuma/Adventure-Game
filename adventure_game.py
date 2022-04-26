import time
import random
from string import Template

# This function triggers messages passed into
# it to display after a 2 seconds delay


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(antagonist, items):
    print_pause("You find yourself standing in an open "
                "field, filled with grass and yellow wildflowers.")
    print_pause(Template("Rumor has it that a $template is "
                         "somewhere around here, and has been "
                         "terrifying the nearby "
                         "village.").substitute(template=antagonist))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    enter_input(antagonist, items)


def fight(antagonist, items):
    if "sword" in items:
        print_pause(Template("As the $template comes "
                    "to attack, you unsheath your "
                             "new sword.").substitute(template=antagonist))
        print_pause("The Sword of Ogoroth shines brightly "
                    "in your hand as you brace yourself "
                    "for the attack")
        print_pause("The " + antagonist + " takes one look "
                    "at your fancy new toy and runs away.")
        print_pause("You have rid the town of the " + antagonist + ". "
                    "You are victorious!")

        response = input("Would you like to play again? (y/n)").lower()
        if "y" in response:
            print_pause("Excellent. Restarting the Game...\n")
            start_game()
        elif "n" in response:
            print_pause("Goodbye! Thanks for playing.")
        else:
            print_pause("You entered a wrong "
                        "input! Thanks for playing.")
    else:
        print_pause("You do your best")
        print_pause("But your dagger is no match "
                    "for the " + antagonist + ".")
        print_pause("You have been defeated")

        response = input("Would you like to play again? (y/n)").lower()
        if "y" in response:
            print_pause("Excellent. Restarting the Game...")
            start_game()
        elif "n" in response:
            print_pause("Goodbye! Thanks for playing.")
        else:
            print_pause("You entered a wrong "
                        "input! Thanks for playing")


def run_away(antagonist, items):
    print_pause("You run back into the field, luckily "
                "you don\'t seem to have been followed")
    print_pause("")
    enter_input(antagonist, items)


def peer_into_cave(items):
    if "sword" in items:
        print_pause("You peer cautiously into the cave")
        print_pause("You\'ve  been here before and gotten "
                    "all the good stuff, it\'s just an empty "
                    "cave now")
    else:
        print_pause("You peer cautiously into the cave")
        print_pause("It turns out to be a very small cave")
        print_pause("Your eye catches a glint of metal "
                    "behind a rock")
        print_pause("You have found the magical sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you")
        print_pause("You walk back out of the field")
        print_pause("")
        items.append("sword")


def knock_door(antagonist, items):
    if "sword" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door "
                    "opens and out steps a " + antagonist + ".")
        print_pause("Epp! This is a " + antagonist + "'s house!")
        print_pause("The " + antagonist + " attacks you!")
        response = input("Would you like to (1) fight or (2) "
                         "run away?\n")
        if "1" in response:
            fight(antagonist, items)
        elif "2" in response:
            run_away(antagonist, items)
        else:
            knock_door(antagonist)
    else:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door "
                    "opens and out steps a " + antagonist + ".")
        print_pause("Epp! This is a " + antagonist + "'s house!")
        print_pause("The " + antagonist + " attacks you!")
        print_pause("You feel a little under-prepared for "
                    "this-what with only having a tiny dagger")
        response = input("Would you like to (1) fight or (2) "
                         "run away?\n")
        if "1" in response:
            fight(antagonist, items)
        elif "2" in response:
            run_away(antagonist, items)
        else:
            knock_door(antagonist)


def enter_input(antagonist, items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = input("What would you like to do?\n")
    if "1" in response:
        knock_door(antagonist, items)
    elif "2" in response:
        peer_into_cave(items)
        enter_input(antagonist, items)
    else:
        enter_input(antagonist, items)


def start_game():
    items = []
    antagonist = random.choice(["wicked fairie", "pirate",
                                "dragon", "troll", "killer"])
    intro(antagonist, items)


start_game()

