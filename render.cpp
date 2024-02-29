#include "utils.h"
#include "color.h"
#include "vec3.h"
#include "ray.h"
#include "hittable.h"
#include "hitlist.h"
#include "sphere.h"

#include <iostream>

color ray_color(const ray& r, const hittable& world) {
    hit_record rec;
    if (world.hit(r, 0, infinity, rec)) {
        return 0.5 * (rec.n_vec + color(1,1,1));
    }

    vec3 unit_direction = unit_vector(r.direction());
    auto a = 0.5*(unit_direction.y() + 1.0);
    return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0);
}

int main() {
    // image details
    auto aspect_ratio = 16.0 / 9.0;
    int image_width = 400;

    // image height must be at least 1 and must be an integer
    int image_height = static_cast<int>(image_width / aspect_ratio);
    image_height = (image_height > 1) ? image_height : 1;

    // World

    hittable_list world;

    world.add(make_shared<sphere>(vec3(-3,0,-2), 0.5));
    world.add(make_shared<sphere>(vec3(0,-100.5,-1), 100));

    // camera and viewpoint
    auto focal_length = 1.0;
    auto viewport_height = 2.0;
    auto viewport_width = viewport_height * (static_cast<double>(image_width)/image_height);
    auto camera_center = vec3(0, 0, 0);

    // +horizontal and -vertical vectors
    auto viewport_u = vec3(viewport_width, 0, 0);
    auto viewport_v = vec3(0, -viewport_height, 0);

    // deltas between pixels
    auto pixel_delta_u = viewport_u / image_width;
    auto pixel_delta_v = viewport_v / image_height;

    // upper left pixel (00)
    auto viewport_upper_left = camera_center
                             - vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2;
    auto pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v);

    // render
    std::cout << "P3\n" << image_width << ' ' << image_height << "\n255\n";

    for (int j = 0; j < image_height; ++j) {
        for (int i = 0; i < image_width; ++i) {
            auto pixel_center = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v);
            // ray_direction is not a unit vector
            auto ray_direction = pixel_center - camera_center;
            ray r(camera_center, ray_direction);

            color pixel_color = ray_color(r, world);
            write_color(std::cout, pixel_color);
        }
    }
}