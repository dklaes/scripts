DIR=$1

for FILENAME in `find ${DIR}/ -name \*.reg`
do
    NUM1=`grep -v POLYGON ${FILENAME} | grep -cv "#"`
    if [ "${NUM1}" != "0" ]; then
      echo "Additional lines found: ${FILENAME}"
    fi

    NUM2=`grep -c Polygon ${FILENAME}`
    if [ "${NUM2}" != "0" ]; then
      echo "'Polygon' instead of 'POLYGON' found: ${FILENAME}"
    fi

    NUM3=`grep POLYGON ${FILENAME} | grep -c ":"`
    if [ "${NUM3}" != "0" ]; then
      echo "Sky coorfdinates found: ${FILENAME}"
    fi

    NUM4=`grep -c polygon ${FILENAME}`
    if [ "${NUM4}" != "0" ]; then
      echo "'polygon' instead of 'POLYGON' found: ${FILENAME}"
    fi

    NUM5=`sed 's/POLYGON/POLYGON\n/g' ${FILENAME} | grep -c POLYGON`
    NUM6=`grep -v "#" ${FILENAME} | grep -c POLYGON`
    if [ "${NUM5}" != "${NUM6}" ]; then
      echo "Several 'POLYGON' in one line found: ${FILENAME}"
    fi
done


find ${DIR}/ -name \*.reg | grep -v 'OMEGA.[0-9]\{4\}-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9]\+' > wrong_format.txt_$$
NUM=`wc -l wrong_format.txt_$$ | awk '{print $1}'`
if [ ${NUM} -ne 0 ]; then
  echo "Files with from filename format:"
  cat wrong_format.txt_$$
fi
rm wrong_format.txt_$$
