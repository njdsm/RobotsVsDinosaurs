from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd
from weapon import Weapon

def user_prompt(string, options):
    try:
        choice = int(input(string))
    except:
        print("Enter a number.")
    if options >= choice > 0:
        return choice
    else:
        result = user_prompt("Not one of your options", options)


if __name__ == '__main__':
    battlefield = Battlefield()
    fleet = Fleet()
    herd = Herd()
    player = battlefield.display_welcome()
    if player == 1:
        player = "Player One's Robots"
    else:
        player = "Player One's Dinosaurs"
    team_size = user_prompt("How many on each team? Less than 10 please.", 10)
    herd.create_herd(team_size)
    fleet.create_fleet(team_size)
    battlefield.fleet = fleet
    battlefield.herd = herd



    for dino in herd.dinosaurs:
        print(dino.type)
    for robot in fleet.robots:
        print(robot.name)
        print(robot.weapon.attack_power)


