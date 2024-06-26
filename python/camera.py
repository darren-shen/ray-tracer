from utils import Interval, random_double, random_unit_on_hemisphere, random_unit_vector, unit_vector
from numpy import array, dot, zeros, multiply
from color import write_color
from ray import Ray
from tqdm import tqdm
from hittable import Hit, Hittable
from hittable_list import HittableList

class Camera:
    def __init__(self):
        self.samples_per_pixel = 30
        self.max_depth = 10
        self.image_width = 400
        # ratio is width/height
        self.aspect_ratio = 16/9
        self.image_height = max(1, int(self.image_width / self.aspect_ratio))
        self.focal_length = 1
        self.viewport_height = 2
        self.viewport_width = self.viewport_height * (self.image_width/self.image_height)

        self.camera_center = zeros(3)

        self.viewport_u, self.viewport_v = array([self.viewport_width, 0, 0]), array([0, -self.viewport_height, 0])
        self.u_delta, self.v_delta = self.viewport_u/self.image_width, self.viewport_v/self.image_height
        self.upper_left = self.camera_center - array([0, 0, self.focal_length]) - (self.viewport_u + self.viewport_v)/2
        self.upper_left_pixel = self.upper_left + (self.u_delta + self.v_delta)/2
        
    def render(self, output: str, world: HittableList):
        with open(output, 'w') as f:
            f.write('P3\n')
            f.write(f"{self.image_width} {self.image_height}\n")
            f.write("255\n")

            for j in tqdm(range(self.image_height), desc="Generating image"):
                for i in range(self.image_width):
                    curr_color = zeros(3)
                    # sample multiple rays per pixel for anti-aliasing
                    for _ in range(self.samples_per_pixel):
                        curr_color += self.ray_color(self.get_ray(i, j), self.max_depth, world)
                    # write the average of all the rays to the output
                    write_color(f, curr_color/self.samples_per_pixel)


    def ray_color(self, r: Ray, depth: int, world: HittableList):
        if depth <= 0:
            return zeros(3)
        
        temp_hit = Hit()
        if world.hit(r, Interval(0.001, float('inf')), temp_hit):
            has_hit, attenuation, scattered = temp_hit.material.scatter(r, temp_hit)
            if has_hit:
                return attenuation * self.ray_color(scattered, depth - 1, world)
            return zeros(3)
        
        a = .5 * unit_vector(r.get_direction())[1] + 1
        return (1 - a) * array([1, 1, 1]) + a * array([.5, .7, 1])
    
    def get_ray(self, i: int, j: int):
        offset = self.sample_pixel()
        return Ray(self.camera_center, self.upper_left_pixel + (i + offset[0]) * self.u_delta + (j + offset[1]) * self.v_delta)

    def sample_pixel(self):
        return array([random_double() - .5, random_double() - .5, 0])
