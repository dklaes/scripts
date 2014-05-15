MD=/vol/braid1/vol3/thomas/KIDS_V0.5.5/
FILTER="u_SDSS g_SDSS r_SDSS i_SDSS z_SDSS"

for FILT in ${FILTER}
do
	for RUN in `ls -1 ${MD}/${FILT}/ | grep run_`
	do
		ZP=`awk 'NR==2 {print $1}' ${MD}/${FILT}/${RUN}/STANDARD_${FILT}/calib/night_0_${FILT}_result.asc`
		AIR=`awk 'NR==2 {print $2}' ${MD}/${FILT}/${RUN}/STANDARD_${FILT}/calib/night_0_${FILT}_result.asc`
		COL=`awk 'NR==2 {print $3}' ${MD}/${FILT}/${RUN}/STANDARD_${FILT}/calib/night_0_${FILT}_result.asc`
		echo ${RUN} ${ZP} ${AIR} ${COL} >> ZPs_${FILT}.txt

		echo ${FILT}/${RUN}
		okular ${MD}/${FILT}/${RUN}/STANDARD_${FILT}/calib/night_0_${FILT}_result.png
	done
done
