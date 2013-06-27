#!/bin/bash

for PROC in `ps aux | grep dklaes | grep illum_correction_contourplot_fitfunction.py | awk '{print $2}'`
do
  kill -9 ${PROC}
done
