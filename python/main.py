import numpy as np
from tqdm import tqdm
from vec3 import Vec3, unit_vector
from color import write_color
from ray import Ray
from hittable import Hit, Hittable
from hittable_list import HittableList
from sphere import Sphere

def ray_color(r: Ray, world):
    temp_hit = Hit()
    if world.hit(r, 0, float('inf'), temp_hit):
        return .5 * (temp_hit.normal + Vec3(1, 1, 1))
    
    a = .5 * unit_vector(r.get_direction()).y + 1
    return (1 - a) * Vec3(1, 1, 1) + a * Vec3(.5, .7, 1)

world = HittableList()
world.add(Sphere(Vec3(0, 0, -1), .5))
world.add(Sphere(Vec3(0, -100.5, -1), 100))


image_width = 400
# ratio is width/height
aspect_ratio = 16/9
image_height = max(1, int(image_width / aspect_ratio))

focal_length = 1
viewport_height = 2
viewport_width = viewport_height * (image_width/image_height)

camera_center = Vec3()

viewport_u, viewport_v = Vec3(viewport_width, 0, 0), Vec3(0, -viewport_height, 0)
u_delta, v_delta = viewport_u/image_width, viewport_v/image_height
upper_left = camera_center - Vec3(0, 0, focal_length) - (viewport_u + viewport_v)/2
upper_left_pixel = upper_left + (u_delta + v_delta)/2

# creating test image
with open('test.ppm', 'w') as f:
    f.write('P3\n')
    f.write(f"{image_width} {image_height}\n")
    f.write("255\n")

    for j in tqdm(range(image_height), desc="Generating image"):
        for i in range(image_width):
            curr_pixel = upper_left_pixel + (i * u_delta) + (j * v_delta)
            curr_ray = curr_pixel - camera_center
            write_color(f, ray_color(Ray(camera_center, curr_ray), world))