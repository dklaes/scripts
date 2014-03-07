# Script for plotting coordinates of ATLAS and KiDS observations, ATLAS and KiDS coverage.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pylab as lab
import angles
import sys

fileKiDS = sys.argv[1]
fileATLAS = sys.argv[2]

datakids = open(fileKiDS,'r')
dataatlas = open(fileATLAS,'r')

def readdata(file):
	RA = np.array([])
	DEC = np.array([])
	data = open(file, 'r')
	for line in data:
		entries = line.strip().split(" ")
		for i in range(entries.count('')):
			entries.remove('')
		string_coords = str(entries[1] + " " + entries[2])
		RA = np.append(RA, angles.h2d(angles.pposition(string_coords)[0]))
		DEC = np.append(DEC, angles.pposition(string_coords)[1])
	return RA, DEC



fig = plt.figure()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

RA, DEC = readdata(fileATLAS)
RA[RA > 180.0] -= 360.0
p1, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'bs', markeredgewidth=0.0, markersize=1.7)
ax1.legend([p1], ["ATLAS data"])
lab.savefig('ATLAS_data_only.png')

RA, DEC = readdata(fileKiDS)
RA[RA > 180.0] -= 360.0
p2, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'ks', markeredgewidth=0.0, markersize=1.7)
ax1.legend([p1,p2], ["ATLAS data", "KiDS data"])

lab.savefig('ATLAS_KiDS_data_only.png')


lab.clf()
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

RA, DEC = readdata(fileKiDS)
RA[RA > 180.0] -= 360.0
p1, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'ks', markeredgewidth=0.0, markersize=1.7)
ax1.legend([p1], ["KiDS data"])
lab.savefig('KiDS_only.png')


# ATLAS area
lab.clf()
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

# First area.
RA = np.array([])
DEC = np.array([])
point1 = '21:30:00.0000 -40:00:00.0000'
point2 = '21:30:00.0000 -10:00:00.0000'
point3 = '04:00:00.0000 -10:00:00.0000'
point4 = '04:00:00.0000 -40:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point3)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point4)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
DEC = np.append(DEC, angles.pposition(point3)[1])
DEC = np.append(DEC, angles.pposition(point4)[1])
DEC = np.append(DEC, angles.pposition(point1)[1])

RA[RA > 180.0] -= 360.0
p1, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'b')

# Second area (right).
RA = np.array([])
DEC = np.array([])
point5 = '12:00:00.0000 -02:00:00.0000'
point6 = '10:00:00.0000 -02:00:00.0000'
point7 = '10:00:00.0000 -29:00:00.0000'
point8 = '12:00:00.0000 -29:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point5)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point6)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point7)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point8)[0]))
DEC = np.append(DEC, angles.pposition(point5)[1])
DEC = np.append(DEC, angles.pposition(point6)[1])
DEC = np.append(DEC, angles.pposition(point7)[1])
DEC = np.append(DEC, angles.pposition(point8)[1])

p2, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'b')


# Second area (left).
RA = np.array([])
DEC = np.array([])

point9 = '12:00:00.0001 -02:00:00.0000'
point10 = '15:30:00.0000 -02:00:00.0000'
point11 = '15:30:00.0000 -20:00:00.0000'
point12 = '15:00:00.0000 -20:00:00.0000'
point13 = '15:00:00.0000 -29:00:00.0000'
point14 = '12:00:00.0001 -29:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point14)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point13)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point12)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point11)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point10)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point9)[0]))
DEC = np.append(DEC, angles.pposition(point14)[1])
DEC = np.append(DEC, angles.pposition(point13)[1])
DEC = np.append(DEC, angles.pposition(point12)[1])
DEC = np.append(DEC, angles.pposition(point11)[1])
DEC = np.append(DEC, angles.pposition(point10)[1])
DEC = np.append(DEC, angles.pposition(point9)[1])


RA[RA > 180.0] -= 360.0

p3, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'b')

RA, DEC = readdata(fileATLAS)
RA[RA > 180.0] -= 360.0
p4, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'bs', markeredgewidth=0.0, markersize=1.7)
ax1.legend([p1], ["ATLAS"])
#lab.savefig('ATLAS_area.png')





# ATLAS area
plt.clf()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

RA = np.array([])
DEC = np.array([])
point1 = '21:30:00.0000 -40:00:00.0000'
point2 = '04:00:00.0000 -10:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect1 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")


RA = np.array([])
DEC = np.array([])
point1 = '10:00:00.0000 -29:00:00.0000'
point2 = '12:00:00.0000 -02:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect2 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")


