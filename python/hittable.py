from numpy import array, dot, zeros
from ray import Ray
from utils import Interval

class Hit:
    def __init__(self, point: array = zeros(3), normal: array = zeros(3), t: int = 0):
        self.point, self.normal, self.t = point, normal, t

    def set_normal(self, r: Ray, outward_normal: array):
        self.normal = outward_normal if dot(r.direction, outward_normal) < 0 else -outward_normal

class Hittable:
    def hit(self, r: Ray, ray_t: Interval, hit: Hit):
        pass