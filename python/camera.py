from utils import Interval, random_double
import numpy as np
from tqdm import tqdm
from vec3 import Vec3, unit_vector, random_unit_on_hemisphere, random_unit_vector
from color import write_color
from ray import Ray
from hittable import Hit, Hittable
from hittable_list import HittableList
from sphere import Sphere

class Camera:
    def __init__(self):
        self.samples_per_pixel = 10
        self.max_depth = 10
        self.image_width = 400
        # ratio is width/height
        self.aspect_ratio = 16/9
        self.image_height = max(1, int(self.image_width / self.aspect_ratio))
        self.focal_length = 1
        self.viewport_height = 2
        self.viewport_width = self.viewport_height * (self.image_width/self.image_height)

        self.camera_center = Vec3()

        self.viewport_u, self.viewport_v = Vec3(self.viewport_width, 0, 0), Vec3(0, -self.viewport_height, 0)
        self.u_delta, self.v_delta = self.viewport_u/self.image_width, self.viewport_v/self.image_height
        self.upper_left = self.camera_center - Vec3(0, 0, self.focal_length) - (self.viewport_u + self.viewport_v)/2
        self.upper_left_pixel = self.upper_left + (self.u_delta + self.v_delta)/2
        
    def render(self, output, world):
        with open(output, 'w') as f:
            f.write('P3\n')
            f.write(f"{self.image_width} {self.image_height}\n")
            f.write("255\n")

            for j in tqdm(range(self.image_height), desc="Generating image"):
                for i in range(self.image_width):
                    curr_color = Vec3()
                    # sample multiple rays per pixel for anti-aliasing
                    for _ in range(self.samples_per_pixel):
                        curr_color += self.ray_color(self.get_ray(i, j), self.max_depth, world)
                    # write the average of all the rays to the output
                    write_color(f, curr_color/self.samples_per_pixel)


    def ray_color(self, r: Ray, depth, world):
        if depth <= 0:
            return Vec3()
        
        temp_hit = Hit()
        if world.hit(r, Interval(0.001, float('inf')), temp_hit):
            return .5 * self.ray_color(Ray(temp_hit.point, temp_hit.normal + random_unit_vector()), depth - 1, world)
        
        a = .5 * unit_vector(r.get_direction()).y + 1
        return (1 - a) * Vec3(1, 1, 1) + a * Vec3(.5, .7, 1)
    
    def get_ray(self, i, j):
        offset = self.sample_pixel()
        return Ray(self.camera_center, self.upper_left_pixel + (i + offset.x) * self.u_delta + (j + offset.y) * self.v_delta)

    def sample_pixel(self):
        return Vec3(random_double() - .5, random_double() - .5, 0)
