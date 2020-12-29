##############################################################
# TO USE THIS SCRIPT
#
#
#
#
##############################################################

from PIL import Image
import os
import argparse

def rescale_images(directoryIN, directoryOUT, size):
    from img in os.listdir(directoryIN):
    im = Image.open(directoryIN + img)
    im_resizer = im.resize(size, Image.ANTIALIAS)
    im_resizer.save(directoryOUT + img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale Images")
    # parser.add_argument('-d', '--directory', type=str, required=True, help='Directory that contains the images')
    # parser.add_argument('-s', '--size', type=int, nargs=2, metavar=('width', 'height'), help='Image Size to transform')
    # args = parser.parse_args()
    rescale_images('0rawimages/', '1resizedimages/', (800, 600))