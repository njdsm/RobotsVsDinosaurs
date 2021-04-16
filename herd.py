from dinosaur import Dinosaur
import random


class Herd:
    # Constructor and Member variables
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, team_size):
        dinosaur_list = ["T-Rex", "Raptor", "Triceratops"]
        dinosaurs = []
        # Loop to create robot fleet
        i = 0
        while i < team_size:
            x = random.randrange(0, 2)
            dino_type = dinosaur_list[x]
            dinosaur = Dinosaur(dino_type)
            dinosaurs.append(dinosaur)
            if dino_type == "T-Rex":
                dinosaur.health = random.randrange(80, 110, 10)
                dinosaur.attack_power = random.randrange(20, 30)
            elif dino_type == "Triceratops":
                dinosaur.health = random.randrange(50, 80, 5)
                dinosaur.attack_power = random.randrange(10, 20)
                dinosaur.energy = 100
            elif dino_type == "Raptor":
                dinosaur.health = random.randrange(30, 50, 5)
                dinosaur.attack_power = random.randrange(10, 15)
                dinosaur.energy = 200
            i += 1
        self.dinosaurs = dinosaurs
        pass
