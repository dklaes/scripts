DATE=20150630

for IMAGE in `ls --color=none ${DATE}/regs/`
do
  echo ${IMAGE}

  IMAGENAME=`basename ${IMAGE} .reg`
  IMAGENAME2=`echo ${IMAGENAME} | awk -F"_" '{print $1}'`

  for FILTER in r_SDSS i_SDSS
  do
    NUM=`grep -c ${IMAGENAME2} ~/git/ATLAS/OMEGACAM/summary_KIDS_images_${FILTER}.txt`

    if [ ${NUM} -eq 1 ]; then
      RUN=`grep ${IMAGENAME2} ~/git/ATLAS/OMEGACAM/summary_KIDS_images_${FILTER}.txt | awk '{print $1}'`
      POINTING=`grep ${IMAGENAME2} ~/git/ATLAS/OMEGACAM/summary_KIDS_images_${FILTER}.txt | awk '{print $3}'`
      echo ${POINTING}

      if [ -f ~/git/ATLAS/regs/${FILTER}/${RUN}/${IMAGE} ]; then
        cat ${DATE}/regs/${IMAGE} | grep -v "#" >> ~/git/ATLAS/regs/${FILTER}/${RUN}/${IMAGE}
      else
        cp ${DATE}/regs/${IMAGE} ~/git/ATLAS/regs/${FILTER}/${RUN}/
      fi
    fi
  done

  echo ""
done
