import numpy as np

class Object:
    """
    Class nina.Object: used to define positions in space.

    Atributes:
        - position (numpy.array): distance vector from the origin.

    Methods:
        - distanceFrom(object): claculate distance from the this to the object.
    """
    def __init__(self, position) -> None:
        self.position = np.array(position)
    def distanceFrom(self, object):
        """
        distanceFrom(object): claculate distance from the this to the object.
            - args:
                - object (nina.Object): object from which the distance will be calculated.
            - returns:
                - distance (float): returns the distance.
        """
        x1 = self.position
        x2 = object.position
        distance = np.linalg.norm(x1-x2)
        return distance