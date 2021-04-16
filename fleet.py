from robot import Robot
from weapon import Weapon
from utils import user_prompt
import random


class Fleet:
    # Constructor and Member variables
    def __init__(self):
        self.robots = []

    def create_fleet(self, team_size, player):
        robot_list = ["bot1", "bot2", "bot3", "bot4", "bot5", "bot6", "bot7", "bot8", "bot9", "bot10"]
        robots = []
        list_of_weapons = "\n\n1. Laser [10 - 20 damage]\n   Energy = 50\n2. Blaster [10 - 15 damage]\n   " \
                          "Energy = 100\n3. FlameThrower [10 - 30 damage]\n   Energy = 20\n\n\n" \
                          "Attacks consume 10 energy.\n\n"
        # Loop to create robot fleet
        i = 0
        while i < team_size:
            name = robot_list[i]
            robot = Robot(name)
            print(list_of_weapons)
            if player == 1:
                weapon_type = user_prompt(f"What is robot {i + 1}'s Weapon?\n Select by entering 1-3. :", 3)
                power_temp = 0
                if weapon_type == 1:
                    weapon_damage = random.randrange(10, 20)
                    weapon_type = "Laser"
                    power_temp = 50
                elif weapon_type == 2:
                    weapon_damage = random.randrange(10, 15)
                    weapon_type = "Blaster"
                    power_temp = 100
                elif weapon_type == 3:
                    weapon_damage = random.randrange(10, 30, 5)
                    weapon_type = "Flamethrower"
                    power_temp = 20
                robot.weapon = Weapon(weapon_type, weapon_damage)
                robot.health = random.randrange(50, 80, 10)
                robots.append(robot)
                robots[i].power_level = power_temp
            else:
                weapon_type = random.randrange(1, 3)
                if weapon_type == 1:
                    weapon_damage = random.randrange(10, 20)
                    weapon_type = "Laser"
                elif weapon_type == 2:
                    weapon_damage = random.randrange(10, 15)
                    weapon_type = "Blaster"
                elif weapon_type == 3:
                    weapon_damage = random.randrange(10, 30, 5)
                    weapon_type = "Flamethrower"
                robot.weapon = Weapon(weapon_type, weapon_damage)
                robots.append(robot)

            i += 1
        self.robots = robots
        pass
