#!/opt/local/bin/python3.4
#
#  Quick and Dirty code to difference 2 frames
#
#  ARC - 10nov2022
#
import numpy as np
import matplotlib
from astropy.io import fits
import matplotlib.pyplot as plt
import sys

dataloc='../data/fnod01/'
aprefix='A/lm_221107_0'
bprefix='B/lm_221107_0'
firstA = 18000
firstB = 18500

fnum   = 2
if ( len( sys.argv ) > 1 ):
  fnum = int( sys.argv[1] )
aStrng = ('%d' % ( firstA + fnum ) )
bStrng = ('%d' % ( firstB + fnum ) )

#
#  Read in the fits data and perform the subtraction
#
with fits.open( dataloc + aprefix + aStrng + '.fits' ) as hdu:
  imData = np.array( hdu[0].data[0], dtype=float )
  imHdr  = hdu[0].header
with fits.open( dataloc + bprefix + bStrng + '.fits' ) as hdu:
  bgData = np.array( hdu[0].data[0], dtype=float )
  bgHdr  = hdu[0].header
filename = "fiz/lm_0" + aStrng + "m" + bStrng + ".fits"
fits.writeto(filename, imData-bgData, overwrite=True )
