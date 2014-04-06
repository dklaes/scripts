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
overlapKIDSATLAS = overlap

for k in range(len(overlap)):
	RA = ((str(overlap[k][0])).replace("-", "m")).replace("+", "p")
	DEC = ((str(overlap[k][1])).replace("-", "m")).replace("+", "p")
	os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_u_tmp.txt")
	os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_g_tmp.txt")
	os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_i_tmp.txt")
	os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_r_tmp.txt")

os.popen("cat runs_KIDS_u_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_ATLAS_u.txt")
os.popen("cat runs_KIDS_g_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_ATLAS_g.txt")
os.popen("cat runs_KIDS_i_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_ATLAS_i.txt")
os.popen("cat runs_KIDS_r_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_ATLAS_r.txt")
os.popen("cat runs_KIDS_?.txt | sort | uniq > runs_KIDS_for_KIDS_ATLAS_total.txt")

os.popen("rm runs_KIDS_?_tmp.txt")


for k in range(len(overlap)):
        RA = ((str(overlap[k][2])).replace("-", "m")).replace("+", "p") 
        DEC = ((str(overlap[k][3])).replace("-", "m")).replace("+", "p")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_u_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_g_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_i_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_r_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_z_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_z_tmp.txt")

os.popen("cat runs_ATLAS_u_tmp.txt | sort | uniq > runs_ATLAS_for_KIDS_ATLAS_u.txt")
os.popen("cat runs_ATLAS_g_tmp.txt | sort | uniq > runs_ATLAS_for_KIDS_ATLAS_g.txt")
os.popen("cat runs_ATLAS_i_tmp.txt | sort | uniq > runs_ATLAS_for_KIDS_ATLAS_i.txt")
os.popen("cat runs_ATLAS_r_tmp.txt | sort | uniq > runs_ATLAS_for_KIDS_ATLAS_r.txt")
os.popen("cat runs_ATLAS_z_tmp.txt | sort | uniq > runs_ATLAS_for_KIDS_ATLAS_z.txt")
os.popen("cat runs_ATLAS_?.txt | sort | uniq > runs_ATLAS_for_KIDS_ATLAS_total.txt")

os.popen("rm runs_ATLAS_?_tmp.txt")



# Overlap KiDS and GAMA.
print("")
print("Starting KiDS / GAMA overlap...")
overlap = np.array([])

for i in range(len(coordsKIDS)):
	# Region G9  (129.0 < RA < 141.0, -1.0 < DEC < 3.0), modified to get also partly overlap
	if 128.5 < coordsKIDS[i][0] < 141.5:
		if -1.5 < coordsKIDS[i][1] < 3.5:
			print("KIDS_" + str(coordsKIDS[i][0]) + "_" + str(coordsKIDS[i][1]))
                        overlap = np.append(overlap, [coordsKIDS[i][0], coordsKIDS[i][1]])
	# Region G12 (174.0 < RA < 186.0, -2.0 < DEC < 2.0), modified to get also partly overlap
	elif 173.5 < coordsKIDS[i][0] < 186.5:
		if -2.5 < coordsKIDS[i][1] < 2.5:
                        print("KIDS_" + str(coordsKIDS[i][0]) + "_" + str(coordsKIDS[i][1])) 
                        overlap = np.append(overlap, [coordsKIDS[i][0], coordsKIDS[i][1]])
	# Region G15 (211.5 < RA < 223.5, -2.0 < DEC < 2.0), modified to get also partly overlap
	elif 211.0 < coordsKIDS[i][0] < 224.0:
		if -2.5 < coordsKIDS[i][1] < 2.5:
                        print("KIDS_" + str(coordsKIDS[i][0]) + "_" + str(coordsKIDS[i][1]))
                        overlap = np.append(overlap, [coordsKIDS[i][0], coordsKIDS[i][1]])

overlap = overlap.reshape((-1,2))

for k in range(len(overlap)):
        RA = ((str(overlap[k][0])).replace("-", "m")).replace("+", "p")
        DEC = ((str(overlap[k][1])).replace("-", "m")).replace("+", "p")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_u_tmp.txt")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_g_tmp.txt")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_i_tmp.txt")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_r_tmp.txt")

os.popen("cat runs_KIDS_u_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_GAMA_u.txt")
os.popen("cat runs_KIDS_g_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_GAMA_g.txt")
os.popen("cat runs_KIDS_i_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_GAMA_i.txt")
os.popen("cat runs_KIDS_r_tmp.txt | sort | uniq > runs_KIDS_for_KIDS_GAMA_r.txt")
os.popen("cat runs_KIDS_?.txt | sort | uniq > runs_KIDS_for_KIDS_GAMA_total.txt")

os.popen("rm runs_KIDS_?_tmp.txt")



# Overlap ATLAS and GAMA.
print("")
print("Starting ATLAS / GAMA overlap...")
overlap = np.array([])

