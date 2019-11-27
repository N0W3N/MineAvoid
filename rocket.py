import random


class Rocket:

    def __init__(self):

        """Initialize the rockets coordinate. Each rocket has a X and Y coordinate."""

        self.x = 0
        self.y = 0

    """Functions to move the rocket one point towards up/down/right/left (marked with x and y coordinates).
        It increments or decrements the value of X or Y by one point."""

    def rocketMoveUp(self):
        self.y += 1

    def rocketMoveDown(self):
        self.y -= 1

    def rocketMoveRight(self):
        self.x += 1

    def rocketMoveLeft(self):
        self.x -= 1

    def movement(self):

        """Define a simple movement function, so the rocket can randomly move in the battlefield by itself."""

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)


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


"""myRocket = []

for x in range(1,10):
    newRocket = Rocket()
    myRocket.append(newRocket)"""

newRocket = Rocket()

battlefield = Battlefield()
battlefield.mine()

print(f"Rocket starts at {newRocket.x} (X) {newRocket.y} (Y).")
print(f"Area of Battlefield: {battlefield.bfx} (X) {battlefield.bfy} (Y)")
print(f"Mines are at: {battlefield.minex}(X) {battlefield.miney} (Y)")

while True:
    newRocket.movement()
    print(f"Rocket is now at: {newRocket.x} (X) {newRocket.y} (Y)")
    if newRocket.x == battlefield.minex and newRocket.y == battlefield.miney:
        print("Rocket has hit the mine")
        break
    else:
        print("Rocket is still flying")
