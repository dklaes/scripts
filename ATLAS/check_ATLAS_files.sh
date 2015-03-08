COADDVERS=V0.5.6A
MD=/vol/braid1/vol3/dklaes/ATLASCOLLAB_${COADDVERS}/

if [ ! -d ${MD} ]; then
  echo "Main directory ${MD} does not exist!"
  exit 1;
fi


while read FIELD
do
  echo ${FIELD}
  PROBLEMS=0
  PROBLEMSFITS=0


  if [ ! -d ${MD}/${FIELD} ]; then
    echo "${FIELD}: Field ${FIELD} does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi


  if [ ! -d ${MD}/${FIELD}/checkplots ]; then
    echo "${FIELD}: Checkplots directory does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/checkplots/${FIELD}.${COADDVERS}_calib.jpg ]; then
    echo "${FIELD}: Calibration checkplot does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/checkplots/${FIELD}.${COADDVERS}_coadds.jpg ]; then
    echo "${FIELD}: Coadd checkplot does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/checkplots/${FIELD}.${COADDVERS}_mag.jpg ]; then
    echo "${FIELD}: Magnitude checkplot does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/checkplots/${FIELD}.${COADDVERS}_masks.jpg ] && [ ! -f ${MD}/${FIELD}/checkplots/${FIELD}.${COADDVERS}_masks_final.jpg ]; then
    echo "${FIELD}: Masks checkplot does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi


  if [ ! -d ${MD}/${FIELD}/empty_skies_${COADDVERS} ]; then
    echo "${FIELD}: Empty skies directory does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/empty_skies_${COADDVERS}/${FIELD}_empty_skies_${COADDVERS}.tsv ]; then
    echo "${FIELD}: Empty skies tsv file does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/empty_skies_${COADDVERS}/${FIELD}_r_SDSS.${COADDVERS}_blankskies_cutouts.png ]; then
    echo "${FIELD}: Empty skies cutouts checkplot does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi
  if [ ! -f ${MD}/${FIELD}/empty_skies_${COADDVERS}/${FIELD}_r_SDSS.${COADDVERS}_blankskies_overview.png ]; then
    echo "${FIELD}: Empty skies cutout overview checkplot does not exist!"
    PROBLEMS=$(( $PROBLEMS+1 ))
  fi


  for FILTER in u_SDSS g_SDSS r_SDSS i_SDSS z_SDSS
  do
    # Check if there should be data at all:
    NUM=`grep -c ${FIELD} /vol/users/users/dklaes/git/ATLAS/OMEGACAM/summary_ATLAS_images_${FILTER}.txt`
    if [ ${NUM} -eq 0 ]; then
      continue
    fi


    if [ ! -d ${MD}/${FIELD}/${FILTER} ]; then
      echo "${FIELD}: Directory for filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS} ]; then
      echo "${FIELD}: Directory for coadds in filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/headers_${COADDVERS} ]; then
      echo "${FIELD}: Directory for headers in filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/masks_${COADDVERS} ] && [ "${FILTER}" == "r_SDSS" ]; then
      echo "${FIELD}: Directory for masks in filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS} ]; then
      echo "${FIELD}: Directory for postcoadd in filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS} ]; then
      echo "${FIELD}: Directory for precoadd in filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi


    if [ ! -f ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.fits ]; then
      echo "${FIELD}: Coadd file for filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
      PROBLEMSFITS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.flag.fits.gz ]; then
      echo "${FIELD}: Flag file for filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
      PROBLEMSFITS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.sum.fits.gz ]; then
      echo "${FIELD}: Sum file for filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
      PROBLEMSFITS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.weight.fits.gz ]; then
      echo "${FIELD}: Weight file for filter ${FILTER} does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
      PROBLEMSFITS=$(( $PROBLEMS+1 ))
    fi
    if [ ${PROBLEMSFITS} -eq 0 ]; then
      OKFITS=`fitsverify -q ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.fits | awk '{print $2}' | sed s/://`
      OKFLAG=`fitsverify -q ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.flag.fits.gz | awk '{print $2}' | sed s/://`
      OKSUM=`fitsverify -q ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.sum.fits.gz | awk '{print $2}' | sed s/://`
      OKWEIGHT=`fitsverify -q ${MD}/${FIELD}/${FILTER}/coadd_${COADDVERS}/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut.weight.fits.gz | awk '{print $2}' | sed s/://`
      if [ "${OKFITS}" != "OK" ]; then
        echo "${FIELD}: Verification for coadded image for filter ${FILTER} failed!"
        PROBLEMS=$(( $PROBLEMS+1 ))
      fi
      if [ "${OKFLAG}" != "OK" ]; then
        echo "${FIELD}: Verification for flag image for filter ${FILTER} failed!"
        PROBLEMS=$(( $PROBLEMS+1 ))
      fi
      if [ "${OKSUM}" != "OK" ]; then
        echo "${FIELD}: Verification for sum image for filter ${FILTER} failed!"
        PROBLEMS=$(( $PROBLEMS+1 ))
      fi
      if [ "${OKWEIGHT}" != "OK" ]; then
        echo "${FIELD}: Verification for weight image for filter ${FILTER} failed!"
        PROBLEMS=$(( $PROBLEMS+1 ))
      fi
    fi


    # headers directory.
    NUM=`ls ${MD}/${FIELD}/${FILTER}/headers_${COADDVERS}/ | wc -l`
    if [ ${NUM} -le 0 ]; then
      echo "${FIELD}: No header files for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi


    # masks directory.
    if [ "${FILTER}" == "r_SDSS" ]; then
      if [ ! -f ${MD}/${FIELD}/${FILTER}/masks_${COADDVERS}/${FIELD}_r_SDSS_stars.reg ] && [ ! -f ${MD}/${FIELD}/${FILTER}/masks_${COADDVERS}/${FIELD}_r_SDSS_stars_final.reg ]; then
        echo "${FIELD}: No masks files!"
        PROBLEMS=$(( $PROBLEMS+1 ))
      else
        if [ -f ${MD}/${FIELD}/${FILTER}/masks_${COADDVERS}/${FIELD}_r_SDSS_stars_final.reg ]; then
          NUM=`wc -l ${MD}/${FIELD}/${FILTER}/masks_${COADDVERS}/${FIELD}_r_SDSS_stars_final.reg | awk '{print $1}'`
        else
          NUM=`wc -l ${MD}/${FIELD}/${FILTER}/masks_${COADDVERS}/${FIELD}_r_SDSS_stars.reg | awk '{print $1}'`
        fi

        if [ ${NUM} -le 3 ]; then
          echo "${FIELD}: Mask file does not contain enough lines!"
          PROBLEMS=$(( $PROBLEMS+1 ))
        fi
      fi
    fi


    # postcoadd directory.
    if [ ! -d ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/cats ]; then
      echo "${FIELD}: Cats directory for filter ${FILTER} in postcoadd directory does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots ]; then
      echo "${FIELD}: Cats directory for filter ${FILTER} in postcoadd directory does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/cats/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut_sex_ldac.asc ]; then
      echo "${FIELD}: ASCII catalog missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/cats/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut_sex_ldac.cat ]; then
      echo "${FIELD}: LDAC catalog missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/cats/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut_sex_ldac_stars.cat ]; then
      echo "${FIELD}: LDAC stars catalog missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots/${FIELD}_${FILTER}.${COADDVERS}.swarp_astrom_scamp_2MASS.ps ]; then
      echo "${FIELD}: Astrometry checkplot missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots/${FIELD}_${FILTER}.${COADDVERS}.swarp_astrom_scamp_2MASS_stats.asc ]; then
      echo "${FIELD}: Astrometry ASCII file missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut_mag_distribution.ps ]; then
      echo "${FIELD}: Mag distribution missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots/${FIELD}_${FILTER}.${COADDVERS}.swarp.cut_magrh.ps ]; then
      echo "${FIELD}: Magrh missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots/coadd_${COADDVERS}_1.ps ]; then
      echo "${FIELD}: coadd_1 checkplot missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/postcoadd_${COADDVERS}/plots/coadd_${COADDVERS}_2.ps ]; then
      echo "${FIELD}: coadd_2 checkplot missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi


    # precoadd directory.
    if [ ! -d ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/cat ]; then
      echo "${FIELD}: Cat directory for filter ${FILTER} in precoadd directory does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/plots ]; then
      echo "${FIELD}: Cats directory for filter ${FILTER} in precoadd directory does not exist!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/cat/chips_phot.cat5 ]; then
      echo "${FIELD}: chips_phot.cat5 catalog missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -f ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/cat/${COADDVERS}.cat ]; then
      echo "${FIELD}: ${COADDVERS}.cat catalog missing for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ `ls ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/cat/OMEGA* | wc -l` -le 0 ]; then
      echo "${FIELD}: No single catalogs for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ ! -d ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/plots/PSFcheck ]; then
      echo "${FIELD}: No PSFcheck directory for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi
    if [ `ls ${MD}/${FIELD}/${FILTER}/precoadd_${COADDVERS}/plots/PSFcheck/ | wc -l` -le 0 ]; then
      echo "${FIELD}: No PSF checkplots for filter ${FILTER}!"
      PROBLEMS=$(( $PROBLEMS+1 ))
    fi

  done

  echo ${FIELD} ${PROBLEMS} >> ATLAS_problems.txt

done < ATLAS_pointings_ready.txt
