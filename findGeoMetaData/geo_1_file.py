from PIL import Image
from PIL.ExifTags import TAGS

import pprint

def get_geographical_coordinates(filename):
    image = Image.open(filename)
    exif_data = image._getexif()

    if exif_data is not None:
        ifd_e_dms = exif_data[34853][4]
        num_e_ = float(ifd_e_dms)
        ifd_n_dms = exif_data[34853][2]
        num_n_ = float(ifd_n_dms)
        # datum = exif_data[34853][18]
        # date = exif_data[34853][29]

        # n_dd = lst_n_dms[0] + (lst_n_dms[1] / 60.0) + (lst_n_dms[2] / 3600.0))
        # e_dd = e_dms[0] + (e_dms[1] / 60) + (e_dms[2] / 3600)
        #
        return num_n_, num_e_


def main():
    filename = r"/home/martin/Pictures/DCIM/100ANDRO/20230815_Skjoldunge_2/snaps/DSC_0017.JPG"
    latitude, longitude = get_geographical_coordinates(filename)

    if latitude is not None and longitude is not None:
        print("Geographical Coordinates:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("No geographical coordinates found in the metadata.")

if __name__ == "__main__":
    main()
