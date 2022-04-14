import numpy as np

class Object:
    def __init__(self, position) -> None:
        self.position = np.array(position)
    def distanceFrom(self, object):
        x1 = self.position
        x2 = object.position
        distance = np.linalg.norm(x1-x2)
        return distance