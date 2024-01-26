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

# Importing Custom Modules
import browse_gui
import band_computation
import reading_xml_meta
import writing_output_image

...


def main(img_path, meta_path, save_path):
    gain_offset_dict = reading_xml_meta.read_xml(meta_path)
    img_rad, meta = band_computation.dn_to_rad(img_path, gain_offset_dict)

    writing_output_image.write_tif(img_rad, meta, save_path)
    print('Band-conversion done, output file saved as: ', save_path)


if __name__ == '__main__':
    prod_path = pathlib.Path('X:\CNEXGH~Q\S3H2YZ~F\EnMap\D62VX0~O\DIAPR7~B\EA5TAS~0.L1C\E0WEA6~M.110\EYR5OA~7')
    img_path = prod_path.joinpath('ENMAP01-____L1C-DT0000052229_20231130T060554Z_001_V010400_20231227T080229Z-SPECTRAL_IMAGE.TIF')

    meta_path = prod_path.joinpath('ENMAP01-____L1C-DT0000052229_20231130T060554Z_001_V010400_20231227T080229Z-METADATA.XML')

    save_folder = pathlib.Path('Z:\DQE\cvss\EnMap')
    save_path = save_folder.joinpath('ENMAP01-____L1C-DT0000052229_20231130T060554Z_001_V010400_20231227T080229Z-SPECTRAL_IMAGE-RADIANCE.TIF')

    main(img_path, meta_path, save_path)
