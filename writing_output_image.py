"""
Created on 25 Jan, 2024 at 12:38
    Title: writing_output_image.py - Writing Raster files from TIFF
    Description:
        -   Saving Raster TIFF file from numpy array, meta info and save path.
@author: Supantha Sen, nrsc, ISRO
"""

# Importing Modules
import rasterio

# Importing Custom Modules
...

...


def write_tif(img_data, meta, save_path):
    img = rasterio.open(save_path, 'w', **meta)

    for band in range(img_data.shape[0]):
        img.write_band(band+1, img_data[band,:,:])
