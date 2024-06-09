from utils import Interval
from numpy import array 
from math import sqrt

def write_color(output_file: str, color: array):
    assert color.shape == [3], f'color has size {color.shape} instead of [3]'
    # writes a color to the output file
    intensity = Interval(0, .999)
    # apply a square root for gamma correction
    r, g, b = int(256 * intensity.clamp(sqrt(color[0]))), int(256 * intensity.clamp(sqrt(color[0]))), int(256 * intensity.clamp(sqrt(color[0])))
    output_file.write(f'{r} {g} {b}\n')