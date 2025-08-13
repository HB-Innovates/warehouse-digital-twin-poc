"""
forklift_simulator.py
Simulates forklift pathing in Omniverse USD scene.
"""
from pxr import Usd
import time

class ForkliftSimulator:
    def __init__(self, stage_path):
        self.stage = Usd.Stage.Open(stage_path)
        self.forklift = self.stage.GetPrimAtPath('/Warehouse/Forklift')
        self.path = [(0,0,0), (5,0,0), (5,3,0), (0,3,0)]
        self.position = list(self.path[0])
        self.speed = 1.0
        self.path_index = 0

    def move(self, delta_time):
        # Simple path following logic
        if self.path_index < len(self.path):
            target = self.path[self.path_index]
            for i in range(3):
                if abs(self.position[i] - target[i]) > 0.01:
                    direction = 1 if self.position[i] < target[i] else -1
                    self.position[i] += direction * self.speed * delta_time
            if all(abs(self.position[i] - target[i]) < 0.1 for i in range(3)):
                self.path_index += 1
            # Update USD prim transform (mock)
            # In real Omniverse, use UsdGeom.Xform
            print(f"Forklift moved to {self.position}")

if __name__ == "__main__":
    sim = ForkliftSimulator("warehouse_usd.usda")
    for _ in range(20):
        sim.move(0.1)
        time.sleep(0.1)
