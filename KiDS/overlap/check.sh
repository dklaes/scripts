while read POINTING
do
  FILTERS=""

  U=`grep -c $POINTING summary_ATLAS_images_u_SDSS_V0.5.7.txt`
  if [ $U -gt 0 ]; then
    FILTERS=`echo "$FILTERS u_SDSS"`
  fi

  G=`grep -c $POINTING summary_ATLAS_images_g_SDSS_V0.5.7.txt`
  if [ $G -gt 0 ]; then
    FILTERS=`echo "$FILTERS g_SDSS"`
  fi

  R=`grep -c $POINTING summary_ATLAS_images_r_SDSS_V0.5.7.txt`
  if [ $R -gt 0 ]; then
    FILTERS=`echo "$FILTERS r_SDSS"`
  fi

  I=`grep -c $POINTING summary_ATLAS_images_i_SDSS_V0.5.7.txt`
  if [ $I -gt 0 ]; then
    FILTERS=`echo "$FILTERS i_SDSS"`
  fi

  Z=`grep -c $POINTING summary_ATLAS_images_z_SDSS_V0.5.7.txt`
  if [ $Z -gt 0 ]; then
    FILTERS=`echo "$FILTERS z_SDSS"`
  fi

  echo -e "$POINTING \t \"$FILTERS\""

done < pointings.txt
