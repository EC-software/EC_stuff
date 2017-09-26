GDAL 2.2.0, released 2017/04/28

C:\>python
Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy, gdal
>>> img = gdal.Open("R:\DTM\SLO160\slo160.vrt")
>>> b1 = img.GetRasterBand(1)
>>> stat1 = b1.GetStatistics(False, True)
>>> print stat1
[0.0, 69.139602661133, 2.2911385373458, 3.4669918718824]
>>> a1 = b1.ReadAsArray()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\OSGEO4~1\apps\Python27\lib\site-packages\osgeo\gdal.py", line 2320, in ReadAsArray
    callback_data = callback_data)
  File "C:\OSGEO4~1\apps\Python27\lib\site-packages\osgeo\gdal_array.py", line 330, in BandReadAsArray
    buf_obj = numpy.empty([buf_ysize,buf_xsize], dtype = typecode)
MemoryError
>>>


