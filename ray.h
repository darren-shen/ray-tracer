#ifndef RAY_H
#define RAY_H

#include "vec3.h"

class ray {
  public:
    // constructors
    // direction is NOT a unit vector, can be arbitrary magnitude
    ray(const vec3& origin, const vec3& direction) : orig( origin ), dir( direction ) {}

    // accessor methods
    vec3 origin() const  { return orig; }
    vec3 direction() const { return dir; }

    // helper methods
    vec3 at(double t) const { return orig + t*dir; }

  private:
    vec3 orig;
    vec3 dir;
};

#endif