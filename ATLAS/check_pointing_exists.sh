while read POINTING
do
  NUM=`ls /vol/braid1/vol3/dklaes/ATLASCOLLAB/ | grep $POINTING | wc -l`
  echo $POINTING $NUM
done < ~/git/ATLAS/pointing_files/overlap_ATLAS_ugriz_CSP0320.txt
