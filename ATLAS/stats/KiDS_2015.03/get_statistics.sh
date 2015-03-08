MD=/vol/braid1/vol3/dklaes/ATLASCOLLAB/

for FILTER in u_SDSS g_SDSS r_SDSS i_SDSS z_SDSS
do
  rm mag_limit_individual_${FILTER}.txt
  rm mag_limit_${FILTER}.txt


  for POINTING in `ls -1 --color=none ${MD} | grep ATLAS_`
  do
    ldactoasc -i ${MD}/${POINTING}/${FILTER}/precoadd_V0.5.6A/cat/V0.5.6A.cat \
              -t STATS -k V0.5.6A IMAGENAME -b -s | awk '$1==1 {print $2}' \
              > tmp_${FILTER}_$$

    # Getting information for limiting magnitude.
    while read IMAGE
    do
      ldactoasc -i ${MD}/${POINTING}/${FILTER}/precoadd_V0.5.6A/cat/${IMAGE}.cat \
                -t FIELDS -k SEXBKDEV ZP EXPTIME -b \
                >> mag_limit_individual_${FILTER}.txt
    done < tmp_${FILTER}_$$


    ldactoasc -i ${MD}/${POINTING}/${FILTER}/postcoadd_V0.5.6A/cats/*.swarp.cut_sex_ldac.cat \
              -t FIELDS -k SEXBKDEV MAGZP -b \
              >> mag_limit_${FILTER}.txt


    # Getting information for sseing.
    while read IMAGE
    do
      ldactoasc -i ${MD}/${POINTING}/${FILTER}/precoadd_V0.5.6A/cat/V0.5.6A.cat \
                -t STATS -s -k IMAGENAME SEEING -b | grep ${IMAGE} | \
                awk '{print $2}' >> seeing_individual_${FILTER}.txt
    done < tmp_${FILTER}_$$

    ldactoasc -i ${MD}/${POINTING}/${FILTER}/postcoadd_V0.5.6A/cats/*.swarp.cut_sex_ldac.cat \
              -t FIELDS -k SEEING -b \
              >> seeing_${FILTER}.txt


    rm tmp_${FILTER}_$$

  done
done
