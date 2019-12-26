from rocket import *
import time

newRocket = Rocket()

Station = Station()
battlefield = Battlefield()
battlefield.mine()
newRocket.fillGasFull()

print(f"Rocket starts at {newRocket.x} (X) {newRocket.y} (Y) and has to reach the Station at {Station.x} (X) and {Station.y} (Y).")
print(f"Area of Battlefield: {battlefield.bfx} (X) {battlefield.bfy} (Y)")
print(f"Mines are at: {battlefield.minex} (X) {battlefield.miney} (Y)")

while True:
    newRocket.movement()
    print(f"Rocket is now at: {newRocket.x} (X) {newRocket.y} (Y)")
    time.sleep(2)
    if newRocket.x == battlefield.minex and newRocket.y == battlefield.miney:
        print("Rocket has hit the mine")
        break
    elif newRocket.x == Station.x and newRocket.y == Station.y:
        print("Rocket has reached the Station")
        break
    elif newRocket.tank <= 10:
        print("Gas tank has reached a critical level. Rocket is returning back to lunar base.")
        break
    else:
        print("Rocket is still flying")
        newRocket.consumption()
