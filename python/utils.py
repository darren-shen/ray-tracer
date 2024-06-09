import numpy as np

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
    
def degree_to_rad(degrees):
    return degrees * pi / 180

def random_double(low=0, high=1):
    return (np.random.rand() * (high - low)) + low
    

