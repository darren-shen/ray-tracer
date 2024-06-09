from numpy import array, zeros

class Ray:
    def __init__(self, origin: array = zeros(3), direction: array = zeros(3)):
        assert origin.shape == [3], f'origin has shape {origin.shape} instead of [3]'
        assert direction.shape == [3], f'direction has shape {origin.shape} instead of [3]'
        self.origin, self.direction = origin, direction

    def get_origin(self):
        return self.origin
    
    def get_direction(self):
        return self.direction
    
    def at(self, t: int):
        return self.origin + t * self.direction