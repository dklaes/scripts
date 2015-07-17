DIR=$1
USERNAME=$2

for FILE in `find ${DIR} -name \*.reg`
do
  sed '/^#/d' ${FILE} | sed 's/polygon/POLYGON/g' > ${FILE}.tmp

  if [ "${USERNAME}" == "" ]; then
    cat ~/header.reg ${FILE}.tmp | sed 's/USERNAME/unknown/' > ${FILE}
  else
    cat ~/header.reg ${FILE}.tmp | sed "s/USERNAME/${USERNAME}/" > ${FILE}
  fi
  rm ${FILE}.tmp
done
