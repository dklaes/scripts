echo "# IMAGENAME e1 e2 V0.5.6A RZP SEEING" > stats.txt

for FIELD in `ls /vol/braid1/vol3/dklaes/ATLASCOLLAB/ --color=none | grep ATLAS_`
do
   ldactoasc -i /vol/braid1/vol3/dklaes/ATLASCOLLAB/${FIELD}/?_SDSS/precoadd_V0.5.6A/cat/V0.5.6A.cat -t STATS -s -k IMAGENAME e1 e2 V0.5.6A RZP SEEING -b >> stats.txt
done
