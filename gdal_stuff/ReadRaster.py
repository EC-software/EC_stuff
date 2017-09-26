from osgeo import gdal
from osgeo import gdalconst
from osgeo import ogr

import access_pg

# *** Open input raster and vector and turn both into relevant format
# ** open Raster data

img = gdal.Open("R:\DTM\SLO160\slo160.vrt", gdalconst.GA_ReadOnly)
b1 = img.GetRasterBand(1)

print "driver = ", img.GetDriver().LongName
print "bands = ", img.RasterCount
print "cols = ", img.RasterXSize
print "rows = ", img.RasterYSize

# get some geo-ref info
# -- for now we just know that everything is in 25832, and hope for the best...

# turn it into an appropriate data/format/type
# -- for now we just know that everything is in 25832, and hope for the best...


# ** open vector data

lst_polys = access_pg.get_recs('where jis_id = 193112')
#print "polygons:", lst_polys
for poly in lst_polys:
    #print poly
    #print str(type(poly[0]))
    #print str(type(poly[1]))
    geom = ogr.CreateGeometryFromWkb(str(poly[1]))
    print "envelope:", geom.GetEnvelope()

# Get som geo-ref info
# -- for now we just know that everything is in 25832, and hope for the best...

# turn into same projection as the raster
# -- for now we just know that everything is in 25832, and hope for the best...

# find  minX,maxX,minY,maxY


# *** Cut out a rectangle mini-raster, inside minX,maxX,minY,maxY

#scanline = b1.ReadRaster(minX, y, width, 1, width, 1, gdalconst.GDT_Int16)

# turn into appropriate PostGIS-raster data/format/type


# *** Return the data to PostGIS