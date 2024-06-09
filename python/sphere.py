from utils import Interval
from ray import Ray
from hittable import Hit, Hittable
from numpy import array, dot
from math import sqrt

class Sphere(Hittable):
    def __init__(self, center: array, radius: array):
        self.center, self.radius = center, radius

    def hit(self, r: Ray, ray_t: Interval, hit: Hit):
        oc = self.center - r.origin
        a = r.direction.length_squared()
        h = dot(r.direction, oc)
        c = oc.length_squared() - self.radius * self.radius

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
        hit.set_normal(r, (hit.point - self.center)/self.radius)
        return True