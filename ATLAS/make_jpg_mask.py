#!/usr/bin/env python

# ----------------------------------------------------------------------------
# File Name:           make_jpg_mask.py
# Author:              Dominik Klaes (dklaes@astro.uni-bonn.de)
# Last modified on:    24.07.2014
# Version:             V1.0
# Description:         Creating jpg images from 3 color images plus stellar
#                      masks.
#                      This script is based upon a script from Reiko Nakajima
#                      (reiko@astro.uni-bonn.de) and Douglas Applegate
#                      (dapple@astro.uni-bonn.de).
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
#stellar_mask_dir = '/home/reiko/1project/rcslens/stellar_masks/reg'  # ... and the new stellar masks
#manual_mask_dir = '/home/reiko/1project/rcslens/manual_masks/reg'  # ... and the new manual masks
final_mask_dir = '/users/dklaes/ATLAS_masks' # where the JPG files will reside
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
    mask_star_reg_f = '%s_%s_stars.reg' % (field, band,)
    mask_star_reg = os.path.join(image_dir, field, band, masks, mask_star_reg_f)

    # Because currently we do not do any manual masking, saturated mask or
    # asteroid masks, this part is commented out.
#    manual_mask_reg_f = '%s.manualmask.reg' % (field)
#    manual_mask_reg = os.path.join(manual_mask_dir, manual_mask_reg_f)
#    if not os.path.isfile(manual_mask_reg):
#        manual_mask_reg = ''   # not all fields have manual masks

    mask_original_dir = os.path.join(image_dir, field, band, masks)
#    mask_void_reg_f = '%s_%s_voids.reg' % (field, band,)
#    mask_void_reg_orig = os.path.join(mask_original_dir, mask_void_reg_f)
#    mask_void_reg = os.path.join(final_mask_dir, mask_void_reg_f)
    shcommand = 'sed s/POLYGON/polygon/g %s > tmp_%s' % (mask_star_reg, mask_star_reg_f)
    S.call(shcommand, shell=True)  # ww doesn't like the all-cap POLYGON file
#    mask_saturated_reg_f = '%s_%s_saturated.reg' % (field, band,)
#    mask_saturated_reg = os.path.join(mask_original_dir, mask_saturated_reg_f)
#    mask_asteroids_reg_f = '%s_%s_asteroids.reg' % (field, band,)
#    mask_asteroids_reg = os.path.join(mask_original_dir, mask_asteroids_reg_f)

#    mask_reg_f = '%s_lensingcandidate_%s.reg' % (field, band,)  # we must create these files
#    mask_reg = os.path.join(final_mask_dir, mask_reg_f)
#    shcommand = 'cat %s %s %s %s %s > %s' % (mask_star_reg, manual_mask_reg, mask_void_reg,
#                                             mask_saturated_reg, mask_asteroids_reg, mask_reg)
#    S.call(shcommand, shell=True)  # created new lensingcandidate mask with better stellar masks

    # Here the names of the different outfiles are defined, first the mask-only
    # FITS image, then mask + coadd FITS and as last one the output TIFF image.
    mask_fits = '%s/%s_mask.fits' % (final_mask_dir, field)
    coadd_mask_fits = '%s/%s_coadd_mask.fits' % (final_mask_dir, field)
    tiff = '%s/%s.tiff' % (final_mask_dir, field)

    # Convert region file "boxes" into "polygons", currently not needed.
    #convert_boxes_into_polygons(mask_reg, mask_poly_reg)

    # Run Weight Watchers (ww) (weight=0 pixels will be masked)
    # Currently commented out because we are not using any weighing.
#    weight_fits_file = '%s_%s.%sA.swarp.cut.weight.fits' % (field, band, Ver)
#    weight_fits = os.path.join(image_dir, field, band, reduction, 
#                               '%s_%s.%sA.swarp.cut.weight.fits.gz' % (field, band, Ver))
#    shcommand = 'gunzip -c %s > %s' % (weight_fits, weight_fits_file)
#    if not os.path.isfile(weight_fits_file):
#        print shcommand
#        S.call(shcommand, shell=True)

    # Set up the ww command. Because the current ww version soes not have saved
    # any internal defaults, they have to be given by the command line.
    shcommand = ww
    shcommand += ' -c default.ww'
    shcommand += ' -WEIGHT_NAMES ""' #% (weight_fits_file,)
    shcommand += ' -WEIGHT_MIN 0.5'       # only mask region where weight == 0
    shcommand += ' -WEIGHT_MAX 100000.0'  # maximum weight in RCS2 single exposures ~250
    shcommand += ' -FLAG_NAMES "blank.fits"'        # we have weight fits file instead (don't need blank.fits)
    shcommand += ' -POLY_NAMES %s' % (mask_star_reg,)
    shcommand += ' -POLY_OUTFLAGS 1'
    shcommand += ' -VERBOSE_TYPE FULL'
    shcommand += ' -OUTFLAG_NAME %s' % (mask_fits,)
    shcommand += ' -OUTWEIGHT_NAME ""'
    shcommand += ' -WEIGHT_OUTFLAGS 1'
    shcommand += ' -FLAG_WMASKS 0xff'
    shcommand += ' -FLAG_MASKS 0x01'
    shcommand += ' -FLAG_OUTFLAGS 2'
#    shcommand += ' -GETAREA Y'
    print shcommand
    S.call(shcommand, shell=True)

#    shcommand = 'rm %s' % (weight_fits_file)
#    S.Popen(shcommand, shell=True)


    # Save the masked percentage value.
    # Currently disabled because GETAREA is not available in the current ww
    # version.
    #shcommand = "dfits %s | fitsort -d EFF_AREA | awk '{print $2}'" % (mask_fits)
    #percentage = S.Popen(shcommand, shell=True, stdout=S.PIPE).communicate()[0].strip()
    #print >> txtf, field, percentage

    # Create a combined r-band coadd with the mask image.
    # The construct with a1 = '%1' is necessary because otherwise Python
    # interprets %1 as variable that has to be filled (similar to %s).
    a1 = '%1'
    a2 = '%2'
    shcommand = "ic '%s %s +' %s %s > %s" % (a1, a2, coadd, mask_fits, coadd_mask_fits,)
    print shcommand
    S.call(shcommand, shell=True)

    # Make the colored image. Here we choose z_SDSS as red channel, i_SDSS as
    # green channel and r_SDSS as blue channel.
    i_band = 'i_SDSS'
    coadd_i = os.path.join(image_dir, field, i_band, reduction, '%s_%s.%sA.swarp.cut.fits' % \
                             (field, i_band, Ver))
    z_band = 'z_SDSS'
    coadd_z = os.path.join(image_dir, field, z_band, reduction, '%s_%s.%sA.swarp.cut.fits' % \
                             (field, z_band, Ver))
    stiff_var = ' -BINNING 8'
#    stiff_var += ' -GAMMA_TYPE SRGB'
#    stiff_var += ' -SKY_TYPE MANUAL'
#    stiff_var += ' -SKY_LEVEL 0.01,0.02,0.02'
#    stiff_var += ' -COLOUR_SAT 1.0'
    shcommand = '%s %s -OUTFILE_NAME %s %s %s %s' % (stiff, stiff_var, tiff, coadd_z, coadd_i, coadd_mask_fits)
    S.call(shcommand, shell=True)

    # Convert the final TIFF image to jpg.
    jpg = '%s/%s.jpg' % (final_mask_dir, field)
    shcommand = 'convert %s %s' % (tiff, jpg)
    S.call(shcommand, shell=True)

    # DEBUG
    break
