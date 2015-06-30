MD=/vol/braid1/vol3/kids/KIDSCOLLAB_V0.5.7A/
DEST=/users/dklaes/

cd ${MD}
find . -type f | awk -F"/" '($3 == "r_SDSS" || $3 == "i_SDSS" || $3 == "checkplots") {print $0}' > ${DEST}/files.txt

while read FILENAME
do
  md5sum ${FILENAME} >> ${DEST}/files_and_checksums.txt
done < ${DEST}/files.txt
