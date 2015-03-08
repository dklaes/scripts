for FILTER in u_SDSS g_SDSS r_SDSS i_SDSS z_SDSS
do
  rm mag_limit_individual_${FILTER}.txt
  rm mag_limit_${FILTER}.txt

  for POINTING in `ls -1 --color=none | grep ATLAS`
  do
    ldactoasc -i ${POINTING}/${FILTER}/precoadd_V0.5.6A/cat/V0.5.6A.cat \
              -t STATS -k V0.5.6A IMAGENAME -b -s | awk '$1==1 {print $2}' \
              > tmp_${FILTER}_$$

    while read IMAGE
    do
      ldactoasc -i ${POINTING}/${FILTER}/precoadd_V0.5.6A/cat/${IMAGE}.cat \
                -t FIELDS -k SEXBKDEV ZP EXPTIME -b \
                >> mag_limit_individual_${FILTER}.txt
    done < tmp_${FILTER}_$$

    rm tmp_${FILTER}_$$


    ldactoasc -i ${POINTING}/${FILTER}/postcoadd_V0.5.6A/cats/*.swarp.cut_sex_ldac.cat \
              -t FIELDS -k SEXBKDEV MAGZP -b \
              >> mag_limit_${FILTER}.txt
  done
done
