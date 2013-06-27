#!/bin/bash

md=/vol/braid1/vol3/thomas/KIDSCOLLAB

#ls -d ${md}/*/ > names_stacks.txt

while read name
do

    ds9 -zscale ${name}r_SDSS/coadd_V0.1A/*.fits -regions load all "${name}/r_SDSS/masks_V0.1A/*.reg"


done < names_stacks.txt
