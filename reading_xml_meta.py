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

    #Band Characteristics
    bnd_ch = root.find('specific').find('bandCharacterisation')

    #Writing the Gain and Offset of each band to a dictionary with key as the Band Number and a tuple of gain and offset value
    dict = {}
    for band in bnd_ch.findall('bandID'):
        gain = float(band.find('GainOfBand').text)
        offset = float(band.find('OffsetOfBand').text)

        dict[band.attrib['number']] = (gain, offset)

    return(dict)


if __name__ == '__main__':
    meta_path = 'X:\CNEXGH~Q\S3H2YZ~F\EnMap\D62VX0~O\DIAPR7~B\EA5TAS~0.L1C\E0WEA6~M.110\EYR5OA~7\EJB9VA~V.XML'
    print('Reading the file:', meta_path)
    read_xml(meta_path)