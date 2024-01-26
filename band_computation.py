"""
Created on 25 Jan, 2024 at 12:20
    Title: band_computation.py - Band Conversion Functions
    Description:
        -   Function to Convert DN band to Radiance band with the gain and offset from Mete File.
        -   Function to ...
@author: Supantha Sen, nrsc, ISRO
"""

# Importing Modules
import rasterio
import numpy as np

# Importing Custom Modules
...

...


## Function to Convert the DN bands to Radiance Bands and return as a Numpy Array
def dn_to_rad(img_path, dict):
    img = rasterio.open(img_path)
    meta = img.meta
    meta.update( dtype = 'float32')

    img_rad = np.empty((img.count, img.shape[0], img.shape[1]))
    for band_num in range(1, img.count+1):
        print('Converting Band:', band_num, 'of', img.count, '...')

        band_dn = img.read(band_num)
        gain, offset = dict[str(band_num)]
        band_rad = (band_dn * gain) + offset

        img_rad[band_num-1,:,:] = band_rad

    print('All Bands Converted and the Radiance DataCube is of shape', img_rad.shape)
    return (img_rad, meta)

