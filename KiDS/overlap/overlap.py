import numpy as np
import os

fKIDS = open('KIDS_fields_filts_avail_all_colours.txt')
coordsKIDS = np.array([])
coords = np.array([])

for line in fKIDS:
	test = line.split(" ")
	RA = test[0].split("_")[1]
	DEC = test[0].split("_")[2]
	coords = np.append(coords,[float(RA), float(DEC)])

coordsKIDS = coords.reshape((-1,2))


fATLAS = open('ATLAS_fields_filts_avail_all_colours.txt')
coordsATLAS = np.array([])
coords = np.array([])

for line in fATLAS:
        test = line.split(" ")    
        RA = test[0].split("_")[1] 
        DEC = test[0].split("_")[2]
        coords = np.append(coords,[float(RA), float(DEC)])

coordsATLAS = coords.reshape((-1,2))

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

os.popen("rm runs_KIDS_?_tmp.txt")
for k in range(len(overlap)):
	RA = ((str(overlap[k][0])).replace("-", "m")).replace("+", "p")
	DEC = ((str(overlap[k][1])).replace("-", "m")).replace("+", "p")
	os.popen("grep KIDS_" + RA + "_" + DEC + " KIDS_summary_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_u_tmp.txt")
	os.popen("grep KIDS_" + RA + "_" + DEC + " KIDS_summary_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_g_tmp.txt")
	os.popen("grep KIDS_" + RA + "_" + DEC + " KIDS_summary_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_i_tmp.txt")
	os.popen("grep KIDS_" + RA + "_" + DEC + " KIDS_summary_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_r_tmp.txt")

os.popen("cat runs_KIDS_u_tmp.txt | sort | uniq > runs_KIDS_u.txt")
os.popen("cat runs_KIDS_g_tmp.txt | sort | uniq > runs_KIDS_g.txt")
os.popen("cat runs_KIDS_i_tmp.txt | sort | uniq > runs_KIDS_i.txt")
os.popen("cat runs_KIDS_r_tmp.txt | sort | uniq > runs_KIDS_r.txt")
os.popen("cat runs_KIDS_?.txt | sort | uniq > runs_KIDS_total.txt")

os.popen("rm runs_KIDS_?_tmp.txt")


#os.popen("rm runs_ATLAS_?_tmp.txt")
#for k in range(len(overlap)):
#        RA = ((str(overlap[k][2])).replace("-", "m")).replace("+", "p") 
#        DEC = ((str(overlap[k][3])).replace("-", "m")).replace("+", "p")
#        os.popen("grep ATLAS_" + RA + "_" + DEC + " ATLAS_summary_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_u_tmp.txt")
#        os.popen("grep ATLAS_" + RA + "_" + DEC + " ATLAS_summary_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_g_tmp.txt")
#        os.popen("grep ATLAS_" + RA + "_" + DEC + " ATLAS_summary_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_i_tmp.txt")
#        os.popen("grep ATLAS_" + RA + "_" + DEC + " ATLAS_summary_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_r_tmp.txt")
#
#os.popen("cat runs_ATLAS_u_tmp.txt | sort | uniq > runs_ATLAS_u.txt")
#os.popen("cat runs_ATLAS_g_tmp.txt | sort | uniq > runs_ATLAS_g.txt")
#os.popen("cat runs_ATLAS_i_tmp.txt | sort | uniq > runs_ATLAS_i.txt")
#os.popen("cat runs_ATLAS_r_tmp.txt | sort | uniq > runs_ATLAS_r.txt")
#os.popen("cat runs_ATLAS_?.txt | sort | uniq > runs_ATLAS_total.txt")

#os.popen("rm runs_ATLAS_?_tmp.txt")
