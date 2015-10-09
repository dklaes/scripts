import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pylab as lab
import numpy as np
import os

radius = 2.0
pixscale = 0.214
area = np.pi * radius * radius / (pixscale * pixscale)

fig = plt.figure()

bins = np.arange(19.5,25.6,0.1)

# l1
if os.path.isfile('mag_limit_u_SDSS.txt'):
  coadd_u = np.genfromtxt('mag_limit_u_SDSS.txt', dtype='str')
  backgrd_dev_u = (coadd_u[:,0]).astype(np.float)
  ZP_u = (coadd_u[:,1]).astype(np.float)
  mag_limit_u = ZP_u - 2.5*np.log10(5.0 * np.sqrt(area) * backgrd_dev_u)
  num_u = len(mag_limit_u)
  mean_u = np.mean(mag_limit_u)
  sigma_u = np.std(mag_limit_u)
  textstr_u = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_u, mean_u, sigma_u)

  ax1 = fig.add_subplot(5,2,1)
  n, bins, patches = plt.hist(mag_limit_u, bins = bins)
  lab.setp(patches, 'facecolor', 'b')
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  plt.title('ATLAS data\ncoadded images')
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax1.text(0.75, 0.85, textstr_u, transform=ax1.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax1.text(0.05, 0.85, 'u_SDSS', transform=ax1.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax1.get_xticklabels(), visible=False)
else:
  textstr_u = '$n=N/A$\n$\mu=N/A$\n$\sigma=N/A$'

  ax1 = fig.add_subplot(5,2,1)
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  plt.title('ATLAS data\ncoadded images')
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax1.text(0.75, 0.85, textstr_u, transform=ax1.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax1.text(0.05, 0.85, 'u_SDSS', transform=ax1.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax1.get_xticklabels(), visible=False)


# l2
if os.path.isfile('mag_limit_g_SDSS.txt'):
  coadd_g = np.genfromtxt('mag_limit_g_SDSS.txt', dtype='str')
  backgrd_dev_g = (coadd_g[:,0]).astype(np.float)
  ZP_g = (coadd_g[:,1]).astype(np.float)
  mag_limit_g = ZP_g - 2.5*np.log10(5.0 * np.sqrt(area) * backgrd_dev_g)
  num_g = len(mag_limit_g)
  mean_g = np.mean(mag_limit_g)
  sigma_g = np.std(mag_limit_g)
  textstr_g = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_g, mean_g, sigma_g)

  ax3 = fig.add_subplot(5,2,3)
  n, bins, patches = plt.hist(mag_limit_g, bins = bins)
  lab.setp(patches, 'facecolor', 'g')
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax3.text(0.75, 0.85, textstr_g, transform=ax3.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax3.text(0.05, 0.85, 'g_SDSS', transform=ax3.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax3.get_xticklabels(), visible=False)
else:
  textstr_g = '$n=N/A$\n$\mu=N/A$\n$\sigma=N/A$'

  ax3 = fig.add_subplot(5,2,3)
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax3.text(0.75, 0.85, textstr_g, transform=ax3.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax3.text(0.05, 0.85, 'g_SDSS', transform=ax3.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax3.get_xticklabels(), visible=False)


# l3
if os.path.isfile('mag_limit_r_SDSS.txt'):
  coadd_r = np.genfromtxt('mag_limit_r_SDSS.txt', dtype='str')
  backgrd_dev = (coadd_r[:,0]).astype(np.float)
  ZP = (coadd_r[:,1]).astype(np.float)
  mag_limit_r = ZP - 2.5*np.log10(5.0 * np.sqrt(area) * backgrd_dev)
  num_r = len(mag_limit_r)
  mean_r = np.mean(mag_limit_r)
  sigma_r = np.std(mag_limit_r)
  textstr_r = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_r, mean_r, sigma_r)

  ax5 = fig.add_subplot(5,2,5)
  n, bins, patches = plt.hist(mag_limit_r, bins = bins)
  lab.setp(patches, 'facecolor', 'r')
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  plt.ylabel('Number of pointings / images')
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax5.text(0.75, 0.85, textstr_r, transform=ax5.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax5.text(0.05, 0.85, 'r_SDSS', transform=ax5.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax5.get_xticklabels(), visible=False)
else:
  textstr_r = '$n=N/A$\n$\mu=N/A$\n$\sigma=N/A$'

  ax5 = fig.add_subplot(5,2,5)
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  plt.ylabel('Number of pointings / images')
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax5.text(0.75, 0.85, textstr_r, transform=ax5.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax5.text(0.05, 0.85, 'r_SDSS', transform=ax5.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax5.get_xticklabels(), visible=False)


# l4
if os.path.isfile('mag_limit_i_SDSS.txt'):
  coadd_i = np.genfromtxt('mag_limit_i_SDSS.txt', dtype='str')
  backgrd_dev_i = (coadd_i[:,0]).astype(np.float)
  ZP_i = (coadd_i[:,1]).astype(np.float)
  mag_limit_i = ZP_i - 2.5*np.log10(5.0 * np.sqrt(area) * backgrd_dev_i)
  num_i = len(mag_limit_i)
  mean_i = np.mean(mag_limit_i)
  sigma_i = np.std(mag_limit_i)
  textstr_i = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_i, mean_i, sigma_i)

  ax7 = fig.add_subplot(5,2,7)
  n, bins, patches = plt.hist(mag_limit_i, bins = bins)
  lab.setp(patches, 'facecolor', 'm')
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax7.text(0.75, 0.85, textstr_i, transform=ax7.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax7.text(0.05, 0.85, 'i_SDSS', transform=ax7.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax7.get_xticklabels(), visible=False)
else:
  textstr_i = '$n=N/A$\n$\mu=N/A$\n$\sigma=N/A$'

  ax7 = fig.add_subplot(5,2,7)
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  ax7.text(0.75, 0.85, textstr_i, transform=ax7.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax7.text(0.05, 0.85, 'i_SDSS', transform=ax7.transAxes, fontsize=8, verticalalignment='top', bbox=props)
  plt.setp(ax7.get_xticklabels(), visible=False)


# l5
if os.path.isfile('mag_limit_z_SDSS.txt'):
  coadd_z = np.genfromtxt('mag_limit_z_SDSS.txt', dtype='str')
  backgrd_dev_z = (coadd_z[:,0]).astype(np.float)
  ZP_z = (coadd_z[:,1]).astype(np.float)
  mag_limit_z = ZP_z - 2.5*np.log10(5.0 * np.sqrt(area) * backgrd_dev_z)
  num_z = len(mag_limit_z)
  mean_z = np.mean(mag_limit_z)
  sigma_z = np.std(mag_limit_z)
  textstr_z = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_z, mean_z, sigma_z)

  ax9 = fig.add_subplot(5,2,9)
  n, bins, patches = plt.hist(mag_limit_z, bins = bins)
  lab.setp(patches, 'facecolor', '0.75')
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  plt.xlabel('Limiting magnitude')
  ax9.text(0.75, 0.85, textstr_z, transform=ax9.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax9.text(0.05, 0.85, 'z_SDSS', transform=ax9.transAxes, fontsize=8, verticalalignment='top', bbox=props)
else:
  textstr_z = '$n=N/A$\n$\mu=N/A$\n$\sigma=N/A$'

  ax9 = fig.add_subplot(5,2,9)
  plt.xlim([19.5,25.5])
  plt.ylim([0,750])
  plt.yticks([0,250,500,750])
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  plt.xlabel('Limiting magnitude')
  ax9.text(0.75, 0.85, textstr_z, transform=ax9.transAxes, fontsize=10, verticalalignment='top', bbox=props)
  ax9.text(0.05, 0.85, 'z_SDSS', transform=ax9.transAxes, fontsize=8, verticalalignment='top', bbox=props)



#individual_u = np.genfromtxt('mag_limit_individual_u_SDSS.txt', dtype='str')
#backgrd_dev_u = (individual_u[:,0]).astype(np.float)
#ZP_u = (individual_u[:,1]).astype(np.float)
#exptime_u = (individual_u[:,2]).astype(np.float)
#mag_limit_u = ZP_u - 2.5*np.log10(5.0 * np.sqrt(area) * -1.08574 * np.log10(backgrd_dev_u/exptime_u))
#num_u = len(mag_limit_u)/32
#mean_u = np.mean(mag_limit_u)
#sigma_u = np.std(mag_limit_u)
#textstr_u = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_u, mean_u, sigma_u)

#individual_g = np.genfromtxt('mag_limit_individual_g_SDSS.txt', dtype='str')
#backgrd_dev_g = (individual_g[:,0]).astype(np.float)
#ZP_g = (individual_g[:,1]).astype(np.float)
#exptime_g = (individual_g[:,2]).astype(np.float)
#mag_limit_g = ZP_g - 2.5*np.log10(5.0 * np.sqrt(area) * -1.08574 * np.log10(backgrd_dev_g/exptime_g))
#num_g = len(mag_limit_g)/32
#mean_g = np.mean(mag_limit_g)
#sigma_g = np.std(mag_limit_g)
#textstr_g = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_g, mean_g, sigma_g)

#individual_r = np.genfromtxt('mag_limit_individual_r_SDSS.txt', dtype='str')
#backgrd_dev_r = (individual_r[:,0]).astype(np.float)
#ZP_r = (individual_r[:,1]).astype(np.float)
#exptime_r = (individual_r[:,2]).astype(np.float)
#mag_limit_r = ZP_r - 2.5*np.log10(5.0 * np.sqrt(area) * -1.08574 * np.log10(backgrd_dev_r/exptime_r))
#num_r = len(mag_limit_r)/32
#mean_r = np.mean(mag_limit_r)
#sigma_r = np.std(mag_limit_r)
#textstr_r = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_r, mean_r, sigma_r)

#individual_i = np.genfromtxt('mag_limit_individual_i_SDSS.txt', dtype='str')
#backgrd_dev_i = (individual_i[:,0]).astype(np.float)
#ZP_i = (individual_i[:,1]).astype(np.float)
#exptime_i = (individual_i[:,2]).astype(np.float)
#mag_limit_i = ZP_i - 2.5*np.log10(5.0 * np.sqrt(area) * -1.08574 * np.log10(backgrd_dev_i/exptime_i))
#num_i = len(mag_limit_i)/32
#mean_i = np.mean(mag_limit_i)
#sigma_i = np.std(mag_limit_i)
#textstr_i = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_i, mean_i, sigma_i)

#individual_z = np.genfromtxt('mag_limit_individual_z_SDSS.txt', dtype='str')
#backgrd_dev_z = (individual_z[:,0]).astype(np.float)
#ZP_z = (individual_z[:,1]).astype(np.float)
#exptime_z = (individual_z[:,2]).astype(np.float)
#mag_limit_z = ZP_z - 2.5*np.log10(5.0 * np.sqrt(area) * -1.08574 * np.log10(backgrd_dev_z/exptime_z))
#num_z = len(mag_limit_z)/32
#mean_z = np.mean(mag_limit_z)
#sigma_z = np.std(mag_limit_z)
#textstr_z = '$n=%d$\n$\mu=%.2f$\n$\sigma=%.2f$'%(num_z, mean_z, sigma_z)

#bins = np.arange(14.0,20.1,0.1)

## r1
#ax2 = fig.add_subplot(5,2,2)
#n, bins, patches = plt.hist(mag_limit_u, bins = bins)
#lab.setp(patches, 'facecolor', 'b')
#plt.xlim([17,22])
#plt.ylim([0,25600])
#plt.yticks([0,6400,12800,19200,25600], (0, 200, 400, 600, 800))
#plt.title('ATLAS data (ATLAS-S overlap)\nsingle exposures')
#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#ax2.text(0.75, 0.85, textstr_u, transform=ax2.transAxes, fontsize=10, verticalalignment='top', bbox=props)
#ax2.text(0.05, 0.85, 'u_SDSS', transform=ax2.transAxes, fontsize=8, verticalalignment='top', bbox=props)
#plt.setp(ax2.get_xticklabels(), visible=False)

## r2
#ax4 = fig.add_subplot(5,2,4)
#n, bins, patches = plt.hist(mag_limit_g, bins = bins)
#lab.setp(patches, 'facecolor', 'g')
#plt.xlim([17,22])
#plt.ylim([0,25600])
#plt.yticks([0,6400,12800,19200,25600], (0, 200, 400, 600, 800))
#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#ax4.text(0.75, 0.85, textstr_g, transform=ax4.transAxes, fontsize=10, verticalalignment='top', bbox=props)
#ax4.text(0.05, 0.85, 'g_SDSS', transform=ax4.transAxes, fontsize=8, verticalalignment='top', bbox=props)
#plt.setp(ax4.get_xticklabels(), visible=False)

## r3
#ax6 = fig.add_subplot(5,2,6)
#n, bins, patches = plt.hist(mag_limit_r, bins = bins)
#lab.setp(patches, 'facecolor', 'r')
#plt.xlim([17,22])
#plt.ylim([0,25600])
#plt.yticks([0,6400,12800,19200,25600], (0, 200, 400, 600, 800))
#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#ax6.text(0.75, 0.85, textstr_r, transform=ax6.transAxes, fontsize=10, verticalalignment='top', bbox=props)
#ax6.text(0.05, 0.85, 'r_SDSS', transform=ax6.transAxes, fontsize=8, verticalalignment='top', bbox=props)
#plt.setp(ax6.get_xticklabels(), visible=False)

## r4
#ax8 = fig.add_subplot(5,2,8)
#n, bins, patches = plt.hist(mag_limit_i, bins = bins)
#lab.setp(patches, 'facecolor', 'm')
#plt.xlim([17,22])
#plt.ylim([0,25600])
#plt.yticks([0,6400,12800,19200,25600], (0, 200, 400, 600, 800))
#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#ax8.text(0.75, 0.85, textstr_i, transform=ax8.transAxes, fontsize=10, verticalalignment='top', bbox=props)
#ax8.text(0.05, 0.85, 'i_SDSS', transform=ax8.transAxes, fontsize=8, verticalalignment='top', bbox=props)
#plt.setp(ax8.get_xticklabels(), visible=False)


## r5
#ax10 = fig.add_subplot(5,2,10)
#n, bins, patches = plt.hist(mag_limit_z, bins = bins)
#lab.setp(patches, 'facecolor', '0.75')
#plt.xlim([17,22])
#plt.ylim([0,25600])
#plt.yticks([0,6400,12800,19200,25600], (0, 200, 400, 600, 800))
#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#plt.xlabel('Limiting magnitude')
#ax10.text(0.75, 0.85, textstr_z, transform=ax10.transAxes, fontsize=10, verticalalignment='top', bbox=props)
#ax10.text(0.05, 0.85, 'z_SDSS', transform=ax10.transAxes, fontsize=8, verticalalignment='top', bbox=props)


lab.savefig('mag_limit_distribution.png')
