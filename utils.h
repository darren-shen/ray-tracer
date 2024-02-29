#ifndef RTWEEKEND_H
#define RTWEEKEND_H

#include <cmath>
#include <limits>
#include <memory>

using std::shared_ptr;
using std::make_shared;
using std::sqrt;

// constants
const double infinity = std::numeric_limits<double>::infinity();
const double pi = 3.141592653589793238979323856;

// functions
inline double degrees_to_radians(double degrees) {
    return degrees * pi / 180.0;
}

#endif