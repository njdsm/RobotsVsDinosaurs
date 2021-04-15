from main import user_prompt


class Battlefield:
    # Constructor and Member variables
    def __init__(self):
        self.fleet = None
        self.herd = None

    def run_game(self):
        pass

    def display_welcome(self):
        choice = user_prompt("Welcome to Dinosaurs Vs Robots! Enter 1 to play as Dinosaurs and 2 to play as Robots", 2)
        return int(choice)
        pass

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass
