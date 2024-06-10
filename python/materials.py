from ray import Ray
from hittable import Hit
from numpy import array, dot, zeros, ones
from utils import random_unit_vector, near_zero, unit_vector, length_squared
from math import sqrt

def reflect(v: array, n: array):
    return v - 2 * dot(v, n) * n

def refract(v: array, n: array, etai_etat):
    cos_theta = min(1, dot(-v, n))
    r_out_perp = etai_etat * (v + cos_theta * n)
    r_out_par = -sqrt(abs(1 - length_squared(r_out_perp))) * n
    return r_out_perp + r_out_par

class Material:
    def scatter(self, r_in: Ray, hit: Hit):
        # return a tuple w true/false, attenuation, scattered
        # is there a point of inclkuding true/false?
        return (False, zeros(3), zeros(3))

class Lambertian(Material):
    def __init__(self, albedo: array):
        self.albedo = albedo

    def scatter(self, r_in: Ray, hit: Hit):
        scatter_direction = hit.normal + random_unit_vector()
        if near_zero(scatter_direction):
            scatter_direction = hit.normal
        attenuation = self.albedo
        scattered = Ray(hit.point, scatter_direction)
        return (True, attenuation, scattered)

class Metal(Material):
    def __init__(self, albedo: array, fuzz = 1):
        self.albedo = albedo
        self.fuzz = fuzz if fuzz <= 1 else 1

    def scatter(self, r_in: Ray, hit: Hit):
        scatter_direction = unit_vector(reflect(r_in.direction, hit.normal)) + self.fuzz * random_unit_vector()
        attenuation = self.albedo
        scattered = Ray(hit.point, scatter_direction)
        return (True, attenuation, scattered)
    
class Dielectric(Material):
    def __init__(self, refraction):
        self.refraction = refraction

    def scatter(self, r_in: Ray, hit: Hit):
        ri = 1/self.refraction if hit.front else self.refraction
        refracted = refract(unit_vector(r_in.direction), hit.normal, ri)
        return (True, ones(3), Ray(hit.point, refracted))