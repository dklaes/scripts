import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pylab as lab
import numpy as np

#lab.clf()
fig = plt.figure()

seeing_u = np.genfromtxt('seeing_u_SDSS.txt', dtype='str')
#data_u = (seeing_u[:,1][1:]).astype(np.float)
data_u = seeing_u.astype(np.float)
num_u = len(data_u)
mean_u = np.mean(data_u)
sigma_u = np.std(data_u)
textstr_u = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_u, mean_u, sigma_u)

seeing_g = np.genfromtxt('seeing_g_SDSS.txt', dtype='str')
#data_g = (seeing_g[:,1][1:]).astype(np.float)
data_g = seeing_g.astype(np.float)
num_g = len(data_g)
mean_g = np.mean(data_g)
sigma_g = np.std(data_g)
textstr_g = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_g, mean_g, sigma_g)

seeing_r = np.genfromtxt('seeing_r_SDSS.txt', dtype='str')
#data_r = (seeing_r[:,1][1:]).astype(np.float)
data_r = seeing_r.astype(np.float)
num_r = len(data_r)
mean_r = np.mean(data_r)
sigma_r = np.std(data_r)
textstr_r = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_r, mean_r, sigma_r)

seeing_i = np.genfromtxt('seeing_i_SDSS.txt', dtype='str')
#data_i = (seeing_i[:,1][1:]).astype(np.float)
data_i = seeing_i.astype(np.float)
num_i = len(data_i)
mean_i = np.mean(data_i)
sigma_i = np.std(data_i)
textstr_i = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_i, mean_i, sigma_i)

seeing_z = np.genfromtxt('seeing_z_SDSS.txt', dtype='str')
#data_z = (seeing_z[:,1][1:]).astype(np.float)
data_z = seeing_z.astype(np.float)
num_z = len(data_z)
mean_z = np.mean(data_z)
sigma_z = np.std(data_z)
textstr_z = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_z, mean_z, sigma_z)




