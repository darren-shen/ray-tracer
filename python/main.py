from hittable_list import HittableList
from sphere import Sphere
from camera import Camera
from numpy import array
from materials import Lambertian, Metal, Dielectric

world = HittableList()
world.add(Sphere(array([0, 0, -1.2]), .5, Lambertian(array([.1, .2, .5]))))
world.add(Sphere(array([0, -100.5, -1]), 100, Lambertian(array([.8, .8, 0]))))
world.add(Sphere(array([-1, 0, -1.2]), .5, Dielectric(1.5)))
world.add(Sphere(array([1, 0, -1.2]), .5, Metal(array([.8, .6, .2]), .1)))

camera = Camera()
camera.render('test.ppm', world)