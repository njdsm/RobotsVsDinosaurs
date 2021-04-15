from dinosaur import Dinosaur


class Herd:
    # Constructor and Member variables
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, team_size):
        dinosaurs = []
        # Loop to create robot fleet
        i = 1
        while i < team_size + 1:
            dino_type = input(f"What type of dino is dino {i}?")
            dinosaur = Dinosaur(dino_type)
            dinosaurs.append(dinosaur)
            i += 1
        self.dinosaurs = dinosaurs
        pass
