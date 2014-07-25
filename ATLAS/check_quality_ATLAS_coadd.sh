#!/bin/bash

MD=$1
SURVEY=$2
VERSION=$3

P_DFITS=/vol/euclid1/euclid1_raid1/dklaes/ATLAS/ldacpipeline//bin/Linux_64/dfits
P_IMSTATS=/vol/euclid1/euclid1_raid1/dklaes/ATLAS/ldacpipeline//bin/Linux_64/imstats
P_FITSORT=/vol/euclid1/euclid1_raid1/dklaes/ATLAS/ldacpipeline//bin/Linux_64/fitsort
P_STIFF=/users/abuddend/theli-1.6.1/bin/Linux_64/stiff

test -d plots || mkdir plots
test -d plots/coadd || mkdir plots/coadd
test -d plots/sum || mkdir plots/sum
test -d plots/weight || mkdir plots/weight
test -d plots/flag || mkdir plots/flag
test -d plots/postcoadd || mkdir plots/postcoadd



echo "FILE TEXPTIME ASTRERR MAGZP MAGZPERR SEEING SEEINERR NCOMBINE MEDIAN MEAN SIGMA MIN MAX" > stats.csv

for POINTING in `ls -1 ${MD}/ | grep ${SURVEY}_`
do
  for FILTER in u_SDSS g_SDSS r_SDSS i_SDSS z_SDSS
  do
    if [ ! -d ${MD}/${POINTING}/${FILTER} ]; then
      NUM=`grep ${POINTING}_${FILTER} known_problems.txt | wc -l | awk '{print $1}'`
      if [ ${NUM} -eq 0 ]; then
        echo ""
        echo "New problem found in ${POINTING}/${FILTER}!" >> problems.txt
        continue
      elif [ ${NUM} -eq 1 ]; then
        echo ""
        echo "Known problem found in ${POINTING}/${FILTER}. Skipping!" >> problems.txt
        continue
      else
        echo ""
        echo "Something weird is going on in ${POINTING}/${FILTER}! Perhaps more than one problem with this pointing and filter!" >> problems.txt
        continue
      fi
    else
      echo ""
      echo "Starting with ${POINTING}/${FILTER} ..."
    fi

    COADDINFO=`${P_DFITS} ${MD}/${POINTING}/${FILTER}/coadd_${VERSION}A/${POINTING}_${FILTER}.${VERSION}A.swarp.cut.fits | ${P_FITSORT} -d TEXPTIME ASTRERR MAGZP MAGZPERR SEEING SEEINERR NCOMBINE`

    IMSTATSINFO=`${P_IMSTATS} ${MD}/${POINTING}/${FILTER}/coadd_${VERSION}A/${POINTING}_${FILTER}.${VERSION}A.swarp.cut.fits | tail -n1`
    MEDIAN=`echo ${IMSTATSINFO} | awk '{print $4}'`
    MEAN=`echo ${IMSTATSINFO} | awk '{print $6}'`
    SIGMA=`echo ${IMSTATSINFO} | awk '{print $7}'`
    MIN=`echo ${IMSTATSINFO} | awk '{print $8}'`
    MAX=`echo ${IMSTATSINFO} | awk '{print $9}'`

    echo ${COADDINFO} ${MEDIAN} ${MEAN} ${SIGMA} ${MIN} ${MAX} >> stats.csv

    # Converting postcoadded checkplots
    gs -sDEVICE=png256 -sOutputFile=plots/postcoadd/${POINTING}_${FILTER}.${VERSION}A.swarp.cut_mag_distribution.png - < ${MD}/${POINTING}/${FILTER}/postcoadd/plots/${POINTING}_${FILTER}.${VERSION}A.swarp.cut_mag_distribution.ps
    gs -sDEVICE=png256 -sOutputFile=plots/postcoadd/${POINTING}_${FILTER}.${VERSION}A.swarp.cut_magrh.png - < ${MD}/${POINTING}/${FILTER}/postcoadd/plots/${POINTING}_${FILTER}.${VERSION}A.swarp.cut_magrh.ps
  done
done
