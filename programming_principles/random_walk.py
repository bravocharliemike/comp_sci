import random

class RandomWalk:
    """Generates random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep walking until the walk reaches the desired number of steps
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far in that direction
            x_direction = random.choice([1, -1])            # left or right?
            x_distance = random.choice([0, 1, 2, 3, 4])     # how far?
            x_step = x_direction * x_distance

            y_direction = random.choice([1, -1])            # left or right?
            y_distance = random.choice([0, 1, 2, 3, 4])     # how far?
            y_step = y_direction * y_distance

            # Reject movements that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Add the x and y values to the x_values attribute
            self.x_values.append(x)
            self.y_values.append(y)
