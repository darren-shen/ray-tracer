#ifndef VEC3_H
#define VEC3_H

#include <cmath>
#include <iostream>

using std::sqrt;

class vec3 {
  public:
    double e[3];

    // constructors
    vec3() : e{0,0,0} {};
    vec3(double e0, double e1, double e2) : e{e0, e1, e2} {};

    // accessors
    double x() const { return e[0]; }
    double y() const { return e[1]; }
    double z() const { return e[2]; }

    // overloading operators
    vec3 operator-() const { return vec3(-e[0], -e[1], -e[2]); }
    double operator[](int i) const { return e[i]; }
    double& operator[](int i) { return e[i]; }

    vec3& operator+=(const vec3 &v) {
        e[0] += v.e[0];
        e[1] += v.e[1];
        e[2] += v.e[2];
        return *this;
    }

    vec3& operator-=(const vec3 &v) { return *this -= v; }

    vec3& operator*=(double t) {
        e[0] *= t;
        e[1] *= t;
        e[2] *= t;
        return *this;
    }

    vec3& operator/=(double t) { return *this *= 1/t; }

    // other helper methods
    double length_squared() const { return e[0]*e[0] + e[1]*e[1] + e[2]*e[2]; }
    double length() const { return sqrt(length_squared()); }

    // for diffusion
    static vec3 random(double min, double max) { return vec3(random_double(min,max), random_double(min,max), random_double(min,max)); }
};

// vector utility functions

inline std::ostream& operator<<(std::ostream &out, const vec3 &v) { return out << v.e[0] << ' ' << v.e[1] << ' ' << v.e[2]; }
inline vec3 operator+(const vec3 &u, const vec3 &v) { return vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2]); }
inline vec3 operator-(const vec3 &u, const vec3 &v) { return vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2]); }
inline vec3 operator*(const vec3 &u, const vec3 &v) { return vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2]); }
inline vec3 operator*(double t, const vec3 &v) { return vec3(t*v.e[0], t*v.e[1], t*v.e[2]); }
inline vec3 operator*(const vec3 &v, double t) { return t * v; }
inline vec3 operator/(vec3 v, double t) { return (1/t) * v; }
inline vec3 unit_vector(vec3 v) { return v / v.length(); }
inline double dot(const vec3 &u, const vec3 &v) { return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]; }
inline vec3 cross(const vec3 &u, const vec3 &v) {
    return vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                u.e[2] * v.e[0] - u.e[0] * v.e[2],
                u.e[0] * v.e[1] - u.e[1] * v.e[0]);
}

// random unit vector via rejection sampling, potentially change to 3 normals? would be more efficient
// https://angms.science/doc/RM/randUnitVec.pdf
inline vec3 random_unit_vector() {
    while (true) {
        auto p = vec3::random(-1,1);
        if (p.length_squared() < 1)
            return unit_vector(p);
    }
}

// if  am looking for skewed distribution towards normal, can use 2 normal method w angles
// https://angms.science/doc/RM/randUnitVec.pdf
inline vec3 random_unit_vector() {
    while (true) {
        auto p = vec3::random(-1,1);
        if (p.length_squared() < 1)
            return unit_vector(p);
    }
}

// finds reflected ray, ray points in same direction as normal
inline vec3 random_on_hemisphere(const vec3& normal) {
    vec3 on_unit_sphere = random_unit_vector();
    if (dot(on_unit_sphere, normal) > 0.0) 
        return on_unit_sphere;
    else
        return -on_unit_sphere;
}

#endif