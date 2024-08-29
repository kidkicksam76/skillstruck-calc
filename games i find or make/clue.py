import random

# List of potential suspects, locations, and weapons
suspects = ["Mr. Green", "Mrs. Peacock", "Professor Plum", "Miss Scarlet", "Colonel Mustard"]
weapons = ["knife", "candlestick", "revolver", "rope", "lead pipe"]
locations = ["kitchen", "ballroom", "library", "study", "dining room"]

# Randomly select the murderer, the weapon, and the crime scene
murderer = random.choice(suspects)
murder_weapon = random.choice(weapons)
crime_scene = random.choice(locations)

def show_intro():
    print("Welcome to the Murder Mystery Game!")
    print("There has been a murder, and it's up to you to solve it.")
    print("You need to find out WHO the murderer is, WHAT weapon was used, and WHERE the murder took place.\n")

def ask_suspect(suspect):
    # Each suspect gives a clue, or lies if they are the murderer
    if suspect == murderer:
        print(f"{suspect} says: I was in the {random.choice(locations)}, but I didn't see anything suspicious.")
    else:
        print(f"{suspect} says: I was in the {random.choice([loc for loc in locations if loc != crime_scene])}, and I think the weapon was the {random.choice(weapons)}.")

def make_accusation():
    print("\nIt's time to make your accusation.")
    accused_murderer = input("Who do you think the murderer is? ")
    accused_weapon = input("What weapon do you think was used? ")
    accused_location = input("Where do you think the murder took place? ")

    if accused_murderer == murderer and accused_weapon == murder_weapon and accused_location == crime_scene:
        print(f"\nCongratulations! You solved the mystery. {murderer} committed the murder with the {murder_weapon} in the {crime_scene}.")
    else:
        print(f"\nWrong accusation! The real culprit was {murderer}, who used the {murder_weapon} in the {crime_scene}. Better luck next time!")

def main_game():
    show_intro()
    
    rounds = 5  # The player has 3 rounds to ask suspects
    asked_suspects = []
    
    while rounds > 0:
        print(f"\nYou have {rounds} rounds left. Choose someone to question: ")
        for suspect in suspects:
            if suspect not in asked_suspects:
                print(f"- {suspect}")
        
        chosen_suspect = input("\nWho would you like to ask? ").title()
        
        if chosen_suspect in suspects and chosen_suspect not in asked_suspects:
            ask_suspect(chosen_suspect)
            asked_suspects.append(chosen_suspect)
            rounds -= 1
        else:
            print("Invalid choice or you've already asked that person.")
    
    make_accusation()

# Start the game
main_game()
