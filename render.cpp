#include "utils.h"

#include "camera.h"
#include "color.h"
#include "vec3.h"
#include "ray.h"
#include "hittable.h"
#include "hitlist.h"
#include "sphere.h"

#include <iostream>

int main() {
    hittable_list world;

    world.add(make_shared<sphere>(vec3(0,0,-1), 0.5));
    world.add(make_shared<sphere>(vec3(0,-100.5,-1), 100));

    camera cam = camera(16.0/9.0, 1200, 100, 30);

    cam.render(world);
}