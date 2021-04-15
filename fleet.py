from robot import Robot


class Fleet:
    # Constructor and Member variables
    def __init__(self):
        self.robots = []

    def create_fleet(self, team_size):
        robots = []
        # Loop to create robot fleet
        i = 1
        while i < team_size + 1:
            name = input(f"What is robot {i}'s Name?")
            robot = Robot(name)
            robots.append(robot)
            i += 1
        self.robots = robots
        pass
