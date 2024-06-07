#ifndef SPHERE_H
#define SPHERE_H

#include "hittable.h"
#include "vec3.h"

class sphere : public hittable {
  public:
    sphere(vec3 _center, double _radius) : center(_center), radius(_radius) {}

    bool hit(const ray& r, double t_min, double t_max, hit_record& rec) const override {
        // sphere can intersect a ray in at most 2 locations using a quadratic with parameterized vector in terms of t
        vec3 dist = r.origin() - center;
        auto a = r.direction().length_squared();
        // introducint b/2 reduces computation needed
        auto bh = dot(dist, r.direction());
        auto c = dist.length_squared() - radius*radius;

        auto d = bh*bh - a*c;
        if (d < 0) return false;
        auto d_2 = sqrt(d);

        // find smallest t value that gives a hit
        auto t = (-bh - d_2) / a;
        if (t <= t_min || t_max <= t) {
            t = (-bh + d_2) / a;
            if (t <= t_min || t_max <= t)
                return false;
        }

        // if hit, sets hit_record so that it can be rendered
        rec.t = t;
        rec.pos = r.at(rec.t);
        rec.n_vec = (rec.pos - center) / radius;
        rec.set_n_vec(r, (rec.pos - center) / radius);

        return true;
    }

  private:
    vec3 center;
    double radius;
};

#endif