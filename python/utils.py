from numpy import array, dot
from numpy.random import rand, uniform

pi = 3.1415926535

class Interval:
    def __init__(self, low=-float('inf'), high=float('inf')):
        self.low, self.high = low, high

    def size(self):
        return self.high - self.low
    
    def contains(self, x):
        return self.low <= x <= self.high
    
    def surrounds(self, x):
        return self.low < x < self.high
    
    def clamp(self, x):
        if x <= self.low:
            return self.low
        elif x >= self.high:
            return self.high
        return x
    
def length_squared(v: array):
    return dot(v, v)

def degree_to_rad(degrees: int):
    return degrees * pi / 180

def random_double(low: int = 0, high: int = 1):
    return (rand() * (high - low)) + low

# np.dot, np.cross, np.random.uniform
    
def unit_vector(v: array):
    return v / v.length()

def random_unit_vector():
    while True:
        r = uniform(-1, 1, 3)
        if r.length_squared() < 1:
            return unit_vector(r)
        
def random_unit_on_hemisphere(normal):
    r = random_unit_vector()
    if dot(r, normal) > 0:
        return r
    return -r

