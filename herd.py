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
            i += 1
        self.dinosaurs = dinosaurs
        pass
