import tifffile
import cv2
import h5py
import glob
import os

# modify the filepath 
filepath = "~/202112101122_20211210_VMSC01101/region_0"
file_location = os.path.join(filepath, 'images', '*.tif')
filenames = glob.glob(file_location)

for f in filenames:
    # load image 
    image = tifffile.imread(f)
    scale_percent = 5 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # make reduced size image to avoid running out of memory 
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    print('resized image')
    tifffile.imsave(f, resized)
    print('saved image subset for single FOV section')

    # delete image to clear up memory 
    image = None 

