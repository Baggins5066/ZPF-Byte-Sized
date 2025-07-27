# Zombie Pro Fisher - Byte Sized (Remake)
import random
import time

def slow_print(text, delay=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def choose(prompt, options):
    while True:
        print(prompt)
        for key, desc in options.items():
            print(f"{key}) {desc}")
        choice = input("> ").strip().upper()
        if choice in options:
            return choice
        print("Invalid entry.")

class Player:
    def __init__(self):
        self.health = 8
        self.max_health = 8
        self.hunger = 10
        self.luck = 0
        self.damage = 1
        self.money = 10
        self.wood = 0
        self.stone = 0
        self.machineparts = 0
        self.fishingrod = "Stick And String"
        self.weapon = "Fists"
        self.armor = []
        self.fish = []
        self.cookbook = False
        self.name = ""
        self.location = "Forest"
        self.turns = 0

    def stats(self):
        print(f"\nNAME: {self.name}")
        print(f"HEALTH: {self.health}/{self.max_health}")
        print(f"DAMAGE: {self.damage}")
        print(f"LUCK: {self.luck}")
        print(f"HUNGER: {self.hunger}")
        print(f"MONEY: {self.money}")
        print(f"WOOD: {self.wood}")
        print(f"STONE: {self.stone}")
        print(f"MACHINE PARTS: {self.machineparts}")
        print(f"FISHING ROD: {self.fishingrod}")
        print(f"WEAPON: {self.weapon}")
        print(f"ARMOR: {', '.join(self.armor) if self.armor else 'None'}")
        print(f"FISH: {', '.join(self.fish) if self.fish else 'None'}\n")

    def update_stats(self):
        if self.hunger > 10:
            self.hunger = 10
        if self.health > self.max_health:
            self.health = self.max_health
        if self.hunger < 0:
            self.hunger = 0
            self.health -= 1
            print("You are starving! -1 HP")

LOCATIONS = ["Forest", "Lake", "Nuclear Plant", "Shack"]

FISH_TABLE = [
    ("Catfish", 1, 10, "common"),
    ("Smallmouth Bass", 11, 20, "common"),
    ("Crappie", 21, 30, "common"),
    ("Bluegill", 31, 40, "common"),
    ("Largemouth Bass", 41, 45, "rare"),
    ("Trout", 46, 50, "rare"),
    ("Snail", 51, 55, "rare"),
    ("Frog", 56, 60, "rare"),
    ("Sturgeon", 61, 63, "epic"),
    ("Walleye", 64, 66, "epic"),
    ("Paddlefish", 67, 69, "epic"),
    ("Zombie Fish", 70, 71, "legendary"),
    ("Mighty Bluegill", 72, 74, "legendary"),
]

WEAPONS = [
    ("Fists", 1, 0),
    ("Knife", 1, 5),
    ("Machete", 2, 10),
    ("Axe", 3, 20),
    ("Pistol", 4, 40),
    ("SMG", 5, 80),
    ("Shotgun", 6, 160),
    ("AR-15", 7, 200),
    ("Sniper", 8, 250),
    ("Brass Knuckles", 9, 400),
    ("Spiked Bat", 10, 600),
]

RODS = [
    ("Stick And String", 0, 0),
    ("Common Rod", 1, 5),
    ("Sturdy Rod", 2, 20),
    ("Premium Rod", 3, 50),
    ("Deep Sea Rod", 4, 100),
    ("Jody Barrs Rod", 5, 250),
]

ARMOR = [
    ("Medkit", "heal", 2, 10),
    ("Nurse Aimees Power Kit", "fullheal", 0, 30),
    ("Ollies Leather Coat", "maxhp", 1, 50),
    ("Tactical Kerpants", "maxhp", 2, 100),
    ("Clemuratan Helmet", "maxhp", 3, 150),
]

FOOD = [
    ("Sage Cookies", 2, 8),
    ("Mrs Sierras Pasta", 4, 11),
    ("Chicky-fi-laa", 8, 20),
    ("Missys Cookbook", "cookbook", 0, 50),
]

def character_creation(player):
    slow_print("Welcome to Zombie Pro Fisher - Byte Sized!")
    time.sleep(1)
    slow_print("\n~*~ Character Customization ~*~\n")
    # Eye color
    eye = choose("Choose eye color:", {"A": "Blue (+2 luck)", "B": "Brown (+1 damage)", "C": "Green (+2 max health)"})
    if eye == "A": player.luck += 2
    elif eye == "B": player.damage += 1
    elif eye == "C": player.max_health += 2
    # Hair color
    hair = choose("Choose hair color:", {"A": "Blonde (+2 luck)", "B": "Brown (+1 damage)", "C": "Black (+2 max health)"})
    if hair == "A": player.luck += 2
    elif hair == "B": player.damage += 1
    elif hair == "C": player.max_health += 2
    # Size
    size = choose("Choose size:", {"A": "Short (+2 luck)", "B": "Tall (+1 damage)", "C": "Medium (+2 max health)"})
    if size == "A": player.luck += 2
    elif size == "B": player.damage += 1
    elif size == "C": player.max_health += 2
    player.name = input("Now, what is your hero's name? ")
    player.health = player.max_health
    slow_print(f"\nStarting your journey now! Here are your stats:")
    player.stats()
    # Random spawn
    player.location = random.choice(LOCATIONS)
    slow_print(f"\nSPAWNING CHARACTER...")
    time.sleep(1)
    slow_print(f"You arrive at the {player.location.upper()}.")

def zombie_encounter(player):
    if player.location == "Shack": return
    spawn_chance = random.randint(0, 10)
    if (spawn_chance >= 9 and player.location != "Shack") or (spawn_chance >= 5 and player.location == "Nuclear Plant"):
        zombie_hp = random.randint(5, 15)
        slow_print("\nZOMBIE ENCOUNTER!")
        while zombie_hp > 0 and player.health > 0:
            print(f"Zombie HP: {zombie_hp} | Your HP: {player.health}")
            action = choose("What do you do?", {"A": "Attack", "B": "Run away"})
            if action == "A":
                dmg = random.randint(0, 3) + player.damage
                slow_print(f"You hit the zombie for {dmg}!")
                zombie_hp -= dmg
                if zombie_hp <= 0:
                    reward = random.randint(1, 10)
                    slow_print(f"You killed the zombie! You got ${reward}.")
                    player.money += reward
                    break
                z_dmg = random.randint(0, 9)
                slow_print(f"The zombie hits you for {z_dmg}!")
                player.health -= z_dmg
            else:
                escape = random.randint(0, 20) + int(player.luck * 1.5)
                if escape >= 12:
                    slow_print("You successfully got away!")
                    break
                else:
                    slow_print("The zombie caught up to you!")
                    z_dmg = random.randint(0, 9)
                    slow_print(f"The zombie hits you for {z_dmg}!")
                    player.health -= z_dmg
        if player.health <= 0:
            slow_print("\nYOU DIED\nYou lasted {} turns. Not bad!".format(player.turns))
            return True
    return False

def forage(player):
    if player.location == "Nuclear Plant":
        slow_print("You're not sure there's anything safe to eat here...")
        return
    if player.location == "Shack":
        slow_print("Mr. Hutchinson tells you to stop snooping around in his shop.")
        return
    player.hunger -= 1
    result = random.randint(-10, 32) + int(player.luck * 1.9)
    if result <= 0:
        slow_print("You found nothing.")
    elif (result <= 10 and not player.cookbook) or (result <= 5 and player.cookbook):
        hp_loss = random.randint(1, 3)
        player.health -= hp_loss
        slow_print(f"Yuck! You ate something you shouldn't have. -{hp_loss} HP.")
    elif (result <= 20 and not player.cookbook) or (result <= 20 and player.cookbook):
        slow_print("You found some nuts and berries. +2 Hunger")
        player.hunger += 2
    elif result <= 25:
        slow_print("You're not sure what you found, but the geiger counter didn't beep - so it's probably safe. +3 Hunger.")
        player.hunger += 3
    elif result <= 30:
        slow_print("You trapped some local fauna and ate a well-cooked meal. +4 Hunger.")
        player.hunger += 4
    elif result <= 35:
        found = random.choice(WEAPONS[1:])
        slow_print(f"You found a weapon! {found[0]}")
        action = choose("Take the weapon or scrap it?", {"A": "Take", "B": "Scrap"})
        if action == "A":
            player.weapon = found[0]
            player.damage = found[1]
        else:
            parts = random.randint(0, 2)
            player.machineparts += parts
            slow_print(f"You got {parts} machine parts.")
    elif result >= 40:
        slow_print("You find a bright green triangular shape. It is crushed and deformed. On it is written '663D'. You hang onto it. It seems like good luck.")

def fishing(player):
    player.hunger -= 1
    roll = random.randint(-74, 74) + int(player.luck * 1.9)
    caught = None
    for fish, low, high, rarity in FISH_TABLE:
        if low <= roll <= high:
            caught = fish
            break
    if caught:
        slow_print(f"You caught a {caught}!")
        player.fish.append(caught)
    else:
        slow_print("You caught nothing today...")

def gather(player, resource):
    amount = random.randint(0, 5)
    slow_print(f"You gathered {amount} pieces of {resource}.")
    if resource == "wood":
        player.wood += amount
    elif resource == "stone":
        player.stone += amount
    elif resource == "machinery":
        player.machineparts += amount
    player.hunger -= 1

def shop(player):
    slow_print("Mr Hutchinson greets you with a warm nod and a gruffy smile.")
    while True:
        action = choose("What would you like to do?", {
            "A": "Buy weapons",
            "B": "Buy/sell fishing goods",
            "C": "Armor Shop",
            "D": "Craft",
            "E": "Sage Snack Shack",
            "F": "Goodbye"
        })
        if action == "A":
            for i, (name, dmg, cost) in enumerate(WEAPONS[1:], 1):
                print(f"{chr(64+i)}) {name} (+{dmg} DMG) - ${cost}")
            print(f"{chr(64+len(WEAPONS))}) Go Back")
            choice = input("> ").strip().upper()
            idx = ord(choice) - 65
            if 0 <= idx < len(WEAPONS)-1 and player.money >= WEAPONS[idx+1][2]:
                player.weapon = WEAPONS[idx+1][0]
                player.damage = WEAPONS[idx+1][1]
                player.money -= WEAPONS[idx+1][2]
                slow_print(f"You bought {player.weapon}!")
            elif choice == chr(64+len(WEAPONS)):
                continue
            else:
                slow_print("Not enough money or invalid choice.")
        elif action == "B":
            rod_options = {chr(65+i): f"{rod[0]} (+{rod[1]} Luck) - ${rod[2]}" for i, rod in enumerate(RODS[1:])}
            rod_options[chr(65+len(RODS[1:]))] = "Sell your fish"
            rod_options[chr(66+len(RODS[1:]))] = "Goodbye"
            for k, v in rod_options.items(): print(f"{k}) {v}")
            choice = input("> ").strip().upper()
            idx = ord(choice) - 65
            if 0 <= idx < len(RODS[1:]) and player.money >= RODS[idx+1][2]:
                player.fishingrod = RODS[idx+1][0]
                player.luck = RODS[idx+1][1]
                player.money -= RODS[idx+1][2]
                slow_print(f"You bought {player.fishingrod}!")
            elif choice == chr(65+len(RODS[1:])):
                # Sell fish
                rarity_values = {"common": 2, "rare": 4, "epic": 7, "legendary": 10}
                total = 0
                for fish in player.fish:
                    for f, _, _, rarity in FISH_TABLE:
                        if fish == f:
                            total += rarity_values[rarity]
                player.money += total
                slow_print(f"You sold your fish for ${total}.")
                player.fish = []
            elif choice == chr(66+len(RODS[1:])):
                continue
            else:
                slow_print("Not enough money or invalid choice.")
        elif action == "C":
            for i, (name, typ, val, cost) in enumerate(ARMOR, 1):
                print(f"{chr(64+i)}) {name} - ${cost}")
            print(f"{chr(64+len(ARMOR)+1)}) Goodbye")
            choice = input("> ").strip().upper()
            idx = ord(choice) - 65
            if 0 <= idx < len(ARMOR) and player.money >= ARMOR[idx][3]:
                name, typ, val, cost = ARMOR[idx]
                if typ == "heal":
                    player.health = min(player.health + val, player.max_health)
                elif typ == "fullheal":
                    player.health = player.max_health
                elif typ == "maxhp":
                    player.max_health += val
                    player.health += val
                    player.armor.append(name)
                player.money -= cost
                slow_print(f"You bought {name}!")
            elif choice == chr(64+len(ARMOR)+1):
                continue
            else:
                slow_print("Not enough money or invalid choice.")
        elif action == "D":
            print("A) Knife ($2, 5 wood, 4 stone)")
            print("B) Machete ($5, 6 wood, 10 stone)")
            print("C) Pistol ($10, 8 wood, 5 stone, 5 machine parts)")
            print("D) SMG ($20, 7 wood, 10 stone, 10 machine parts)")
            print("E) Shotgun ($80, 10 wood, 15 stone, 20 machine parts)")
            print("F) Goodbye")
            choice = input("> ").strip().upper()
            if choice == "A" and player.money >= 2 and player.wood >= 5 and player.stone >= 4:
                player.weapon = "Knife"
                player.damage = 1
                player.money -= 2
                player.wood -= 5
                player.stone -= 4
                slow_print("You crafted a Knife!")
            elif choice == "B" and player.money >= 5 and player.wood >= 6 and player.stone >= 10:
                player.weapon = "Machete"
                player.damage = 2
                player.money -= 5
                player.wood -= 6
                player.stone -= 10
                slow_print("You crafted a Machete!")
            elif choice == "C" and player.money >= 10 and player.wood >= 8 and player.stone >= 5 and player.machineparts >= 5:
                player.weapon = "Pistol"
                player.damage = 3
                player.money -= 10
                player.wood -= 8
                player.stone -= 5
                player.machineparts -= 5
                slow_print("You crafted a Pistol!")
            elif choice == "D" and player.money >= 20 and player.wood >= 7 and player.stone >= 10 and player.machineparts >= 10:
                player.weapon = "SMG"
                player.damage = 4
                player.money -= 20
                player.wood -= 7
                player.stone -= 10
                player.machineparts -= 10
                slow_print("You crafted an SMG!")
            elif choice == "E" and player.money >= 80 and player.wood >= 10 and player.stone >= 15 and player.machineparts >= 20:
                player.weapon = "Shotgun"
                player.damage = 5
                player.money -= 80
                player.wood -= 10
                player.stone -= 15
                player.machineparts -= 20
                slow_print("You crafted a Shotgun!")
            elif choice == "F":
                continue
            else:
                slow_print("Not enough resources or invalid choice.")
        elif action == "E":
            for i, (name, val, cost) in enumerate(FOOD, 1):
                print(f"{chr(64+i)}) {name} - ${cost}")
            print(f"F) Goodbye")
            choice = input("> ").strip().upper()
            idx = ord(choice) - 65
            if 0 <= idx < len(FOOD) and player.money >= FOOD[idx][2]:
                name, val, cost = FOOD[idx]
                if name == "Missys Cookbook":
                    player.cookbook = True
                else:
                    player.hunger += val
                player.money -= cost
                slow_print(f"You bought {name}!")
            elif choice == "F":
                continue
            else:
                slow_print("Not enough money or invalid choice.")
        elif action == "F":
            break

def main():
    player = Player()
    character_creation(player)
    while player.health > 0:
        player.turns += 1
        player.update_stats()
        if zombie_encounter(player):
            break
        print("\nWhat would you like to do?")
        options = {}
        if player.location == "Forest":
            options = {"A": "Forage", "B": "Change location", "C": "Check stats", "D": "Gather wood", "E": "Watch birds"}
        elif player.location == "Lake":
            options = {"A": "Forage", "B": "Change location", "C": "Check stats", "D": "Go fishing", "E": "Gather rocks"}
        elif player.location == "Nuclear Plant":
            options = {"A": "Forage", "B": "Change location", "C": "Check stats", "D": "Gather machine parts", "E": "Listen to echoes"}
        elif player.location == "Shack":
            options = {"A": "Forage", "B": "Change location", "C": "Check stats", "D": "Interact with Mr. Hutchinson", "E": "Rest by the fire"}
        choice = choose("Choose an action:", options)
        if choice == "A":
            forage(player)
        elif choice == "B":
            locs = {"A": "Forest", "B": "Lake", "C": "Nuclear Plant", "D": "Shack"}
            loc_choice = choose("Where would you like to go?", locs)
            if locs[loc_choice] == player.location:
                slow_print("You can't travel to a place you're already at.")
            else:
                player.location = locs[loc_choice]
                slow_print(f"You travel to the {player.location}.")
        elif choice == "C":
            player.stats()
        elif choice == "D":
            if player.location == "Forest":
                gather(player, "wood")
            elif player.location == "Lake":
                fishing(player)
            elif player.location == "Nuclear Plant":
                gather(player, "machinery")
            elif player.location == "Shack":
                shop(player)
        elif choice == "E":
            if player.location == "Forest":
                event = random.randint(1, 4)
                if event == 1:
                    slow_print("The birds are lively today. +1 HP.")
                    player.health = min(player.health + 1, player.max_health)
                elif event == 2:
                    slow_print("There are only a few birds today. You find peace in solitude.")
                elif event == 3:
                    slow_print("No birds today. It's quiet and eerie. -1 Damage.")
                    player.damage = max(1, player.damage - 1)
                elif event == 4:
                    slow_print("You see large birds. +1 luck, -1 Hunger.")
                    player.luck += 1
                    player.hunger -= 1
            elif player.location == "Lake":
                gather(player, "stone")
            elif player.location == "Nuclear Plant":
                event = random.randint(1, 4)
                if event == 1:
                    slow_print("You hear the humming of a machine. +1 HP.")
                    player.health = min(player.health + 1, player.max_health)
                elif event == 2:
                    slow_print("You hear water dripping in the dark corridors.")
                elif event == 3:
                    slow_print("You hear zombie screeches. -1 damage.")
                    player.damage = max(1, player.damage - 1)
                elif event == 4:
                    slow_print("You hear metal drop in the distance. +1 money.")
                    player.money += 1
            elif player.location == "Shack":
                slow_print("The fire reminds you of home.")
    slow_print("Game Over. Thanks for playing!")

if __name__ == "__main__":
    main()