RA = np.array([])
DEC = np.array([])
point1 = '12:00:00.0001 -29:00:00.0000'
point2 = '15:00:00.0000 -02:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect3 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")


RA = np.array([])
DEC = np.array([])
point1 = '15:00:00.0000 -20:00:00.0000'
point2 = '15:30:00.0000 -02:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect4 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")

ax1.add_patch(rect1)
ax1.add_patch(rect2)
ax1.add_patch(rect3)
ax1.add_patch(rect4)
ax1.legend([rect1], ["ATLAS area"])
lab.savefig('ATLAS_area.png')





# ATLAS area + data
plt.clf()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

RA = np.array([])
DEC = np.array([])
point1 = '21:30:00.0000 -40:00:00.0000'
point2 = '04:00:00.0000 -10:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect1 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")

RA = np.array([])
DEC = np.array([])
point1 = '10:00:00.0000 -29:00:00.0000'
point2 = '12:00:00.0000 -02:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect2 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")

RA = np.array([])
DEC = np.array([])
point1 = '12:00:00.0001 -29:00:00.0000'
point2 = '15:00:00.0000 -02:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect3 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")

RA = np.array([])
DEC = np.array([])
point1 = '15:00:00.0000 -20:00:00.0000'
point2 = '15:30:00.0000 -02:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect4 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="yellow")

ax1.add_patch(rect1)
ax1.add_patch(rect2)
ax1.add_patch(rect3)
ax1.add_patch(rect4)

RA, DEC = readdata(fileATLAS)
RA[RA > 180.0] -= 360.0
p1, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'bs', markeredgewidth=0.0, markersize=1.7)
ax1.legend([rect1,p1], ["ATLAS area", "ATLAS data"])
lab.savefig('ATLAS_area_data.png')





# KiDS area
plt.clf()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

RA = np.array([])
DEC = np.array([])
point1 = '15:52:00.0000 -03:00:00.0000'
point2 = '15:00:00.0000 +05:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect1 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '15:00:00.0000 -05:00:00.0000'
point2 = '12:00:00.0001 +05:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect2 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '10:00:00.0000 -05:00:00.0000'
point2 = '12:00:00.0000 +05:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect3 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '08:40:00.0000 -03:00:00.0000'
point2 = '09:08:00.0000 -01:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect4 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '22:00:00.0000 -35:00:00.0000'
point2 = '03:30:00.0000 -25:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect5 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

ax1.add_patch(rect1)
ax1.add_patch(rect2)
ax1.add_patch(rect3)
ax1.add_patch(rect4)
ax1.add_patch(rect5)
ax1.legend([rect1], ["KiDS area"])
lab.savefig('KiDS_area.png')





# KiDS area + data
plt.clf()
ax1 = fig.add_subplot(111, projection='mollweide')
ax1.grid()

RA = np.array([])
DEC = np.array([])
point1 = '15:52:00.0000 -03:00:00.0000'
point2 = '15:00:00.0000 +05:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect1 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '15:00:00.0000 -05:00:00.0000'
point2 = '12:00:00.0001 +05:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect2 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '10:00:00.0000 -05:00:00.0000'
point2 = '12:00:00.0000 +05:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect3 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '08:40:00.0000 -03:00:00.0000'
point2 = '09:08:00.0000 -01:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect4 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

RA = np.array([])
DEC = np.array([])
point1 = '22:00:00.0000 -35:00:00.0000'
point2 = '03:30:00.0000 -25:00:00.0000'
RA = np.append(RA, angles.h2d(angles.pposition(point1)[0]))
RA = np.append(RA, angles.h2d(angles.pposition(point2)[0]))
DEC = np.append(DEC, angles.pposition(point1)[1])
DEC = np.append(DEC, angles.pposition(point2)[1])
RA[RA > 180.0] -= 360.0
rect5 = matplotlib.patches.Rectangle((RA[0]*np.pi/180.0,DEC[0]*np.pi/180.0),(RA[1]-RA[0])*np.pi/180.0, (DEC[1]-DEC[0])*np.pi/180.0,color="magenta")

ax1.add_patch(rect1)
ax1.add_patch(rect2)
ax1.add_patch(rect3)
ax1.add_patch(rect4)
ax1.add_patch(rect5)

RA, DEC = readdata(fileKiDS)
RA[RA > 180.0] -= 360.0
p1, = ax1.plot(RA*np.pi/180.0,DEC*np.pi/180.0,'ks', markeredgewidth=0.0, markersize=1.7)

ax1.legend([rect1, p1], ["KiDS area", "KiDS data"])
lab.savefig('KiDS_area_data.png')
