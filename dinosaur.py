class Dinosaur:
    # Constructor and Member variables
    def __init__(self, type):
        self.type = type
        self.energy = 100
        self.attack_power = 10
        self.health = 50

    def attack(self, robot, attack_type):
        damage = 0
        if self.energy == 0:
            print("Out of energy. Instead of attacking it will rest. Gain 30 energy")
            self.energy = self.energy + 30
        elif attack_type == 1:
            damage = self.attack_power * 1.5
            robot.health = robot.health - damage
            self.energy = self.energy - 20
            print(self.type + " attacked " + robot.name + " and did " + str(damage) + " damage!\n")
        elif attack_type == 2:
            robot.health = robot.health - self.attack_power
            self.energy = self.energy - 10
            print(self.type + " attacked " + robot.name + " and did " + str(self.attack_power) + " damage!\n")

