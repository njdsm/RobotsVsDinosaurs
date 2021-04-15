from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd
from weapon import Weapon

if __name__ == '__main__':
    battlefield = Battlefield()
    fleet = Fleet()
    herd = Herd()
    team_size = int(input("How many on each team?"))
    herd.create_herd(team_size)
    fleet.create_fleet(team_size)
    for dino in herd.dinosaurs:
        print(dino)
    for robot in fleet.robots:
        print(robot)

    pass
