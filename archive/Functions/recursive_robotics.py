class Robot:
    def __init__(self, name):
        self._name = name
        self.sub_robots = []

    def add_sub_robot(self, sub_robot):
        self.sub_robots.append(sub_robot)

    def count_robots(robot):
        """Return the total count of the robots in the heirarchy using Recursion."""
        total = 0
        for sub_robot in robot.sub_robots:
            total += count_robots(sub_robot)
        return total
