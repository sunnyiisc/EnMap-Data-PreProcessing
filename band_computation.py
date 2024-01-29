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
import datetime

# Importing Custom Modules
...

...


## Function to Convert the DN bands to Radiance Bands and return as a Numpy Array
def dn_to_rad(img_dn, meta, gain_offset_dict):

    meta.update( dtype = 'float32')

    img_rad = np.empty((img_dn.count, img_dn.shape[0], img_dn.shape[1]))
    for band_num in range(1, img_dn.count+1):
        print('Converting Band (DN to RAD):', band_num, 'of', img_dn.count, '...')

        band_dn = img_dn.read(band_num)
        gain, offset = gain_offset_dict[str(band_num)]

        ##Band Computation Keeping No-data as No-data in radiance also
        band_rad = np.where( band_dn == img_dn.nodata, img_dn.nodata, (band_dn * gain) + offset )

        ##Converting the Radiance unit as (mW/cm^2/sr/um)
        img_rad[band_num-1,:,:] = band_rad * 100.0

    print('All Bands Converted and the Radiance DataCube is of shape', img_rad.shape)
    return (img_rad, meta)


def rad_to_refl(img_rad, meta, dop, sun_ele_dict):
    meta.update(dtype='float32')

    d = d_calc(day_to_julianday(dop))

    img_refl = np.where(band_rad == 0.0, 0.0, (band_rad * np.pi * d * d) / (e0 * np.cos(np.radians(90.0 - sun_ele_band))))
    img_refl = np.empty(img_rad.shape)
    for band_num in range(1, img_rad.shape[0] + 1):
        print('Converting Band (RAD to REFL):', band_num, 'of', img_rad.shape[0], '...')

        band_rad = img_rad[band_num - 1, :, :]
        e0 = e0_valread(str(band_num))
        sun_ele_band = float(sun_ele_dict['center']) #sun_ele_band_creation(sun_ele_dict)

        ##Band Computation Keeping No-data as No-data in radiance also
        band_rad = np.where(band_rad == 0.0, 0.0, (band_rad * np.pi * d * d) / (e0 * np.cos(np.radians(90.0 - sun_ele_band))))

        ##Converting the Radiance unit as (mW/cm^2/sr/um)
        img_refl[band_num - 1, :, :] = band_rad

    print('All Bands Converted and the Reflectance DataCube is of shape', img_refl.shape)
    return (img_refl, meta)

def rad_to_refl(img_rad, meta, dop, sun_ele_dict):
    meta.update(dtype='float32')

    d = d_calc(day_to_julianday(dop))

    img_refl = np.empty(img_rad.shape)
    for band_num in range(1, img_rad.shape[0] + 1):
        print('Converting Band (RAD to REFL):', band_num, 'of', img_rad.shape[0], '...')

        band_rad = img_rad[band_num - 1, :, :]
        e0 = e0_valread(str(band_num))
        sun_ele_band = float(sun_ele_dict['center']) #sun_ele_band_creation(sun_ele_dict)

        ##Band Computation Keeping No-data as No-data in radiance also
        band_rad = np.where(band_rad == 0.0, 0.0, (band_rad * np.pi * d * d) / (e0 * np.cos(np.radians(90.0 - sun_ele_band))))

        ##Converting the Radiance unit as (mW/cm^2/sr/um)
        img_refl[band_num - 1, :, :] = band_rad

    print('All Bands Converted and the Reflectance DataCube is of shape', img_refl.shape)
    return (img_refl, meta)


def day_to_julianday(date):
    yy, mm, dd = date.split('-')

    julian_day = datetime.datetime(int(yy), int(mm), int(dd), 0, 0, 0).timetuple().tm_yday

    return(julian_day)


def d_calc(jul_day):
    file = 'EarthSunDistance.csv'

    data = np.loadtxt(file, delimiter=',', skiprows=1)
    d = {int(doy): float(dist) for doy, dist in data}

    return(d[jul_day])


def e0_valread(band):
    file = 'E0_value_enmap.csv'

    data = np.loadtxt(file, delimiter=',', skiprows=1, dtype='str')
    e0_val = {band_num: float(e0) for band_num, wavelength, e0 in data}

    return (e0_val[band])


if __name__ == '__main__':
    print('test', type( e0_valread(str(1))) )
    print('dop', day_to_julianday('2022-10-22'))