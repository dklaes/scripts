# Command to generate the list of changed files (example):
# git diff --name-only New_region_files_2015_08_21 $(git merge-base New_region_files_2015_08_21 master)

SURVEY=$1
FILESCHANGED=$2
GITDIR=/vol/users/users/dklaes/git/

while read FILEPATH
do
  FILTER=`echo $FILEPATH | awk -F"/" '{print $2}'`
  FILENAME=`echo $FILEPATH | awk -F"/" '{print $4}' | awk -F"_" '{print $1}'`
  grep ${FILENAME} ${GITDIR}/ATLAS/OMEGACAM/summary_${SURVEY}_images_${FILTER}.txt | awk '{print $3}' >> pointings.tmp
done < ${FILESCHANGED}

cat pointings.tmp | sort -V | uniq > pointings_to_be_reprocessed.txt

rm pointings.tmp
