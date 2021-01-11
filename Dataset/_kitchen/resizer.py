
#           TO USE THIS SCRIPT
"""
    1- run "pip3 install Pillow"
    2- if there is no _raw/ folder, create it
    3- Copy raw images to _raw folder
    4- Run script only
    5- Take resized images from _resized folder

    This Script will resize the photos automatically
"""

from PIL import Image
import os
import argparse

def rescale_process(directory, out, size):
    
    dirs = os.listdir(directory)
    
    for img in dirs:
        im = Image.open(directory + img)
        im_resizer = im.resize(size, Image.ANTIALIAS)
        im_resizer.save(out + img)
        
    print('Process is Done')
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Rescale Images")
    args = parser.parse_args()
    rescale_process('_raw/', '_resized/', (800, 600))
