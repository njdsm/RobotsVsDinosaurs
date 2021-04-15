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
        name = input("What is your Name? :")
        player = self.display_welcome()
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
        self.fleet = fleet
        self.herd = herd
        print("\n" * 10)
        print(player_banner)
        display(player, self.fleet, self.herd)
        print(computer_banner)
        display(computer, self.fleet, self.herd)
        input("Press enter to start the game...")
        winner = None
        game_on = True
        while game_on:
            choice = None
            print(player_banner + " turn!")
            if player == 1:
                choice = int(self.show_robo_opponent_options())
                self.robo_turn(choice)
            else:
                choice = int(self.show_dino_opponent_options())
                self.dino_turn(choice)
            # Computer Turn
            print(computer_banner + " turn!")
            if player == 1:
                self.dino_turn(1)
            else:
                self.robo_turn(1)
            # Check for dead
            if self.herd.dinosaurs[0].health <= 0:
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
            if self.fleet.robots[0].health <= 0:
                self.fleet.robots.remove(self.fleet.robots[0])
            if len(self.herd.dinosaurs) < 1:
                winner = "Robots Win!"
                game_on = False
            if len(self.fleet.robots) < 1:
                winner = "Dinosaurs Win!"
                game_on = False
            print(computer_banner + " turn!")
            if player == 1:
                self.dino_turn(1)
            else:
                self.robo_turn(1)
        self.display_winner(winner)

    def display_welcome(self):
        choice = user_prompt("Welcome to Dinosaurs Vs Robots! Enter 1 to play as Dinosaurs and 2 to play as Robots. :", 2)
        return int(choice)

    def battle(self):
        pass

    def dino_turn(self, choice):
        self.herd.dinosaurs[choice - 1].attack(self.fleet.robots[0])

    def robo_turn(self, choice):
        self.fleet.robots[choice - 1].attack(self.herd.dinosaurs[0])

    def show_dino_opponent_options(self):
        print("What would you like to do?\n")
        i = 1
        while i <= len(self.herd.dinosaurs):
            print(f"{i}: Attack with " + self.herd.dinosaurs[i - 1].type)
        pass
        print(f"{len(self.herd.dinosaurs) + 1}: Display units")
        choice = user_prompt("", len(self.herd.dinosaurs) + 1)
        if int(choice) != len(self.herd.dinosaurs) + 1:
            return choice
        else:
            display("Robots", self.fleet, self.herd)
            display("Dinosaurs", self.fleet, self.herd)
            return self.show_robo_opponent_options()

    def show_robo_opponent_options(self):
        print("What would you like to do?\n")
        i = 1
        while i <= len(self.fleet.robots):
            print(f"{i}: Attack with " + self.fleet.robots[i - 1].name)
            i += 1
        print(f"{len(self.fleet.robots) + 1}: Display units")
        choice = user_prompt("", len(self.fleet.robots) + 1)
        if int(choice) != len(self.fleet.robots) + 1:
            return choice
        else:
            display(1, self.fleet, self.herd)
            display(2, self.fleet, self.herd)
            return self.show_robo_opponent_options()

    def display_winner(self, string):
        print(string)
