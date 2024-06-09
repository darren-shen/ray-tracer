from vec3 import Vec3
from hittable_list import HittableList
from sphere import Sphere
from camera import Camera

world = HittableList()
world.add(Sphere(Vec3(0, 0, -1), .5))
world.add(Sphere(Vec3(0, -100.5, -1), 100))

camera = Camera()
camera.render('test.ppm', world)