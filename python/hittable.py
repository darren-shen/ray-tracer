from vec3 import Vec3, dot
from utils import Interval

class Hit:
    def __init__(self, point: Vec3 = Vec3(), normal: Vec3 = Vec3(), t=0):
        self.point, self.normal, self.t = point, normal, t

    def set_normal(self, r: Vec3, outward_normal: Vec3):
        self.normal = outward_normal if dot(r.direction, outward_normal) < 0 else -outward_normal

class Hittable:
    def hit(self, r, ray_t: Interval, rec):
        pass