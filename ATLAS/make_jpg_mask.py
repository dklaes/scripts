#!/usr/bin/env python

import subprocess as S
import numpy as np
import pylab as P
import sys
import os

"""
make_jpg_mask.py
 

"""

usage = """
make_jpg_mask.py

usage: make_jpg_mask.py <field_list_file>

  field_list_file: is a text file containing a list of fields to process

  output file(s): jpg images of the overlay of images with masks

"""


#
# specify data directories
#
Ver = 'V0.5.5'
new_ver = '%s.manual'
image_dir = '/vol/braid1/vol3/dklaes/ATLASCOLLAB/'
band = 'r_SDSS'
reduction = 'coadd_%sA' % (Ver,)   # need the coadded image
masks = 'masks_%sA' % (Ver,)       # ...as well as the masks
#stellar_mask_dir = '/home/reiko/1project/rcslens/stellar_masks/reg'  # ... and the new stellar masks
#manual_mask_dir = '/home/reiko/1project/rcslens/manual_masks/reg'  # ... and the new manual masks
# where the JPG files will reside
final_mask_dir = '/users/dklaes/ATLAS_masks'
shcommand = 'mkdir -p %s' % (final_mask_dir,)
S.call(shcommand, shell=True)

# commands

ww = 'ww_theli'

# name area file (keeps record of the percentage of masked pixels)
#masked_percentage_file = 'masked_percentage.txt'
#txtf = open(masked_percentage_file, 'w')
#print >> txtf, "#field, masked_percentage"

# create blank file (only needs to be run once)
#shcommand = "ic -p 8 -c 18500 18500 '0' > blank.fits"

#
# process arguments
#
if len(sys.argv) != 2:
    print usage
    sys.exit(2)

#
# get field list
#
try:
    field_list = filter(lambda s: not s.startswith('#'), open(sys.argv[1], 'r').readlines())
    field_list = map(lambda s: s.split()[0], field_list)
except IOError:
    print 'Cannot open field file %s, exiting' % (sys.argv[1],)
    sys.exit(2)



#
# generate mask fits files
#
for field in field_list:

    print field

    #
    # get file names
    #
    coadd = os.path.join(image_dir, field, band, reduction, '%s_%s.%sA.swarp.cut.fits' % \
                             (field, band, Ver))
    mask_star_reg_f = '%s_%s_stars.reg' % (field, band,)
    mask_star_reg = os.path.join(image_dir, field, band, masks, mask_star_reg_f)

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

    mask_fits = '%s/%s_mask.fits' % (final_mask_dir, field)
    coadd_mask_fits = '%s/%s_coadd_mask.fits' % (final_mask_dir, field)
    tiff = '%s/%s.tiff' % (final_mask_dir, field)

    #
    # convert region file "boxes" into "polygons"
    #
    #convert_boxes_into_polygons(mask_reg, mask_poly_reg)

    #
    # run Weight Watchers (ww) (weight=0 pixels will be masked)
    #
#    weight_fits_file = '%s_%s.%sA.swarp.cut.weight.fits' % (field, band, Ver)
#    weight_fits = os.path.join(image_dir, field, band, reduction, 
#                               '%s_%s.%sA.swarp.cut.weight.fits.gz' % (field, band, Ver))
#    shcommand = 'gunzip -c %s > %s' % (weight_fits, weight_fits_file)
#    if not os.path.isfile(weight_fits_file):
#        print shcommand
#        S.call(shcommand, shell=True)

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


    #
    # save the masked percentage value
    #
    #shcommand = "dfits %s | fitsort -d EFF_AREA | awk '{print $2}'" % (mask_fits)
    #percentage = S.Popen(shcommand, shell=True, stdout=S.PIPE).communicate()[0].strip()
    #print >> txtf, field, percentage

    # Create a combined r-band coadd with the mask image.
    a1 = '%1'
    a2 = '%2'
    shcommand = "ic '%s %s +' %s %s > %s" % (a1, a2, coadd, mask_fits, coadd_mask_fits,)
    print shcommand
    S.call(shcommand, shell=True)

    #
    # make the colored image
    #
    stiff = '/users/dklaes/Downloads/stiff-2.4.0/src/stiff'
    i_band = 'i_SDSS'
    coadd_i = os.path.join(image_dir, field, i_band, reduction, '%s_%s.%sA.swarp.cut.fits' % \
                             (field, i_band, Ver))
    z_band = 'z_SDSS'
    coadd_z = os.path.join(image_dir, field, z_band, reduction, '%s_%s.%sA.swarp.cut.fits' % \
                             (field, z_band, Ver))
    stiff_var = ' -BINNING 4'
#    stiff_var += ' -GAMMA_TYPE SRGB'
#    stiff_var += ' -SKY_TYPE MANUAL'
#    stiff_var += ' -SKY_LEVEL 0.01,0.02,0.02'
#    stiff_var += ' -COLOUR_SAT 1.0'
    shcommand = '%s %s -OUTFILE_NAME %s %s %s %s' % (stiff, stiff_var, tiff, coadd_z, coadd_i, coadd_mask_fits)
    S.call(shcommand, shell=True)

    #
    # convert to jpg and place file under public_html
    #
    jpg = '%s/%s.jpg' % (final_mask_dir, field)
    shcommand = 'convert %s %s' % (tiff, jpg)
    S.call(shcommand, shell=True)

    # DEBUG
    break
