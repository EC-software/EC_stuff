import struct

from osgeo import gdal
from osgeo import gdalconst
from osgeo import ogr

import access_pg

"""

Note: (where posible)
  x,y refers to raster space (pixel count) and n,e (North,East) refers to geographical space
"""

# *** Open input raster and vector and turn both into relevant format
# ** open Raster data

#img = gdal.Open("R:\DTM\SLO160\slo160.vrt", gdalconst.GA_ReadOnly)
img = gdal.Open("R:/DTM/SLO160/10km_616_70_slo160.tif", gdalconst.GA_ReadOnly)

print "img driver:", img.GetDriver().LongName
print "img bands:", img.RasterCount
print "img cols (x-count):", img.RasterXSize
print "img rows (y-count):", img.RasterYSize

# get some geo-ref info
# -- for now we just know that everything is in 25832, and hope for the best, but we still need
geotrans = img.GetGeoTransform()
print "img geotrans: e for top left x,y                 ", geotrans[0]
tl_e = geotrans[0]
print "img geotrans: w-e pixel resolution               ", geotrans[1]
pixse = geotrans[1]
print "img geotrans: rotation, 0 if image is 'north up' ", geotrans[2]
print "img geotrans: n for top left x,y                 ", geotrans[3]
tl_n = geotrans[3]
print "img geotrans: rotation, 0 if image is 'north up' ", geotrans[4]
print "img geotrans: n-s pixel resolution               ", geotrans[5]
pixsn = -1 * geotrans[5]

# tl: Top left of image, ll: Lower left of img
##print "ll_n = {} - ({} * {})".format(tl_e, img.RasterYSize, pixsn)
ll_n = tl_n - (img.RasterYSize * pixsn) #  tl_x - (number_of_rows * cellsize_e)
ll_e = tl_e  # ll_e = tl_e :-)
##print "ll (e,n): {}, {}".format(ll_e, ll_n)
##print "Expect:   ~{}, ~{}".format(440000, 6050000)


b1 = img.GetRasterBand(1)
b1_datatype = b1.DataType
print "bnd datatype:", gdal.GetDataTypeName(b1_datatype)

# turn it into an appropriate data/format/type
# -- for now we just know that everything is in 25832, and hope for the best...


# ** open vector data

lst_polys = access_pg.get_recs('where jis_id in (193112, 1922023)') #  , 1455959
#print "polygons:", lst_polys
for poly in lst_polys:
    #print poly
    #print str(type(poly[0]))
    #print str(type(poly[1]))
    pid = poly[0]
    geom = ogr.CreateGeometryFromWkb(str(poly[1]))

    # Get som geo-ref info
    # -- for now we just know that everything is in 25832, and hope for the best...

    # turn into same projection as the raster
    # -- for now we just know that everything is in 25832, and hope for the best...

    # find  surrounding rectangle
    envelope = geom.GetEnvelope()  # http://gdal.org/python/osgeo.ogr.Geometry-class.html#GetEnvelope
    # Apparently return tuple of (env_min_e, env_max_e, env_min_n, env_max_n), 
    # eg. (589016.77, 589017.643, 6140759.048, 6140763.666)
    print "\nvec id, envelope:", pid, envelope
    env_min_e, env_max_e, env_min_n, env_max_n = envelope
    ##print "{}, {}, {}, {}".format(env_min_e, env_max_e, env_min_n, env_max_n)

    # *** Cut out a rectangle mini-raster, inside minX,maxX,minY,maxY
    # ReadRaster(self, xoff, yoff, xsize, ysize, buf_xsize = None, buf_ysize = None, buf_type = None, band_list = None )
    # The xoff, yoff, xsize, ysize parameter define the rectangle on the raster file to read.
    # The buf_xsize, buf_ysize values are the size of the resulting buffer.
    # So you might say "0,0,512,512,100,100" to read a 512x512 block at the top left of the image into a 100x100 buffer (downsampling the image).

    ##print "({} - {}) / {}".format(env_min_e, ll_e, pixse) - Works in both LL- and TL-centric unicerse...
    offs_e = int(round( (env_min_e - ll_e) / pixse ))
    ##print "({} - {}) / {}".format(env_min_n, ll_n, pixsn) - Works in a LL-centruc unicerse...
    #offs_n = int(round( (env_min_n - ll_n) / pixsn ))
    ##print "({} - {}) / {}".format(env_min_n, ll_n, pixsn) - Works in a TL-centruc unicerse...
    offs_n = int(round( (tl_n - env_max_n) / pixsn ))  # in the TL-centric univ. this is must be TL corner of envelope.

    size_e = int(round( (env_max_e - env_min_e) / pixse ))
    size_n = int(round( (env_max_n - env_min_n) / pixsn ))

    print "rasmini offsx {}, offsy {}, sizex {}, sizey {}".format(offs_e, offs_n, size_e, size_n)
    #             ReadRaster(xoff, yoff, xsize, ysize, buf_xsize=None, buf_ysize=None, buf_type=None, band_list=None)
    ras_mini = b1.ReadRaster(offs_e, offs_n, size_e, size_n, size_e, size_n, b1_datatype)
    lst_pix_val = struct.unpack('f' * (size_e * size_n), ras_mini)
    print lst_pix_val

    # ################################# get a test pix
    # size_e, size_n = (1,1)
    # offs_e, offs_n = (0,0)
    # ras_mini = b1.ReadRaster(offs_e, offs_n, size_e, size_n, size_e, size_n, b1_datatype)
    # lst_pix_val = struct.unpack('f' * (size_e * size_n), ras_mini)
    # print lst_pix_val

    # turn into appropriate PostGIS-raster data/format/type


# *** Return the data to PostGIS

print "\nExpect inside 1455959 : 0.940215; 2.1563144; 1.249801; 0.849523"