"""
Created on 24 Jan, 2024 at 12:14
    Title: main.py - EnMap Data preprocessing
    Description:
        -   Reading the EnMap data and Conversion of the DN band to Radiance Band
        -   Reading the Radiance Band and conversion of Radiance to Reflectance Band
@author: Supantha Sen, nrsc, ISRO
"""

# Importing Modules
import pathlib
import rasterio

# Importing Custom Modules
import browse_gui
import band_computation
import reading_xml_meta
import writing_output_image

...


def main(img_path, meta_path, save_path_rad):
    #Reading XML meta data
    gain_offset_dict, dop, sun_ele_dict = reading_xml_meta.read_xml(meta_path)

    #Reading the Raster Image
    img_dn = rasterio.open(img_path)
    meta_dn = img_dn.meta

    #Band Conversion from DN to Radiance and Reflectance
    img_rad, meta_rad = band_computation.dn_to_rad(img_dn, meta_dn, gain_offset_dict)
    img_refl, meta_refl = band_computation.rad_to_refl(img_rad, meta_rad, dop, sun_ele_dict)

    #Writing the Radiance and Reflectance Band as TIF file
    writing_output_image.write_tif(img_rad, meta_rad, save_path_rad)
    print('Band-conversion done, output Radiance file saved as: ', save_path_rad)

    writing_output_image.write_tif(img_refl, meta_refl, save_path_refl)
    print('Band-conversion done, output Reflectance file saved as: ', save_path_refl)


if __name__ == '__main__':
    prod_path = pathlib.Path('Z:\DQE\cvss\EnMap\ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z')
    img_path = prod_path.joinpath('ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z-SPECTRAL_IMAGE.TIF')

    meta_path = prod_path.joinpath('ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z-METADATA.XML')

    save_folder = pathlib.Path('Z:\DQE\cvss\EnMap')
    save_path_rad = save_folder.joinpath('ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z-SPECTRAL_IMAGE-RADIANCE.TIF')
    save_path_refl = save_folder.joinpath('ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z-SPECTRAL_IMAGE-REFLECTANCE.TIF')

    main(img_path, meta_path, save_path_rad)
