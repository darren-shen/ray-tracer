from vec3 import Vec3

class Ray:
    def __init__(self, origin: Vec3 = Vec3(), direction: Vec3 = Vec3()):
        self.origin, self.direction = origin, direction

    def get_origin(self):
        return self.origin
    
    def get_direction(self):
        return self.direction
    
    def at(self, t):
        return self.origin + t * self.direction