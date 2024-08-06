import shutil
import numpy as np
from PIL import Image
from PIL import ImageSequence
import time
import math

print('\n\n\n')

# print(w, h)

gif_name = 'gifs/' + '1' + '.gif'

symbol_str = ' .:/|0'
# symbol_str = '0QC71]|/:. '


def get_pixel_to_symbol(frame, x, y):
    return symbol_str[int(math.floor(frame.getpixel((x, y)) // (255/len(symbol_str))-0.001))]


def frame_to_ascii(frame, w, h):
    frame = frame.convert('L')
    # .rotate(90, expand=True)
    ascii_frame = []
    ascii_str = ''
    width, height = frame.size
    # height, width = h, w
    for y in range(height):
        for x in range(width):
            ascii_str += str(get_pixel_to_symbol(frame, x, y))
        ascii_str += '\n'
    print(ascii_str)
    time.sleep(0.1)




with Image.open(gif_name) as img:
    while True:
        for frame in ImageSequence.Iterator(img):
            w, h = shutil.get_terminal_size()
            frame = frame.resize((w, h))
            frame_to_ascii(frame, w, h)