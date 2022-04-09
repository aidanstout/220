import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.surface_area = 0
        self.volume = 0

    def get_radius(self):
        return self.radius

    def surface_area(self):
        radius = self.radius
        self.surface_area = float(4 * math.pi * (radius ** 2))
        return self.surface_area

    def volume(self):
        radius = self.radius
        self.volume = float((4/3) * math.pi * (radius ** 3))
        return self.volume
