from robot import Robot
from weapon import Weapon
from main import user_prompt
import random


class Fleet:
    # Constructor and Member variables
    def __init__(self):
        self.robots = []

    def create_fleet(self, team_size):
        robots = []
        list_of_weapons = "1. Laser [4 - 12 damage]\n2. Blaster [6 - 10 damage]\n3. FlameThrower [1 - 16 damage]"
        # Loop to create robot fleet
        i = 1
        while i < team_size + 1:
            name = input(f"What is robot {i}'s Name?")
            robot = Robot(name)
            print(list_of_weapons)
            weapon_type = user_prompt(f"What is robot {i}'s Weapon?\n Select by entering 1-3", 3)
            if weapon_type == "1":
                weapon_damage = random.randrange(4, 12)
            elif weapon_type == "2":
                weapon_damage = random.randrange(6, 10)
            elif weapon_type == "3":
                weapon_damage = random.randrange(1, 15)
            robot.weapon = Weapon(weapon_type, weapon_damage)
            robots.append(robot)
            i += 1
        self.robots = robots
        pass
