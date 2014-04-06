#!/bin/bash

DIR="/vol/euclid1/euclid1_raid1/dklaes/data/KIDS_V0.5/r_SDSS/"
REDDIR=`pwd`

rm ZPs_0.asc ZPs_nights.asc

for RUN in `ls -1 ${DIR}`
do
	echo $RUN
	VALUE=`gawk 'NR==2' $DIR/$RUN/STANDARD_r_SDSS/calib/night_0_r_SDSS_result.asc`
	echo $RUN $VALUE >> ZPs_0.asc

	cd $DIR/$RUN/STANDARD_r_SDSS/calib/
	for NIGHT in `ls -1 night_*.asc | grep -v night_0_r_SDSS_result.asc | gawk -F "_" '{print $2}'`
	do
		VALUE2=`gawk 'NR==2' $DIR/$RUN/STANDARD_r_SDSS/calib/night_${NIGHT}_r_SDSS_result.asc`
		echo $NIGHT $VALUE2 >> $REDDIR/ZPs_nights.asc
	done
	cd $REDDIR
done


read -p "Please change _n and _f order manually for correct time order!" x


gnuplot <<EOF
set encoding iso_8859_1
set term png
set grid
set autoscale
set xlabel 'night (GABODSID)'
set ylabel 'zeropoint in magnitude'

set yrange[20:26]
set output 'ZPs_nights.png'
plot 'ZPs_nights.asc' u 1:2 notitle

set yrange[24.5:25]
set output 'ZPs_nights_zoom.png'
plot 'ZPs_nights.asc' u 1:2 notitle

set output 'ZPs_runs.png'
set xtics rotate by -90
unset xlabel
plot 'ZPs_0.asc' u :2:xtic(1) notitle

EOF
