
#           TO USE THIS SCRIPT
"""
    1- run "pip3 install Pillow"
    2- Copy raw images to _raw folder
    3- Run script only
    4- Take resized images from _resized folder
    
    This Script will resize the photos automatically
"""

from PIL import Image
import os
import argparse

def rescale_images(directory, out, size):
    
    dirs = os.listdir(directory)
    
    for img in dirs:
        im = Image.open(directory + img)
        im_resizer = im.resize(size, Image.ANTIALIAS)
        im_resizer.save(out + img)
        
    print('Image Resizing Process is Done')
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Rescale Images")
    args = parser.parse_args()
    rescale_images('_raw/', '_resized/', (800, 600))