#!/usr/bin/env python

# ----------------------------------------------------------------------------
# File Name:           make_jpg_3masks.py
# Author:              Dominik Klaes (dklaes@astro.uni-bonn.de)
# Last modified on:    24.07.2014
# Version:             V1.0
# Description:         Creating jpg images from 3 different masks into the
#                      r-band image.
# ----------------------------------------------------------------------------

import subprocess as S
import numpy as np
import pylab as P
import sys
import os

usage = """
make_jpg_mask.py

usage: make_jpg_mask.py <field_list_file>

  field_list_file: is a text file containing a list of fields to process

  output file(s): jpg images of the overlay of images with masks

"""


#
# Specify data directories and variables
#
# Data reduction version
Ver = 'V0.5.5'
# Main directory, also known as MD in THELI
image_dir = '/vol/braid1/vol3/dklaes/ATLASCOLLAB/'
# Filter of which the masks shall be used (supposed to be at
# 'image_dir/POINTING/').
band = 'r_SDSS'
# The directory name where the coadded images are (supposed to be at
# 'image_dir/POINTING/band/').
reduction = 'coadd_%sA' % (Ver,)
# The directory name where the masks are (supposed to be at
# 'image_dir/POINTING/band/').
masks = 'masks_%sA' % (Ver,)       # ...as well as the masks
final_mask_dir = '/users/dklaes/ATLAS_masks' # where the JPG files will reside

# Create the structure if not available.
shcommand = 'mkdir -p %s' % (final_mask_dir,)
S.call(shcommand, shell=True)


# Specify the paths to programs used later.
ww = 'ww_theli'
stiff = '/users/dklaes/Downloads/stiff-2.4.0/src/stiff'

# Name area file (keeps record of the percentage of masked pixels).
# In the current used version of WeightWatcher this is not possible.
#masked_percentage_file = 'masked_percentage.txt'
#txtf = open(masked_percentage_file, 'w')
#print >> txtf, "#field, masked_percentage"

# Create blank file (only needs to be run once if there is none).
#shcommand = "ic -p 8 -c 18500 18500 '0' > blank.fits"
#print shcommand
#S.call(shcommand, shell=True)


# Check if the number of process arguments are correct.
if len(sys.argv) != 2:
    print usage
    sys.exit(2)


# Get field list from file (first argument).
try:
    field_list = filter(lambda s: not s.startswith('#'), open(sys.argv[1], 'r').readlines())
    field_list = map(lambda s: s.split()[0], field_list)
except IOError:
    print 'Cannot open field file %s, exiting!' % (sys.argv[1],)
    sys.exit(2)



