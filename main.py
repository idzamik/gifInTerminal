import shutil
from PIL import Image
from PIL import ImageSequence
import time
import math
import sys

print('\n\n')

ascii_type = int(sys.argv[1])
file_name = sys.argv[2]

if file_name == '_':
    gif_name = 'gifs/' + '1' + '.gif'   # ЗДЕСЬ ПИСАТЬ НАЗВАНИЕ ФАЙЛА ВО ВТОРЫХ КОВЫЧКАХ
else:
    gif_name = 'gifs/' + file_name + '.gif'

gif_name = 'gifs/' + '1' + '.gif'

if ascii_type == 1:
    symbol_str = ' .:/|0'
elif ascii_type == 2:
    symbol_str = '0QC71]|/:. '
else:
    print('Введите верные данные!')
    sys.exit()
    

def get_pixel_to_symbol(frame, x, y):
    return symbol_str[int(math.floor(frame.getpixel((x, y)) // (255/len(symbol_str))-0.001))]


def frame_to_ascii(frame, w, h):
    frame = frame.convert('L')
    ascii_str = ''
    width, height = frame.size
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