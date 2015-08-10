for FILTER in r_SDSS i_SDSS
do
  rm mag_limit_individual_${FILTER}.txt
  rm mag_limit_${FILTER}.txt

  for POINTING in `ls -1 --color=none | grep KIDS_`
  do
    ldactoasc -i ${POINTING}/${FILTER}/precoadd_V0.5.7A/cat/V0.5.7A.cat \
              -t STATS -k V0.5.7A IMAGENAME -b -s | awk '$1==1 {print $2}' \
              > tmp_${FILTER}_$$

    while read IMAGE
    do
      ldactoasc -i ${POINTING}/${FILTER}/precoadd_V0.5.7A/cat/${IMAGE}.cat \
                -t FIELDS -k SEXBKDEV ZP EXPTIME -b \
                >> mag_limit_individual_${FILTER}.txt
    done < tmp_${FILTER}_$$

    rm tmp_${FILTER}_$$


    ldactoasc -i ${POINTING}/${FILTER}/postcoadd_V0.5.7A/cats/*.swarp.cut_sex_ldac.cat \
              -t FIELDS -k SEXBKDEV MAGZP -b \
              >> mag_limit_${FILTER}.txt



    ldactoasc -i ${POINTING}/${FILTER}/precoadd_V0.5.7A/cat/V0.5.7A.cat \
              -t STATS -k V0.5.7A SEEING -b -s | awk '$1==1 {print $2}' \
              >> seeing_individual_${FILTER}.txt

    dfits ${POINTING}/${FILTER}/coadd_V0.5.7A/${POINTING}_${FILTER}.V0.5.7A.swarp.cut.fits | \
      fitsort -d SEEING | grep -v error | awk '{print $2}' >> seeing_${FILTER}.txt
  done
done



for FILTER in u_SDSS g_SDSS z_SDSS
do
  cp mag_limit_individual_r_SDSS.txt mag_limit_individual_${FILTER}.txt
  cp mag_limit_r_SDSS.txt mag_limit_${FILTER}.txt

  cp seeing_individual_r_SDSS.txt seeing_individual_${FILTER}.txt
  cp seeing_r_SDSS.txt seeing_${FILTER}.txt
done
