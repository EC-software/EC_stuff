from osgeo import gdal
import sys
# this allows GDAL to throw Python Exceptions
gdal.UseExceptions()

try:
    src_ds = gdal.Open( "A:\pgv_k_udsigtshoejdemodel.vrt" )
except RuntimeError, e:
    print 'Unable to open input'
    print e
    sys.exit(1)

try:
    srcband = src_ds.GetRasterBand(1)
except RuntimeError, e:
    # for example, try GetRasterBand(10)
    print 'Band ( %i ) not found' % band_num
    print e
    sys.exit(1)

print srcband