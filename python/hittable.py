from vec3 import Vec3, dot

class Hit:
    def __init__(self, point=Vec3(), vec=Vec3(), t=0):
        self.point, self.vec, self.t = point, vec, t
        self.p = Vec3()
        self.normal = Vec3()

    def set_normal(self, r, outward_normal):
        self.normal = outward_normal if dot(r.direction.e, outward_normal.e) < 0 else -outward_normal

class Hittable:
    def hit(self, r, ray_tmin, ray_tmax, rec):
        pass