from PIL import Image
import numpy as np
import fire
import sys

def color(newColor, path):
    image = Image.open(path)
    npimage = np.array(image)

    if newColor == 'red':
        npimage[:, :, (1, 2)] = 0
    else:
        print('error!')
        sys.exit(1)

    image = Image.fromarray(npimage)
    
    newImage = './image.png'
    image.save(newImage)

if __name__ == '__main__':
    fire.Fire()
