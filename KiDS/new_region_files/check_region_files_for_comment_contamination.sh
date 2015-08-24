<<<<<<< HEAD
for FILENAME in `find ./regs/ -name \*.reg`
do
    NUM=`grep Region ${FILENAME} | grep -cv "#"`
    if [ "${NUM}" == "1" ]; then
      echo ${FILENAME}
=======
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
>>>>>>> bc2d18ee7334515469028fe4afa12d723d522d7a
    fi
done
