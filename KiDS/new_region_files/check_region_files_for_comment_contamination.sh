for FILENAME in `find ./regs/ -name \*.reg`
do
    NUM=`grep Region ${FILENAME} | grep -cv "#"`
    if [ "${NUM}" == "1" ]; then
      echo ${FILENAME}
    fi
done
