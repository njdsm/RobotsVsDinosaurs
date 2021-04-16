class Robot:
    # Constructor and Member variables
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 50
        self.weapon = None

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        self.power_level = self.power_level - 10
        print(self.name + " attacked " + dinosaur.type + " and did " + str(self.weapon.attack_power) + " damage!")
