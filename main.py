from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd
from weapon import Weapon
from utils import *
import os


def display(number):
    if number == 1:
        for bot in fleet.robots:
            print("Name: " + bot.name)
            print("Power Level: " + str(bot.power_level))
            print("Health: " + str(bot.health))
            print("Weapon: " + str(bot.weapon.type) + "\n   Damage: " + str(bot.weapon.attack_power) + "\n")
    elif number == 2:
        for dino in herd.dinosaurs:
            print("Type: " + dino.type)
            print("Energy: " + str(dino.energy))
            print("Health: " + str(dino.health))
            print("Attack Power: " + str(dino.attack_power) + "\n")
    print("\n")


if __name__ == '__main__':
    # Set up the objects and get some info from the user
    battlefield = Battlefield()
    fleet = Fleet()
    herd = Herd()
    name = input("What is your Name? :")
    player = battlefield.display_welcome()
    if player == 1:
        player_banner = f"{name}'s Robots"
        computer_banner = "Computer's Dinosaurs"
        computer = 2
    else:
        player_banner = "Player One's Dinosaurs"
        computer_banner = "Computer's Robots"
        computer = 1
    team_size = user_prompt("How many on each team? Less than 10 please. :", 10)
    herd.create_herd(team_size)
    fleet.create_fleet(team_size)
    battlefield.fleet = fleet
    battlefield.herd = herd
    print("\n" * 10)
    print(player_banner)
    display(player)
    print(computer_banner)
    display(computer)
    input("Press enter to start the game...")

    # start the game


