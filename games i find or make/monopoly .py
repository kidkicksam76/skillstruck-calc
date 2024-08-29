import random

# Define the board as a list of properties
board = [
    {"name": "Go", "price": 0, "rent": 0, "owner": None},
    {"name": "Mediterranean Avenue", "price": 60, "rent": 2, "owner": None},
    {"name": "Community Chest", "price": 0, "rent": 0, "owner": None},
    {"name": "Baltic Avenue", "price": 60, "rent": 4, "owner": None},
    {"name": "Income Tax", "price": 0, "rent": 200, "owner": None},
    {"name": "Reading Railroad", "price": 200, "rent": 25, "owner": None},
    {"name": "Oriental Avenue", "price": 100, "rent": 6, "owner": None},
    {"name": "Chance", "price": 0, "rent": 0, "owner": None},
    {"name": "Vermont Avenue", "price": 100, "rent": 6, "owner": None},
    {"name": "Connecticut Avenue", "price": 120, "rent": 8, "owner": None},
    {"name": "Jail", "price": 0, "rent": 0, "owner": None},
    # Continue defining properties as needed...
]

# Define a class for players
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []

    def move(self, steps):
        self.position = (self.position + steps) % len(board)
        print(f"{self.name} landed on {board[self.position]['name']}.")

    def buy_property(self):
        current_property = board[self.position]
        if current_property["owner"] is None:
            if self.money >= current_property["price"]:
                self.money -= current_property["price"]
                current_property["owner"] = self.name
                self.properties.append(current_property["name"])
                print(f"{self.name} bought {current_property['name']} for ${current_property['price']}.")
            else:
                print(f"{self.name} doesn't have enough money to buy {current_property['name']}.")
        else:
            print(f"{current_property['name']} is already owned by {current_property['owner']}.")

    def pay_rent(self):
        current_property = board[self.position]
        if current_property["owner"] and current_property["owner"] != self.name:
            rent = current_property["rent"]
            self.money -= rent
            owner = next(player for player in players if player.name == current_property["owner"])
            owner.money += rent
            print(f"{self.name} paid ${rent} in rent to {owner.name}.")
        elif current_property["owner"] == self.name:
            print(f"{self.name} landed on their own property.")

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Initialize players
players = [Player("Player 1"), Player("Player 2")]

def play_turn(player):
    input(f"\n{player.name}'s turn. Press Enter to roll the dice...")
    dice = roll_dice()
    print(f"{player.name} rolled {dice[0]} and {dice[1]} for a total of {sum(dice)}.")
    player.move(sum(dice))
    
    current_property = board[player.position]
    if current_property["price"] > 0:
        if current_property["owner"] is None:
            choice = input(f"Do you want to buy {current_property['name']} for ${current_property['price']}? (yes/no) ").lower()
            if choice == "yes":
                player.buy_property()
        else:
            player.pay_rent()
    else:
        print(f"{current_property['name']} is a special tile.")

def main_game():
    while True:
        for player in players:
            play_turn(player)
            if player.money <= 0:
                print(f"{player.name} is bankrupt! Game over.")
                return
            if len(player.properties) >= 3:  # Win condition for this simplified game
                print(f"{player.name} owns 3 properties and wins the game!")
                return

# Start the game
main_game()
