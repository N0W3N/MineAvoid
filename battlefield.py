import random


class Battlefield:
    """Create and initialize the battlefield with static coordinate - it is 10 points high and 10 points long."""

    def __init__(self):
        self.bfx = 10
        self.bfy = 10

        """Initialize the mine coordinates."""

        self.minex = 0
        self.miney = 0

    def mine(self):
        """Do randomly generate the mine coordinates."""

        self.minex = random.randint(1, 10)
        self.miney = random.randint(1, 10)