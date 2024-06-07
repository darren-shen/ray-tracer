import numpy as np

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
        return Vec3(*(self.e + other.e))

    def __sub__(self, other):
        return Vec3(*(self.e - other.e))

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
def dot(u, v):
    return np.dot(u, v)

def cross(u, v):
    return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                u.e[2] * v.e[0] - u.e[0] * v.e[2],
                u.e[0] * v.e[1] - u.e[1] * v.e[0])

def unit_vector(v):
    return v / v.length()

