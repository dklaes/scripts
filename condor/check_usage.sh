#!/bin/bash
# -----------------------------------------------------------------------------
# File Name:           check_mmory.sh
# Author:              Dominik Klaes (dklaes@astro.uni-bonn.de)
# Last modified on:    06.06.2014
# Version:             V1.0
# Description:         This program checks the amount of memory in MB which is
#                      used by a program, given as first argument.
# -----------------------------------------------------------------------------
#
# Syntax:
#
# ./check_memory.sh "PROGRAM_CALL"
#
# where PROGRAM_CALL is the entire command to start the program, including
# arguments given to that program.
#
#
# Output:
# As output of this program, two files are created. First, a file named
#          memcheck_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt
# is created where ${PROGRAM} is the name of the launched program, ${ARGUMENTS}
# are the arguments given to that program and ${TIMESTARTLOG} the time when
# this script was started. This is given in the format
# YEAR.MONTH.DAY_HOUR:MINUTE:SECOND. If ${PROGRAM} containes slahes, e.g. when
# when you are excuting a program in another directory, everything before the
# last slash will be deleted. For each slash in ARGUMENTS, these will be
# replaced by two underscores. Each space, e.g. between several arguments, will
# be replaced by a single underscore.
#
# The second file created is named
#      memcheck_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
# and contains statistical information such as number of datapoints, mean,
# minimum and maximum.
#
#
# Example:
# Assuming a command line like
#       ./testprogram.sh variable1 variable2
# at the time 13.05.2014 12:13:45 the variables mentioned above will be:
# - PROGRAM: testprogram.sh
# - ARGUMENTS: variable1_variable2
# - TIMESTARTLOG: 2014.05.13_12:13:45
#
#
# Internal variables:
# Currently we have only one internal variable which can/should be set be the
# user:
# - DELAY: This variable sets the time in seconds the program should wait until
#          it checks for the memory consumption again. Per default it is set to
#          0, so it doesn't wait and checks as fast as possible.
#          WARNING: Please keep in mind that with this value set to 0, the  I/O
#                   is the highest possible, so the logfile can be large! With
#                   the default value, you will get about 15KB of data per
#                   logging minute.
DELAY=0


# Please do not change anything from here on unless you are absolutely sure!
TIMESTART=`date +"%Y.%m.%d %H:%M:%S"`
TIMESTARTLOG=`echo ${TIMESTART} | awk '{print $1"_"$2}'`
PROGRAM=`echo $1 | awk '{print $1}' | xargs basename`
ARGUMENTS=`echo $1 | sed 's/'${PROGRAM}'//g' | sed 's/ //' | sed 's/ /_/g' | sed 's/\//__/g'`

echo "Memory checking programm called at ${TIMESTART} with argument(s): $1"

# Get the sudo rights or all the following scripts.
sudo touch blank
if [ -e blank ]; then
  echo "Getting sudo rights completed!"
  sudo rm blank
else
  echo "Unable to get sudo rights. Exiting!"
  exit 1;
fi

# Executing the programm and saving its PID.
$1 & PID=$!

# RUN variable: 0 means program is running, 1 means program has finished.
RUN=0
DURATIONOLD=""
COVERED=""
IOPIDS=""

while [ ${RUN} -eq 0 ]
do
  TIME=`date +"%Y %m %d %H %M %S %2N %s.%2N"`
  if [ -z ${DURATIONOLD} ]; then
    DURATIONOLD=`echo ${TIME} | awk '{print $8}'`
  fi
  DURATION=`echo ${TIME} ${DURATIONOLD}| awk '{print $8-$9}'`

  # Get the PIDs of the child processes:
  CHILDS=`pstree -pA ${PID} | awk -F'(' '{print $NF}' | awk -F')' '{print $1}'`
  if [ "${PID}" == "${CHILDS}" ]; then
    ALLPIDS=`echo ${PID}`
  else
    ALLPIDS=`echo ${PID} ${CHILDS}`
  fi

  # Writing CPU and memory usage for all PIDs at once:
  ps u -p "${ALLPIDS}" --no-heading | awk -v PSAUX="$TIME $DURATION" '{print PSAUX, $2, $3, $6/1024.0}' \
       >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem.txt

  for i in ${ALLPIDS}
  do
    # Start monitoring the I/O with iostats. Currently this is the only
    # possibility I know and needs sudo rights.
    if [[ "${COVERED}" =~ "${i}" ]]; then
      echo ""
    else
      sudo iotop -kt -p ${i} -qqq > ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_${i}.txt & IOPID=$!
      COVERED=`echo ${COVERED} ${i}`
      IOPIDS=`echo ${IOPIDS} ${IOPID}`
    fi
  done

  if [ `ps u -p ${PID} | wc -l` -eq 1 ]; then
    # The program has finished. End logging.
    RUN=1
  fi

  sleep ${DELAY}
done

# The iotop processes don't seem to stop here, so we have to kill them manually.
sudo kill ${IOPIDS}

TIMESTOP=`date +"%Y.%m.%d %H:%M:%S"`
echo "Memory checking programm finished at ${TIMESTOP}."

echo ""

echo "Calculating statistics..."

awk '{print $9}' ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem.txt | sort -u > timestamps_cpu_mem_uniq.txt
while read TIME
do
  awk -v TIME=${TIME} '$9==TIME {sum1+=$11; sum2+=$12} END {print TIME, sum1, sum2}' \
       ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem.txt \
       >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem_sum.txt
done < timestamps_cpu_mem_uniq.txt

echo "CPU usage (in %):" > ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $2}' ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem_sum.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Memory usage in (MB):" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $3}' ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem_sum.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt


awk '{print $1}' ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_*.txt | sort -u > timestamps_IO_uniq.txt
while read TIME
do
  awk -v TIME=${TIME} '$1==TIME {sum1+=$5; sum2+=$7} END {print TIME, sum1/1024.0, sum2/1024.0}' \
       ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_*.txt \
       >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_sum.txt
done < timestamps_IO_uniq.txt

echo "" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Reading (in MB/s):" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $2}' ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_sum.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Writing (in MB/s):" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $3}' ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_sum.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Calculating statistics... Done!"

echo ""

echo "Starting plotting..."
gnuplot<<EOF
set term png

# CPU and memory usage
reset
set output '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem.png'
set xlabel 'Time in seconds since start'
set ylabel 'CPU usage in percent (red)'
set y2label 'Memory usage in MB (green)'
set title 'CPU and memory usage'
set ytics nomirror
set y2tics
set autoscale
plot '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem_sum.txt' u 1:2 notitle pt 7 lc 1 ps 0.5 axes x1y1, \
     '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_cpu_mem_sum.txt' u 1:3 notitle pt 7 lc 2 ps 0.5 axes x1y2

# IO
reset
set autoscale
set output '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO.png'
set xlabel 'Time in seconds since start'
set ylabel 'Read (red) / Write (green) rate in MB/s'
set title 'IO'
plot '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_sum.txt' u 2 notitle pt 7 lc 1 ps 0.5, \
     '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO_sum.txt' u 3 notitle pt 7 lc 2 ps 0.5

EOF
echo "Starting plotting... Done!"

echo ""

echo "Statistics:"
cat ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt

rm timestamps_cpu_mem_uniq.txt timestamps_IO_uniq.txt
exit 0;
