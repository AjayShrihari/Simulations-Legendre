#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:24:17 2020

@author: ajay
"""

from numpy import sin, cos, pi, sqrt, shape, linspace, meshgrid, zeros
from math import factorial
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mp3d
import math
def Spherical2Cartesian(r, theta, phi):

    x = r* sin(theta)* cos(phi)
    y = r* sin(theta)* sin(phi)
    z = r* cos(theta)
    
    return x, y, z

def Legendre_Poly(n, x):

    if n == 0:
        P = 1
        
    elif n == 1:
        P = x
        
    else:
        P = (1/n)* ((2*n - 1)* x* Legendre_Poly(n-1, x) - (n - 1)* Legendre_Poly(n-2, x))

    return P

l = int(input('Enter n:'))

phi = linspace(0, 2* pi, 100)
tht = linspace(0, pi, 100)

Phi, Tht = meshgrid(phi, tht)
p, q = shape(Phi)
P_plot = zeros([p, q])
for i in range(0 + 1, p - 1):
    for j in range(0 + 1, q - 1):
            P_plot[i, j] = math.fabs(Legendre_Poly(l,  cos( Phi[i, j])))
p, q = shape(P_plot)

for i in range(0, p):
    for j in range(0, q):

        if P_plot[i, j] < 0:
            Tht[i, j] = Tht[i, j] + pi
x, y, z = Spherical2Cartesian(P_plot, Tht, Phi)
fig = plt.figure('Plot of Pm cos(m*phi)')
ax = fig.add_subplot( 111 , projection='3d')

ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = 'k')

#plt.axis('square')
plt.title('Plot of Pm cos(m*phi)', fontsize = 14, fontweight = 'bold')
ax.set_xlabel('X', fontsize = 12, fontweight = 'bold')
ax.set_ylabel('Y', fontsize = 12, fontweight = 'bold')
ax.set_zlabel('Z', fontsize = 12, fontweight = 'bold')
plt.show()
