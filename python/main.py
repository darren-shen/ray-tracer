from hittable_list import HittableList
from sphere import Sphere
from camera import Camera
from numpy import array

world = HittableList()
world.add(Sphere(array([0, 0, -1]), .5))
world.add(Sphere(array([0, -100.5, -1]), 100))

camera = Camera()
camera.render('test.ppm', world)