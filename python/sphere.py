from hittable import Hit, Hittable
from vec3 import Vec3, dot
from math import sqrt

class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center, self.radius = center, radius

    def hit(self, r, ray_tmin, ray_tmax, rec):
        oc = self.center - r.origin
        a = r.direction.length_squared()
        h = dot(r.direction.e, oc.e)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = h*h - a*c
        if discriminant < 0:
            return False
        
        root = (h - sqrt(discriminant)) / a
        if root <= ray_tmin or root >= ray_tmax:
            root = (h + sqrt(discriminant)) / a
            if root <= ray_tmin or root >= ray_tmax:
                return False
            
        rec.t, rec.p = root, r.at(rec.t)
        rec.set_normal(r, (rec.p - self.center)/self.radius)
        return True