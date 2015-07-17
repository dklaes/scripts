# I assume that all FITS files are in the subdirectory 'FITS' and the region
# files in the subdirectory 'regs'.

for IMAGE in `ls --color=none FITS/`
do
  echo ${IMAGE}
  IMAGENAME=`basename ${IMAGE} .sub.fits | awk -F"OFCS" '{print $1}'`
  ds9 -zscale FITS/${IMAGE} -regions regs/${IMAGENAME}.reg
done
