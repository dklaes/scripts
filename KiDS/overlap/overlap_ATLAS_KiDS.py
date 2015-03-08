import numpy as np
import os

fKIDS = open('KIDS_fields_filts_avail_ugri.txt')
coordsKIDS = np.array([])
coords = np.array([])

for line in fKIDS:
	test = line.split(" ")
	RA = test[0].split("_")[1]
	DEC = test[0].split("_")[2]
	coords = np.append(coords,[float(RA), float(DEC)])

coordsKIDS = coords.reshape((-1,2))


fATLAS = open('ATLAS_fields_filts_avail_ugriz.txt')
coordsATLAS = np.array([])
coords = np.array([])

for line in fATLAS:
        test = line.split(" ")    
        RA = test[0].split("_")[1] 
        DEC = test[0].split("_")[2]
        coords = np.append(coords,[float(RA), float(DEC)])

coordsATLAS = coords.reshape((-1,2))


# Overlap KiDS and ATLAS.
print("Starting KiDS / ATLAS overlap...")
overlap = np.array([])

for i in range(len(coordsKIDS)):
	for j in range(len(coordsATLAS)):
		RAdist = np.fabs(coordsATLAS[j][0] - coordsKIDS[i][0])
		if RAdist < 1.0:
			DECdist = np.fabs(coordsATLAS[j][1] - coordsKIDS[i][1])
			if DECdist < 1.0:
				print("KIDS_" + str(coordsKIDS[i][0]) + "_" + str(coordsKIDS[i][1]) + " ATLAS_" + str(coordsATLAS[j][0]) + "_" + str(coordsATLAS[j][1]))
				overlap = np.append(overlap, [coordsKIDS[i][0], coordsKIDS[i][1], coordsATLAS[j][0], coordsATLAS[j][1]])

overlap = overlap.reshape((-1,4))

overlap_uniq = np.array([])
for k in range(len(overlap)):
	number = 0

	RAKIDS = ((str(overlap[k][0])).replace("-", "m")).replace(".", "p")
	DECKIDS = ((str(overlap[k][1])).replace("-", "m")).replace(".", "p")

        RAATLAS = ((str(overlap[k][2])).replace("-", "m")).replace(".", "p") 
        DECATLAS = ((str(overlap[k][3])).replace("-", "m")).replace(".", "p")

        number = number + int(os.popen("grep KIDS_" + RAKIDS + "_" + DECKIDS + " summary_KIDS_images_u_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep KIDS_" + RAKIDS + "_" + DECKIDS + " summary_KIDS_images_g_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep KIDS_" + RAKIDS + "_" + DECKIDS + " summary_KIDS_images_r_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep KIDS_" + RAKIDS + "_" + DECKIDS + " summary_KIDS_images_i_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])

        number = number + int(os.popen("grep ATLAS_" + RAATLAS + "_" + DECATLAS + " summary_ATLAS_images_u_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep ATLAS_" + RAATLAS + "_" + DECATLAS + " summary_ATLAS_images_g_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep ATLAS_" + RAATLAS + "_" + DECATLAS + " summary_ATLAS_images_r_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep ATLAS_" + RAATLAS + "_" + DECATLAS + " summary_ATLAS_images_i_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
        number = number + int(os.popen("grep ATLAS_" + RAATLAS + "_" + DECATLAS + " summary_ATLAS_images_z_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])

        if number == 0:	
		overlap_uniq = np.append(overlap_uniq, (RAATLAS, DECATLAS))

array_tuple = [tuple(row) for row in overlap_uniq.reshape((-1,2))]
overlap_uniq = np.unique(array_tuple)

for i in range(len(overlap_uniq)):
	print("ATLAS_" + overlap_uniq[i][0] + "_" + overlap_uniq[i][1])
