POINTING=$1
MD=/vol/users/users/dklaes/git/ATLAS/OMEGACAM/

u=`grep ${POINTING} ${MD}/summary_ATLAS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq | wc -l | awk '{print $1}'`
g=`grep ${POINTING} ${MD}/summary_ATLAS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq | wc -l | awk '{print $1}'`
r=`grep ${POINTING} ${MD}/summary_ATLAS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq | wc -l | awk '{print $1}'`
i=`grep ${POINTING} ${MD}/summary_ATLAS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq | wc -l | awk '{print $1}'`
z=`grep ${POINTING} ${MD}/summary_ATLAS_images_z_SDSS.txt | awk '{print $1}' | sort | uniq | wc -l | awk '{print $1}'`

echo "u: ${u}"
echo "g: ${g}"
echo "r: ${r}"
echo "i: ${i}"
echo "z: ${z}"
