from vec3 import Vec3
import numpy as np

def write_color(output_file, color: Vec3):
    r, g, b = int(255.999 * color.x), int(255.999 * color.y), int(255.999 * color.z)
    output_file.write(f'{r} {g} {b}\n')