for i in range(len(coordsATLAS)):
        # Region G9 (129.0 < RA < 141.0, -1.0 < DEC < 3.0), modified to get also partly overlap
        if 128.5 < coordsATLAS[i][0] < 141.5:
                if -1.5 < coordsATLAS[i][1] < 3.5:
                        print("ATLAS_" + str(coordsATLAS[i][0]) + "_" + str(coordsATLAS[i][1]))
                        overlap = np.append(overlap, [coordsATLAS[i][0], coordsATLAS[i][1]])
        # Region G12 (174.0 < RA < 186.0, -2.0 < DEC < 2.0), modified to get also partly overlap
        elif 173.5 < coordsATLAS[i][0] < 186.5:
                if -2.5 < coordsATLAS[i][1] < 2.5:
                        print("ATLAS_" + str(coordsATLAS[i][0]) + "_" + str(coordsATLAS[i][1]))
                        overlap = np.append(overlap, [coordsATLAS[i][0], coordsATLAS[i][1]])
        # Region G15 (211.5 < RA < 223.5, -2.0 < DEC < 2.0), modified to get also partly overlap
        elif 211.0 < coordsATLAS[i][0] < 224.0:
                if -2.5 < coordsATLAS[i][1] < 2.5:
                        print("ATLAS_" + str(coordsATLAS[i][0]) + "_" + str(coordsATLAS[i][1]))
                        overlap = np.append(overlap, [coordsATLAS[i][0], coordsATLAS[i][1]])

overlap = overlap.reshape((-1,2))

for k in range(len(overlap)):
        RA = ((str(overlap[k][0])).replace("-", "m")).replace("+", "p")
        DEC = ((str(overlap[k][1])).replace("-", "m")).replace("+", "p")
	print("ATLAS_" + RA + "_" + DEC)
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_u_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_g_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_i_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_r_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_z_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_z_tmp.txt")

os.popen("cat runs_ATLAS_u_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_GAMA_u.txt")
os.popen("cat runs_ATLAS_g_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_GAMA_g.txt")
os.popen("cat runs_ATLAS_i_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_GAMA_i.txt")
os.popen("cat runs_ATLAS_r_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_GAMA_r.txt")
os.popen("cat runs_ATLAS_z_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_GAMA_z.txt")
os.popen("cat runs_ATLAS_?.txt | sort | uniq > runs_ATLAS_for_ATLAS_GAMA_total.txt")

os.popen("rm runs_ATLAS_?_tmp.txt")



# Overlap ATLAS, KiDS and GAMA.
# overlapKIDSATLAS: KIDS_RA, KIDS_DEC, ATLAS_RA, ATLAS_DEC
print("")
print("Starting KiDS / ATLAS / GAMA overlap...")
overlap = np.array([])

