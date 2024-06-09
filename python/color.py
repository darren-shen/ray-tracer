from vec3 import Vec3
from utils import Interval
from math import sqrt

def write_color(output_file: str, color: Vec3):
    # writes a color to the output file
    intensity = Interval(0, .999)
    # apply a square root for gamma correction
    r, g, b = int(256 * intensity.clamp(max(sqrt(color.x), 0))), int(256 * intensity.clamp(max(sqrt(color.y), 0))), int(256 * intensity.clamp(max(sqrt(color.z), 0)))
    output_file.write(f'{r} {g} {b}\n')