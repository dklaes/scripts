# SD is the main directory where the processed FITS files are.
SD=/vol/braid1/vol3/kids/KIDSCOLLAB_V0.5.7A_prerelease/
VERSION=V0.5.7A
# GITDIR is the directory where we have the THELI git repository.
GITDIR=/users/dklaes/git/
SURVEY=KIDS

for IMAGE in `ls --color=none regs/`
do
  echo ${IMAGE}

  IMAGENAME=`basename ${IMAGE} .reg`
  IMAGENAME2=`echo ${IMAGENAME} | awk -F"_" '{print $1}'`

  for FILTER in r_SDSS i_SDSS
  do
    NUM=`grep -c ${IMAGENAME2} ${GITDIR}/ATLAS/OMEGACAM/summary_${SURVEY}_images_${FILTER}.txt`

    if [ ${NUM} -eq 1 ]; then
      POINTING=`grep ${IMAGENAME2} ${GITDIR}/ATLAS/OMEGACAM/summary_${SURVEY}_images_${FILTER}.txt | awk '{print $3}'`
      echo $POINTING
      cp ${SD}/${POINTING}/${FILTER}/single_${VERSION}/${IMAGENAME}OFCS*.sub.fits FITS/
    fi
  done
done
