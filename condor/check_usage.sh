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

# Executing the programm and saving its PID.
$1 & PID=$!

# RUN variable: 0 means program is running, 1 means program has finished.
RUN=0
DURATIONOLD=""

# Start monitoring the I/O with iostats. Currently this is the only possibility
# I know and needs sudo rights.
sudo iotop -kt -p ${PID} -qqq > iotop_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt & PIDIO=$!


while [ ${RUN} -eq 0 ]
do
  TIME=`date +"%Y %m %d %H %M %S %2N %s.%2N"`
  if [ -z ${DURATIONOLD} ]; then
    DURATIONOLD=`echo ${TIME} | awk '{print $8}'`
  fi
  DURATION=`echo ${TIME} | awk -v DURATIONOLD=${DURATIONOLD} '{print $8-DURATIONOLD}'`

  # Now getting the used memory from ps in MB.
  PSAUX=`ps aux | awk -v PID=${PID} '$2==PID {print $3, $6/1024.0}'`
  NUM=`ps aux | awk -v PID=${PID} '$2==PID {print $1}' | wc -l`

  if [ ${NUM} -eq 1 ]; then
    # Everything is fine, print the memory in MB into log file.
    echo "${TIME} ${DURATION} ${PSAUX}" >> cpu_mem_check_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt
  elif [ ${NUM} -eq 0 ]; then
    # The program has finished. End logging.
    RUN=1
    sudo kill ${PIDIO}
  fi

  sleep ${DELAY}
done

TIMESTOP=`date +"%Y.%m.%d %H:%M:%S"`
echo "Memory checking programm finished at ${TIMESTOP}."

echo ""

echo "Calculating statistics..."
echo "CPU usage (in %):" > ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $10}' cpu_mem_check_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Memory usage in (MB):" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $11}' cpu_mem_check_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Reading (in MB/s):" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $5/1024.0}' iotop_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt | \
    awk -f statistics.awk >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
echo "Writing (in MB/s):" >> ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt
awk '{print $7/1024.0}' iotop_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt | \
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
set yrange[0:100]
plot 'cpu_mem_check_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt' u 9:10 notitle pt 7 lc 1 ps 0.5 axes x1y1, \
     'cpu_mem_check_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt' u 9:11 notitle pt 7 lc 2 ps 0.5 axes x1y2

# IO
reset
set autoscale
set output '${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_IO.png'
set xlabel 'Time in seconds since start'
set ylabel 'Read (red) / Write (green) rate in MB/s'
set title 'IO'
plot 'iotop_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt' u (\$5/1024.0) notitle pt 7 lc 1 ps 0.5, \
     'iotop_${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}.txt' u (\$7/1024.0) notitle pt 7 lc 2 ps 0.5

EOF
echo "Starting plotting... Done!"

echo ""

echo "Statistics:"
cat ${PROGRAM}_${ARGUMENTS}_${TIMESTARTLOG}_statistics.txt

exit 0;
