RELEASEDIR=/vol/braid1/vol3/dklaes/ATLASCOLLAB

while read POINTING
do
  NUM=`ls $RELEASEDIR | grep -c $POINTING`

  if [ $NUM -lt 1 ]; then
    echo "$POINTING missing!"
  fi
done < /users/dklaes/git/ATLAS/pointing_files/overlap_ATLAS_griz_KiDS-N_V0.5.7_April_2014.txt
