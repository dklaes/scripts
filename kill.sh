#!/bin/bash

for PROC in `ps aux | grep dklaes | grep python | grep residuals | awk '{print $2}'`
do
  kill -9 ${PROC}
done
