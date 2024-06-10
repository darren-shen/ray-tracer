from utils import Interval, length_squared
from ray import Ray
from hittable import Hit, Hittable
from numpy import array, dot
from math import sqrt
from materials import Material

class Sphere(Hittable):
    def __init__(self, center: array, radius: array, material: Material):
        self.center, self.radius, self.material = center, radius, material

    def hit(self, r: Ray, ray_t: Interval, hit: Hit):
        oc = self.center - r.origin
        a = length_squared(r.direction)
        h = dot(r.direction, oc)
        c = length_squared(oc) - self.radius * self.radius

        discriminant = h*h - a*c
        if discriminant < 0:
            return False
        
        root = (h - sqrt(discriminant)) / a
        if not ray_t.surrounds(root):
            root = (h + sqrt(discriminant)) / a
            if not ray_t.surrounds(root):
                return False
            
        hit.t = root
        hit.point = r.at(hit.t)
        hit.material = self.material
        hit.set_normal(r, (hit.point - self.center)/self.radius)
        return True