for i in range(len(overlapKIDSATLAS)):
        # Region G9 (129.0 < RA < 141.0, -1.0 < DEC < 3.0), modified to get also partly overlap
        if 128.5 < overlapKIDSATLAS[i][0] < 141.5:
                if -1.5 < overlapKIDSATLAS[i][1] < 3.5:
                        print("KIDS_" + str(overlapKIDSATLAS[i][0]) + "_" + str(overlapKIDSATLAS[i][1]) + "-> ATLAS_" + str(overlapKIDSATLAS[i][2]) + "_" + str(overlapKIDSATLAS[i][3]))
                        overlap = np.append(overlap, [overlapKIDSATLAS[i][0], overlapKIDSATLAS[i][1], overlapKIDSATLAS[i][2], overlapKIDSATLAS[i][3]])
        # Region G12 (174.0 < RA < 186.0, -2.0 < DEC < 2.0), modified to get also partly overlap
        elif 173.5 < overlapKIDSATLAS[i][0] < 186.5:
                if -2.5 < overlapKIDSATLAS[i][1] < 2.5:
                        print("KIDS_" + str(overlapKIDSATLAS[i][0]) + "_" + str(overlapKIDSATLAS[i][1]) + "-> ATLAS_" + str(overlapKIDSATLAS[i][2]) + "_" + str(overlapKIDSATLAS[i][3]))
                        overlap = np.append(overlap, [overlapKIDSATLAS[i][0], overlapKIDSATLAS[i][1], overlapKIDSATLAS[i][2], overlapKIDSATLAS[i][3]])
        # Region G15 (211.5 < RA < 223.5, -2.0 < DEC < 2.0), modified to get also partly overlap
        elif 211.0 < overlapKIDSATLAS[i][0] < 224.0:
                if -2.5 < overlapKIDSATLAS[i][1] < 2.5:
                        print("KIDS_" + str(overlapKIDSATLAS[i][0]) + "_" + str(overlapKIDSATLAS[i][1]) + "-> ATLAS_" + str(overlapKIDSATLAS[i][2]) + "_" + str(overlapKIDSATLAS[i][3]))
                        overlap = np.append(overlap, [overlapKIDSATLAS[i][0], overlapKIDSATLAS[i][1], overlapKIDSATLAS[i][2], overlapKIDSATLAS[i][3]])

        # Region G9 (129.0 < RA < 141.0, -1.0 < DEC < 3.0), modified to get also partly overlap
        if 128.5 < overlapKIDSATLAS[i][2] < 141.5:
                if -1.5 < overlapKIDSATLAS[i][3] < 3.5:
                        print("ATLAS_" + str(overlapKIDSATLAS[i][2]) + "_" + str(overlapKIDSATLAS[i][3]) + "-> KIDS_" + str(overlapKIDSATLAS[i][0]) + "_" + str(overlapKIDSATLAS[i][1]))
                        overlap = np.append(overlap, [overlapKIDSATLAS[i][0], overlapKIDSATLAS[i][1], overlapKIDSATLAS[i][2], overlapKIDSATLAS[i][3]])
        # Region G12 (174.0 < RA < 186.0, -2.0 < DEC < 2.0), modified to get also partly overlap
        elif 173.5 < overlapKIDSATLAS[i][2] < 186.5:
                if -2.5 < overlapKIDSATLAS[i][3] < 2.5:
                        print("ATLAS_" + str(overlapKIDSATLAS[i][2]) + "_" + str(overlapKIDSATLAS[i][3]) + "-> KIDS_" + str(overlapKIDSATLAS[i][0]) + "_" + str(overlapKIDSATLAS[i][1]))
                        overlap = np.append(overlap, [overlapKIDSATLAS[i][0], overlapKIDSATLAS[i][1], overlapKIDSATLAS[i][2], overlapKIDSATLAS[i][3]])
        # Region G15 (211.5 < RA < 223.5, -2.0 < DEC < 2.0), modified to get also partly overlap
        elif 211.0 < overlapKIDSATLAS[i][2] < 224.0:
                if -2.5 < overlapKIDSATLAS[i][3] < 2.5:
                        print("ATLAS_" + str(overlapKIDSATLAS[i][2]) + "_" + str(overlapKIDSATLAS[i][3]) + "-> KIDS_" + str(overlapKIDSATLAS[i][0]) + "_" + str(overlapKIDSATLAS[i][1]))
                        overlap = np.append(overlap, [overlapKIDSATLAS[i][0], overlapKIDSATLAS[i][1], overlapKIDSATLAS[i][2], overlapKIDSATLAS[i][3]])

overlap = overlap.reshape((-1,4))

for k in range(len(overlap)):
        RA = ((str(overlap[k][2])).replace("-", "m")).replace("+", "p")
        DEC = ((str(overlap[k][3])).replace("-", "m")).replace("+", "p")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_u_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_g_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_i_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_r_tmp.txt")
        os.popen("grep ATLAS_" + RA + "_" + DEC + " summary_ATLAS_images_z_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_ATLAS_z_tmp.txt")

        RA = ((str(overlap[k][0])).replace("-", "m")).replace("+", "p")
        DEC = ((str(overlap[k][1])).replace("-", "m")).replace("+", "p")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_u_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_u_tmp.txt")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_g_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_g_tmp.txt")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_i_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_i_tmp.txt")
        os.popen("grep KIDS_" + RA + "_" + DEC + " summary_KIDS_images_r_SDSS.txt | awk '{print $1}' | sort | uniq >> runs_KIDS_r_tmp.txt")


os.popen("cat runs_ATLAS_u_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_KIDS_GAMA_u.txt")
os.popen("cat runs_ATLAS_g_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_KIDS_GAMA_g.txt")
os.popen("cat runs_ATLAS_i_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_KIDS_GAMA_i.txt")
os.popen("cat runs_ATLAS_r_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_KIDS_GAMA_r.txt")
os.popen("cat runs_ATLAS_z_tmp.txt | sort | uniq > runs_ATLAS_for_ATLAS_KIDS_GAMA_z.txt")
os.popen("cat runs_ATLAS_?.txt | sort | uniq > runs_ATLAS_for_ATLAS_KIDS_GAMA_total.txt")

os.popen("cat runs_KIDS_u_tmp.txt | sort | uniq > runs_KIDS_for_ATLAS_KIDS_GAMA_u.txt")
os.popen("cat runs_KIDS_g_tmp.txt | sort | uniq > runs_KIDS_for_ATLAS_KIDS_GAMA_g.txt")
os.popen("cat runs_KIDS_i_tmp.txt | sort | uniq > runs_KIDS_for_ATLAS_KIDS_GAMA_i.txt")
os.popen("cat runs_KIDS_r_tmp.txt | sort | uniq > runs_KIDS_for_ATLAS_KIDS_GAMA_r.txt")
os.popen("cat runs_KIDS_?.txt | sort | uniq > runs_KIDS_for_ATLAS_KIDS_GAMA_total.txt")

os.popen("rm runs_ATLAS_?_tmp.txt")
os.popen("rm runs_KIDS_?_tmp.txt")