# l1
ax1 = fig.add_subplot(5,2,1)
n, bins, patches = plt.hist(data_u, 21)
lab.setp(patches, 'facecolor', 'b')
plt.xlim([0.2,2.2])
plt.ylim([0,100])
plt.yticks([0,25,50,75,100])
plt.title('KiDS data\ncoadded images')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax1.text(0.75, 0.85, textstr_u, transform=ax1.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax1.text(0.05, 0.85, 'u_SDSS', transform=ax1.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax1.get_xticklabels(), visible=False)

# l2
ax3 = fig.add_subplot(5,2,3)
n, bins, patches = plt.hist(data_g, 21)
lab.setp(patches, 'facecolor', 'g')
plt.xlim([0.2,2.2])
plt.ylim([0,100])
plt.yticks([0,25,50,75,100])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax3.text(0.75, 0.85, textstr_g, transform=ax3.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax3.text(0.05, 0.85, 'g_SDSS', transform=ax3.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax3.get_xticklabels(), visible=False)

# l3
ax5 = fig.add_subplot(5,2,5)
n, bins, patches = plt.hist(data_r, 21)
lab.setp(patches, 'facecolor', 'r')
plt.xlim([0.2,2.2])
plt.ylim([0,100])
plt.yticks([0,25,50,75,100])
plt.ylabel('Number of pointings / images')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax5.text(0.75, 0.85, textstr_r, transform=ax5.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax5.text(0.05, 0.85, 'r_SDSS', transform=ax5.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax5.get_xticklabels(), visible=False)

# l4
ax7 = fig.add_subplot(5,2,7)
n, bins, patches = plt.hist(data_i, 21)
lab.setp(patches, 'facecolor', 'm')
plt.xlim([0.2,2.2])
plt.ylim([0,100])
plt.yticks([0,25,50,75,100])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax7.text(0.75, 0.85, textstr_i, transform=ax7.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax7.text(0.05, 0.85, 'i_SDSS', transform=ax7.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax7.get_xticklabels(), visible=False)

# l5
ax9 = fig.add_subplot(5,2,9)
n, bins, patches = plt.hist(data_z, 21)
lab.setp(patches, 'facecolor', '0.75')
plt.xlim([0.2,2.2])
plt.ylim([0,100])
plt.yticks([0,25,50,75,100])
plt.xlabel('Seeing in arcseconds')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax9.text(0.75, 0.85, textstr_z, transform=ax9.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax9.text(0.05, 0.85, 'z_SDSS', transform=ax9.transAxes, fontsize=8, verticalalignment='top', bbox=props)


seeing_individual_u = np.genfromtxt('seeing_individual_u_SDSS.txt', dtype='str')
data_individual_u = (seeing_individual_u).astype(np.float)
num_individual_u = len(data_individual_u)
mean_individual_u = np.mean(data_individual_u)
sigma_individual_u = np.std(data_individual_u)
textstr_individual_u = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_individual_u, mean_individual_u, sigma_individual_u)

seeing_individual_g = np.genfromtxt('seeing_individual_g_SDSS.txt', dtype='str')
data_individual_g = (seeing_individual_g).astype(np.float)
num_individual_g = len(data_individual_g)
mean_individual_g = np.mean(data_individual_g)
sigma_individual_g = np.std(data_individual_g)
textstr_individual_g = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_individual_g, mean_individual_g, sigma_individual_g)

seeing_individual_r = np.genfromtxt('seeing_individual_r_SDSS.txt', dtype='str')
data_individual_r = (seeing_individual_r).astype(np.float)
num_individual_r = len(data_individual_r)
mean_individual_r = np.mean(data_individual_r)
sigma_individual_r = np.std(data_individual_r)
textstr_individual_r = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_individual_r, mean_individual_r, sigma_individual_r)

seeing_individual_i = np.genfromtxt('seeing_individual_i_SDSS.txt', dtype='str')
data_individual_i = (seeing_individual_i).astype(np.float)
num_individual_i = len(data_individual_i)
mean_individual_i = np.mean(data_individual_i)
sigma_individual_i = np.std(data_individual_i)
textstr_individual_i = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_individual_i, mean_individual_i, sigma_individual_i)

seeing_individual_z = np.genfromtxt('seeing_individual_z_SDSS.txt', dtype='str')
data_individual_z = (seeing_individual_z).astype(np.float)
num_individual_z = len(data_individual_z)
mean_individual_z = np.mean(data_individual_z)
sigma_individual_z = np.std(data_individual_z)
textstr_individual_z = '$n=%d$\n$\mu=%.2f\'\'$\n$\sigma=%.2f\'\'$'%(num_individual_z, mean_individual_z, sigma_individual_z)


# r1
ax2 = fig.add_subplot(5,2,2)
n, bins, patches = plt.hist(data_individual_u, 21)
lab.setp(patches, 'facecolor', 'b')
plt.xlim([0.2,2.2])
plt.ylim([0,400])
plt.yticks([0,100,200,300,400])
plt.title('KiDS data\nsingle exposures')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax2.text(0.75, 0.85, textstr_individual_u, transform=ax2.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax2.text(0.05, 0.85, 'u_SDSS', transform=ax2.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax2.get_xticklabels(), visible=False)

# r2
ax4 = fig.add_subplot(5,2,4)
n, bins, patches = plt.hist(data_individual_g, 21)
lab.setp(patches, 'facecolor', 'g')
plt.xlim([0.2,2.2])
plt.ylim([0,400])
plt.yticks([0,100,200,300,400])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax4.text(0.75, 0.85, textstr_individual_g, transform=ax4.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax4.text(0.05, 0.85, 'g_SDSS', transform=ax4.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax4.get_xticklabels(), visible=False)

# r3
ax6 = fig.add_subplot(5,2,6)
n, bins, patches = plt.hist(data_individual_r, 21)
lab.setp(patches, 'facecolor', 'r')
plt.xlim([0.2,2.2])
plt.ylim([0,400])
plt.yticks([0,100,200,300,400])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax6.text(0.75, 0.85, textstr_individual_r, transform=ax6.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax6.text(0.05, 0.85, 'r_SDSS', transform=ax6.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax6.get_xticklabels(), visible=False)

# r4
ax8 = fig.add_subplot(5,2,8)
n, bins, patches = plt.hist(data_individual_i, 21)
lab.setp(patches, 'facecolor', 'm')
plt.xlim([0.2,2.2])
plt.ylim([0,400])
plt.yticks([0,100,200,300,400])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax8.text(0.75, 0.85, textstr_individual_i, transform=ax8.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax8.text(0.05, 0.85, 'i_SDSS', transform=ax8.transAxes, fontsize=8, verticalalignment='top', bbox=props)
plt.setp(ax8.get_xticklabels(), visible=False)

# r5
ax10 = fig.add_subplot(5,2,10)
n, bins, patches = plt.hist(data_individual_z, 21)
lab.setp(patches, 'facecolor', '0.75')
plt.xlim([0.2,2.2])
plt.ylim([0,400])
plt.yticks([0,100,200,300,400])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.xlabel('Seeing in arcseconds')
ax10.text(0.75, 0.85, textstr_individual_z, transform=ax10.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax10.text(0.05, 0.85, 'z_SDSS', transform=ax10.transAxes, fontsize=8, verticalalignment='top', bbox=props)


lab.savefig('seeing_distribution.png')
