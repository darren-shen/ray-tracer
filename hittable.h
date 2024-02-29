#ifndef HITTABLE_H
#define HITTABLE_H

#include "ray.h"

class hit_record {
  public:
    vec3 pos;
    vec3 n_vec;
    double t;
    bool front_face;

    void set_n_vec(const ray& r, const vec3& outward_normal) {
        // sets normal to always point against ray, simplies math in coloring
        // outward_normal MUST be a unit vector
        front_face = dot(r.direction(), outward_normal) < 0;
        n_vec = front_face ? outward_normal : -outward_normal;
    }
};

class hittable {
  public:
    virtual ~hittable() = default;
     // min and max t values
    virtual bool hit(const ray& r, double t_min, double t_max, hit_record& rec) const = 0;
};

#endif