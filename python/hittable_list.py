from utils import Interval
from hittable import Hit, Hittable
from ray import Ray

class HittableList:
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects = []

    def add(self, obj: Hittable):
        self.objects.append(obj)

    def hit(self, r: Ray, ray_t: Interval, hit: Hit):
        has_hit = False
        closest = ray_t.high
        
        for obj in self.objects:
            if obj.hit(r, Interval(ray_t.low, closest), hit):
                has_hit = True
                closest = hit.t

        return has_hit