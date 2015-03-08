import subprocess
import numpy as np
import os

fATLAS = open('ATLAS_fields_filts_avail.txt')
coordsATLAS = np.array([])
coords = np.array([])

for line in fATLAS:
        test = line.split(" ")    
        RA = test[0].split("_")[1] 
        DEC = test[0].split("_")[2]
        coords = np.append(coords,[float(RA), float(DEC)])

coordsATLAS = coords.reshape((-1,2))


# Overlap CFHTLenS and ATLAS.
print("Starting CFHLenS / ATLAS overlap...")
overlap = np.array([])

for j in range(len(coordsATLAS)):
	RA = coordsATLAS[j][0]
	DEC = coordsATLAS[j][1]
	if RA > 29.5:
		if RA < 39.5:
			if DEC > -11.5:
				if DEC < -3.0:
					overlap = np.append(overlap, [coordsATLAS[j][0], coordsATLAS[j][1]])

overlap = overlap.reshape((-1,2))

# Check for runs from which no data should be taken:
for k in range(len(overlap)):
	number = 0
	RA = ((str(overlap[k][0])).replace("-", "m")).replace(".", "p")
	DEC = ((str(overlap[k][1])).replace("-", "m")).replace(".", "p")
	number = number + int(os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_u_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
	number = number + int(os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_g_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
	number = number + int(os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_r_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
	number = number + int(os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_i_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
	number = number + int(os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_z_SDSS.txt | grep -c run_11_09_f").readline().split("\n")[0])
	if number == 0:
		print("ATLAS_" + RA + "_" + DEC)
