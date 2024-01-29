"""
Created on 17 Jan, 2024 at 12:18
    Title: reading_xml_meta.py - XML File Reader
    Description:
        -   Reading the XML meta file and converting the gain and offset value of each bands to a dictionary.
@author: Supantha Sen, nrsc, ISRO
"""

# Importing Modules
import xml.etree.ElementTree as et

# Importing Custom Modules
...

...


def read_xml(path):
    tree = et.parse(path)
    root = tree.getroot()

    #DOP
    dop_acq = root.find('specific').find('datatakeStart').text
    dop = dop_acq.split('T')[0]

    #Sun Elevation Angle
    dict_sun_ele = {}
    sun_ele = root.find('specific').find('sunElevationAngle')
    for ele in sun_ele:
        dict_sun_ele[ele.tag] = ele.text

    #Band Characteristics
    bnd_ch = root.find('specific').find('bandCharacterisation')

    #Writing the Gain and Offset of each band to a dictionary with key as the Band Number and a tuple of gain and offset value
    dict_gain_offset = {}
    for band in bnd_ch.findall('bandID'):
        gain = float(band.find('GainOfBand').text)
        offset = float(band.find('OffsetOfBand').text)

        dict_gain_offset[band.attrib['number']] = (gain, offset)

    return(dict_gain_offset, dop, dict_sun_ele)


if __name__ == '__main__':
    meta_path = 'Z:\DQE\cvss\EnMap\ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z\ENMAP01-____L1C-DT0000004688_20221022T094657Z_004_V010400_20231227T165538Z-METADATA.XML'
    print('Reading the file:', meta_path)
    read_xml(meta_path)