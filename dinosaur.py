class Dinosaur:
    # Constructor and Member variables
    def __init__(self, type):
        self.type = type
        self.energy = 100
        self.attack_power = 10
        self.health = 50

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        self.energy = self.energy - 10
