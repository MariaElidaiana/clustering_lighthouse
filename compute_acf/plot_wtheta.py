import numpy as np
import matplotlib.pyplot as plt

w = np.genfromtxt('./output_wtheta/galaxy_xi/bin_1_1.txt', skip_header=1)
theta = np.genfromtxt('./output_wtheta/galaxy_xi/theta.txt', skip_header=2)


plt.plot(theta*(180./np.pi), w)
plt.xlabel(r'$\theta \, [deg]$')
plt.ylabel(r'$w(\theta)$')
plt.xscale("log",  nonposx='clip')
plt.yscale("log",  nonposy='clip')
plt.savefig('wtheta_nz.png')