# Generate the mask fits files.
for field in field_list:

    print field

    # Combine all required directory and file names.
    coadd = os.path.join(image_dir, field, band, reduction, '%s_%s.%sA.swarp.cut.fits' % \
                             (field, band, Ver))
    mask_star_reg1_f = '%s_%s_stars_13.5_11.3.reg' % (field, band,)
    mask_star_reg1 = os.path.join(image_dir, field, band, masks, mask_star_reg1_f)
    mask_star_reg2_f = '%s_%s_stars_12_10.5.reg' % (field, band,)
    mask_star_reg2 = os.path.join(image_dir, field, band, masks, mask_star_reg2_f)

    mask_original_dir = os.path.join(image_dir, field, band, masks)

    shcommand = 'sed s/POLYGON/polygon/g %s > tmp1_%s' % (mask_star_reg1, mask_star_reg1_f)
    S.call(shcommand, shell=True)  # ww doesn't like the all-cap POLYGON file
    shcommand = 'sed s/POLYGON/polygon/g %s > tmp2_%s' % (mask_star_reg2, mask_star_reg2_f)
    S.call(shcommand, shell=True)  # ww doesn't like the all-cap POLYGON file

    # Here the names of the different outfiles are defined, first the mask-only
    # FITS image, then mask + coadd FITS and as last one the output TIFF image.
    mask_fits1 = '%s/%s_mask1.fits' % (final_mask_dir, field)
    coadd_mask_fits1 = '%s/%s_coadd_mask1.fits' % (final_mask_dir, field)
    mask_fits2 = '%s/%s_mask2.fits' % (final_mask_dir, field)
    coadd_mask_fits2 = '%s/%s_coadd_mask2.fits' % (final_mask_dir, field)
    tiff = '%s/%s.tiff' % (final_mask_dir, field)

    # Set up the ww command. Because the current ww version soes not have saved
    # any internal defaults, they have to be given by the command line.
    shcommand = ww
    shcommand += ' -c default.ww'
    shcommand += ' -WEIGHT_NAMES ""' #% (weight_fits_file,)
    shcommand += ' -WEIGHT_MIN 0.5'       # only mask region where weight == 0
    shcommand += ' -WEIGHT_MAX 100000.0'  # maximum weight in RCS2 single exposures ~250
    shcommand += ' -FLAG_NAMES "blank.fits"'        # we have weight fits file instead (don't need blank.fits)
    shcommand += ' -POLY_NAMES %s' % (mask_star_reg1,)
    shcommand += ' -POLY_OUTFLAGS 1'
    shcommand += ' -VERBOSE_TYPE FULL'
    shcommand += ' -OUTFLAG_NAME %s' % (mask_fits1,)
    shcommand += ' -OUTWEIGHT_NAME ""'
    shcommand += ' -WEIGHT_OUTFLAGS 1'
    shcommand += ' -FLAG_WMASKS 0xff'
    shcommand += ' -FLAG_MASKS 0x01'
    shcommand += ' -FLAG_OUTFLAGS 2'
    print shcommand
    S.call(shcommand, shell=True)

    shcommand = ww
    shcommand += ' -c default.ww'
    shcommand += ' -WEIGHT_NAMES ""' #% (weight_fits_file,)
    shcommand += ' -WEIGHT_MIN 0.5'       # only mask region where weight == 0
    shcommand += ' -WEIGHT_MAX 100000.0'  # maximum weight in RCS2 single exposures ~250
    shcommand += ' -FLAG_NAMES "blank.fits"'        # we have weight fits file instead (don't need blank.fits)
    shcommand += ' -POLY_NAMES %s' % (mask_star_reg2,)
    shcommand += ' -POLY_OUTFLAGS 1'
    shcommand += ' -VERBOSE_TYPE FULL'
    shcommand += ' -OUTFLAG_NAME %s' % (mask_fits2,)
    shcommand += ' -OUTWEIGHT_NAME ""'
    shcommand += ' -WEIGHT_OUTFLAGS 1'
    shcommand += ' -FLAG_WMASKS 0xff'
    shcommand += ' -FLAG_MASKS 0x01'
    shcommand += ' -FLAG_OUTFLAGS 2'
    print shcommand
    S.call(shcommand, shell=True)

#    shcommand = 'rm %s' % (weight_fits_file)
#    S.Popen(shcommand, shell=True)


    # Create a combined r-band coadd with the mask image.
    # The construct with a1 = '%1' is necessary because otherwise Python
    # interprets %1 as variable that has to be filled (similar to %s).
    a1 = '%1'
    a2 = '%2'
    shcommand = "ic '%s %s +' %s %s > %s" % (a1, a2, coadd, mask_fits1, coadd_mask_fits1,)
    print shcommand
    S.call(shcommand, shell=True)
    shcommand = "ic '%s %s +' %s %s > %s" % (a1, a2, coadd, mask_fits2, coadd_mask_fits2,)
    print shcommand
    S.call(shcommand, shell=True)

    # Make the colored image.
    stiff_var = ' -BINNING 8'
    shcommand = '%s %s -OUTFILE_NAME %s %s %s %s' % (stiff, stiff_var, tiff, coadd_mask_fits1, coadd_mask_fits2, coadd_mask_fits1)
    S.call(shcommand, shell=True)

    # Convert the final TIFF image to jpg.
    jpg = '%s/%s.jpg' % (final_mask_dir, field)
    shcommand = 'convert %s %s' % (tiff, jpg)
    S.call(shcommand, shell=True)

    # Delete all not longer needed files.
    shcommand = 'rm %s/*.fits %s/*.tiff' % (final_mask_dir, final_mask_dir)
    S.call(shcommand, shell=True)

    # DEBUG
    #break
