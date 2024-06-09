import numpy as np
from utils import random_double

class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.e = np.array([x, y, z], dtype=np.float64)

    @property
    def x(self):
        return self.e[0]

    @property
    def y(self):
        return self.e[1]

    @property
    def z(self):
        return self.e[2]

    # negate, get item, set item
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    
    def __getitem__(self, i):
        return self.e[i]
    
    def __setitem__(self, i, val):
        self.e[i] = val

    # add, subtract, multiply, divide
    def __iadd__(self, v):
        self.e += v.e
        return self

    def __imul__(self, t):
        self.e *= t
        return self

    def __itruediv__(self, t):
        self.e /= t
        return self
    
    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(*(self.e + other.e))
        else:
            return Vec3(*(self.e + other))

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(*(self.e - other.e))
        else:
            return Vec3(*(self.e - other))

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(*(self.e * other.e))
        else:
            return Vec3(*(self.e * other))

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return Vec3(*(self.e / other))

    # length
    def length(self):
        return np.linalg.norm(self.e)

    def length_squared(self):
        return np.dot(self.e, self.e)

# dot, cross, unit
def dot(u: Vec3, v: Vec3):
    return np.dot(u.e, v.e)

def cross(u: Vec3, v: Vec3):
    u_e, v_e = u.e, v.e
    return Vec3(u_e[1] * v_e[2] - u_e[2] * v_e[1],
                u_e[2] * v_e[0] - u_e[0] * v_e[2],
                u_e[0] * v_e[1] - u_e[1] * v_e[0])

def unit_vector(v: Vec3):
    return v / v.length()

def random_vector(low=0, high=1):
    return Vec3(random_double(low, high), random_double(low, high), random_double(low, high))

def random_unit_vector():
    r = Vec3()
    while True:
        r = random_vector(-1, 1)
        if r.length_squared() < 1:
            return unit_vector(r)
        
def random_unit_on_hemisphere(normal):
    r = random_unit_vector()
    if dot(r, normal) > 0:
        return r
    return -r

