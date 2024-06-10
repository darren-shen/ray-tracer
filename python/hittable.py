from numpy import array, dot, zeros
from ray import Ray
from utils import Interval

class Hit:
    def __init__(self, material = None, point: array = zeros(3), normal: array = zeros(3), t: int = 0):
        self.point, self.normal, self.t, self.material, self.front = point, normal, t, material, False

    def set_normal(self, r: Ray, outward_normal: array):
        self.front = dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front else -outward_normal

class Hittable:
    def hit(self, r: Ray, ray_t: Interval, hit: Hit):
        pass