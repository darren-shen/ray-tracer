#ifndef COLOR_H
#define COLOR_H

#include "vec3.h"

#include <iostream>

using color = vec3;

void write_color(std::ostream &out, color pixel_color, int samples) {
    // takes SUM (not average) of all sample points and writes color
    // takes square root for gamma correction
    out << static_cast<int>(255.999 * sqrt(pixel_color.x() / samples)) << ' '
        << static_cast<int>(255.999 * sqrt(pixel_color.y() / samples)) << ' '
        << static_cast<int>(255.999 * sqrt(pixel_color.z() / samples)) << '\n';
}

#endif