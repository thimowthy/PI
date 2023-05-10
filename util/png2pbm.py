from PIL import Image
import os
import numpy as np

path = str(__file__)
path = path.split(os.path.sep)

path = os.path.sep.join(dir for dir in path[:-2])

os.chdir(path)

files = [ f.split(".")[0] for f in os.listdir('C:/Users/55799/Desktop/PI/images') if 'png' in f ]

for f in files:
    im = Image.open(f'images/{f}.png').convert('1')
    na = np.logical_not(np.array(im))
    with open(f'images/{f}.pbm','w') as f:
        f.write(f'P1\n{im.width} {im.height}\n')
        np.savetxt(f, na, fmt='%d')
