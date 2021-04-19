from fleet import Fleet
from herd import Herd
from utils import *


class Battlefield:
    # Constructor and Member variables
    def __init__(self):
        self.fleet = None
        self.herd = None

    def run_game(self):
        fleet = Fleet()
        herd = Herd()
        player = self.display_welcome()
        team_size = user_prompt("How many on each team? Less than 10 please. :", 10)
        herd.create_herd(team_size)
        fleet.create_fleet(team_size, player)
        self.fleet = fleet
        self.herd = herd
        print("\n" * 10)
        display(self.fleet, self.herd)
        input("Press enter to start the game...")
        winner = None
        game_on = True
        while game_on:
            choice = None
            print("Your turn!\n")
            if player == 1:
                choice = self.show_robo_opponent_options()
                if choice != "skip":
                    self.robo_turn(int(choice))
                # Computer Turn
                print(f"Computer's turn!\n")
                self.dino_turn(1, 2)
            else:
                choice = self.show_dino_opponent_options()
                if choice != "skip":
                    attack_type = user_prompt("What type of attack?\n1: Slam (more damage, higher energy cost)\n2: Bite\n:", 2)
                    self.dino_turn(int(choice), int(attack_type))
                # Computer Turn
                print(f"Computer's turn!\n")
                self.robo_turn(1)
            # Check for dead
            if self.herd.dinosaurs[0].health <= 0:
                print(f"{self.herd.dinosaurs[0].type} has died!")
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
            if self.fleet.robots[0].health <= 0:
                print(f"{self.fleet.robots[0].name} has died!")
                self.fleet.robots.remove(self.fleet.robots[0])
            if len(self.herd.dinosaurs) < 1:
                winner = "Robots Win!"
                game_on = False
            if len(self.fleet.robots) < 1:
                winner = "Dinosaurs Win!"
                game_on = False
        self.display_winner(winner)

    def display_welcome(self):
        choice = user_prompt("Welcome to Dinosaurs Vs Robots!\nTo play as Robots enter 1\nTo play as Dinosaurs enter 2\n:", 2)
        return int(choice)

    def dino_turn(self, choice, attack_type):
        self.herd.dinosaurs[choice - 1].attack(self.fleet.robots[0], attack_type)

    def robo_turn(self, choice):
        self.fleet.robots[choice - 1].attack(self.herd.dinosaurs[0])

    def show_dino_opponent_options(self):
        print("What would you like to do?\n")
        i = 1
        while i <= len(self.herd.dinosaurs):
            print(f"{i}: Attack with " + self.herd.dinosaurs[i - 1].type)
            i = i + 1
        print(f"{len(self.herd.dinosaurs) + 1}: Charge Energy")
        print(f"{len(self.herd.dinosaurs) + 2}: Display units")
        choice = user_prompt("", len(self.herd.dinosaurs) + 2)
        if int(choice) == len(self.herd.dinosaurs) + 2:
            display(self.fleet, self.herd)
            return self.show_dino_opponent_options()
        elif int(choice) == len(self.herd.dinosaurs) + 1:
            self.herd.dinosaurs[0].energy = self.herd.dinosaurs[0].energy + 10
            return "skip"
        else:
            return choice

    def show_robo_opponent_options(self):
        print("What would you like to do?\n")
        i = 1
        while i <= len(self.fleet.robots):
            print(f"{i}: Attack with " + self.fleet.robots[i - 1].name)
            i += 1
        print(f"{len(self.fleet.robots) + 1}: Charge Energy")
        print(f"{len(self.fleet.robots) + 2}: Display units")
        choice = user_prompt("", len(self.fleet.robots) + 2)
        if int(choice) == len(self.fleet.robots) + 2:
            display(self.fleet, self.herd)
            display(self.fleet, self.herd)
            return self.show_robo_opponent_options()
        elif int(choice) == len(self.fleet.robots) + 1:
            for bot in self.fleet.robots:
                bot.power_level = bot.power_level + 10
            return "skip"
        else:
            return choice


    def display_winner(self, string):
        print(string)
