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
      RUN=`grep ${IMAGENAME2} ${GITDIR}/ATLAS/OMEGACAM/summary_${SURVEY}_images_${FILTER}.txt | awk '{print $1}'`
      POINTING=`grep ${IMAGENAME2} ${GITDIR}/ATLAS/OMEGACAM/summary_${SURVEY}_images_${FILTER}.txt | awk '{print $3}'`
      echo ${POINTING}

      if [ -f ${GITDIR}/ATLAS/regs/${FILTER}/${RUN}/${IMAGE} ]; then
        cat regs/${IMAGE} | grep -v "#" >> ${GITDIR}/ATLAS/regs/${FILTER}/${RUN}/${IMAGE}
      else
        cat regs/${IMAGE} | grep -v "#" > ${IMAGE}.tmp
        cat header.reg ${IMAGE}.tmp > ${GITDIR}/ATLAS/regs/${FILTER}/${RUN}/${IMAGE}
      fi
    fi
  done

  echo ""
done
