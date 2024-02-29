#ifndef CAMERA_H
#define CAMERA_H

#include "utils.h"

#include "color.h"
#include "hittable.h"

#include <iostream>

class camera {
  public:
    double aspect_ratio; // = width/height
    int image_width;
    int samples;
    int max_depth; // for child rays in recursive calls to ray_color

    // initializers, default size is 200 x 200 pixels
    camera() : aspect_ratio( 1.0 ), image_width( 200 ), samples( 10 ), max_depth( 10 ) {}
    camera(const double i_aspect, const int i_width, const int i_samples, const int i_depth) : 
                    aspect_ratio( i_aspect ), image_width( i_width ), samples( i_samples ), max_depth ( i_depth ) {}
    void render(const hittable& world) {
        // rounding image height, must be > 0
        image_height = static_cast<int>(image_width / aspect_ratio);
        image_height = (image_height > 0) ? image_height : 0;

        center = vec3(0, 0, 0);

        // viewport dimensions
        auto focal_length = 1.0;
        auto viewport_height = 2.0;
        auto viewport_width = viewport_height * (static_cast<double>(image_width)/image_height);

        // horizontal and vertical viewport vectors
        auto viewport_u = vec3(viewport_width, 0, 0);
        auto viewport_v = vec3(0, -viewport_height, 0);

        // distance between pixels
        p_du = viewport_u / image_width;
        p_dv = viewport_v / image_height;

        // setting p00 = upper left corner + pixel deltas/2
        p00 = (center - vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2) + 0.5 * (p_du + p_dv);
        
        std::cout << "P3\n" << image_width << ' ' << image_height << "\n255\n";

        for (int j = 0; j < image_height; ++j) {
            for (int i = 0; i < image_width; ++i) {
                auto pixel_center = p00 + (i * p_du) + (j * p_dv);
                // ray_direction is not a unit vector
                color pixel_color(0,0,0);
                // takes several sample points and averages them for color, makes for smoother edges via anti-aliasing
                for (int sample = 0; sample < samples; ++sample) {
                    ray r = get_ray(i, j);
                    pixel_color += ray_color(r, max_depth, world);
                }
                write_color(std::cout, pixel_color, samples);
            }
        }
    }

  private:
    int image_height; // = rounded width/aspect ratio
    vec3 center; // camera center
    vec3 p00; // location of upper left pixel
    vec3 p_du;  // right offset per pixel
    vec3 p_dv; // down offset per pixel

    ray get_ray(int i, int j) const {
        // random camera ray given pixel 
        auto pixel_center = p00 + (i * p_du) + (j * p_dv);
        auto pixel_sample = pixel_center + pixel_sample_square();

        auto ray_origin = center;
        auto ray_direction = pixel_sample - ray_origin;

        return ray(ray_origin, ray_direction);
    }

    vec3 pixel_sample_square() const {
        // random point in a pixel given the center of the pixel
        auto px = -0.5 + random_double();
        auto py = -0.5 + random_double();
        return (px * p_du) + (py * p_dv);
    }

    color ray_color(const ray& r, int depth, const hittable& world) {
        // checks if ray hits anything in given world, returns appropriate color for pixel
        hit_record rec;

        // if max recursive depth is reached
        if (depth < 0) {
            return color(0, 0, 0);
        }
        // min is non-zero to get rid of "shadow acne," smoothing out rounding errors
        if (world.hit(r, 0.001, infinity, rec)) {
            // diffusion, object receives 50% of reflected ray
            return 0.5 * ray_color(ray(rec.pos, rec.n_vec + random_unit_vector()), depth-1, world);
        }

        vec3 unit_direction = unit_vector(r.direction());
        auto a = 0.5*(unit_direction.y() + 1.0);
        return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0);
    }
};

#endif