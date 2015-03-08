import subprocess
import numpy as np
import os

fATLAS = open('ATLAS_fields_filts_avail_griz.txt')
coordsATLAS = np.array([])
coords = np.array([])

for line in fATLAS:
        test = line.split(" ")    
        RA = test[0].split("_")[1] 
        DEC = test[0].split("_")[2]
        coords = np.append(coords,[float(RA), float(DEC)])

coordsATLAS = coords.reshape((-1,2))


# Overlap SDSS and 2dFLenS.
print("Starting 2dFLenS / ATLAS overlap...")
overlap = np.array([])

for j in range(len(coordsATLAS)):
	RA = coordsATLAS[j][0]
	DEC = coordsATLAS[j][1]
	if (RA < 53.5) or (RA > 329.0):
		if (DEC < -25.0) and (DEC > -37.0):
			overlap = np.append(overlap, [coordsATLAS[j][0], coordsATLAS[j][1]])

overlap = overlap.reshape((-1,2))

# Check for runs from which no data should be taken:
for k in range(len(overlap)):
	number = 0
	RA = ((str(overlap[k][0])).replace("-", "m")).replace(".", "p")
	DEC = ((str(overlap[k][1])).replace("-", "m")).replace(".", "p")
	print("ATLAS_" + RA + "_" + DEC)
