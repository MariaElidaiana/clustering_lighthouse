import cluster_toolkit as clusterwl
import numpy as np
import os
import matplotlib.pyplot as plt

dir_lin = './output_xi_mm/matter_power_lin/'
k = np.genfromtxt(os.path.join(dir_lin,"k_h.txt"), skip_header=1)
P_k = np.genfromtxt(os.path.join(dir_lin,"p_k.txt"), skip_header=1)[2] # getting the P_k for z=0.2

xi_mm_heide = './xi_mm_z0.2_for_maria.dat'
r_heide = np.genfromtxt(xi_mm_heide, skip_header=5)[:,0]
xi_mm_heide = np.genfromtxt(xi_mm_heide, skip_header=5)[:,1]

mass=1e14
omega_m=0.267
h=0.71
#c = 5
NR = 1000
R = np.logspace(-2, 1.5, NR, base=10)
Rp = np.logspace(-4.2, 3, NR, base=10)
xi_mm = clusterwl.xi.xi_mm_at_R(Rp, k, P_k)

plt.figure()
plt.plot(r_heide*h, xi_mm_heide, label='Heide: z=0.2')
plt.plot(Rp, xi_mm,label='Tom: z=0.2')
plt.xscale("log",  nonposx='clip')
plt.yscale("log",  nonposy='clip')
plt.ylabel(r'$\xi_{mm}$')
plt.xlabel(r'$r\,\, [Mpc/h]$')
plt.legend(loc='upper right')
plt.savefig('xi_mm_Tom_x_Heide_z0.2.png')
