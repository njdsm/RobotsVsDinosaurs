import fleet
import herd


def user_prompt(string, options):
    while True:
        try:
            choice = int(input(string))
            if options >= choice > 0:
                return choice
        except:
            print("Not one of your options. :")


def display(number, fleet, herd):
    i = 1
    if number == 1:
        for bot in fleet.robots:
            print(f"{i}:")
            print("Name: " + bot.name)
            print("Power Level: " + str(bot.power_level))
            print("Health: " + str(bot.health))
            print("Weapon: " + str(bot.weapon.type) + "\n   Damage: " + str(bot.weapon.attack_power) + "\n")
            i += 1
    elif number == 2:
        for dino in herd.dinosaurs:
            print(f"{i}:")
            print("Type: " + dino.type)
            print("Energy: " + str(dino.energy))
            print("Health: " + str(dino.health))
            print("Attack Power: " + str(dino.attack_power) + "\n")
            i += 1
    print("\n")
