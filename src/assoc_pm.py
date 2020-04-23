#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 19:46:04 2020


"""
from numpy import sin, cos, pi, sqrt, shape, linspace, meshgrid, zeros
from math import factorial
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mp3d
def Spherical2Cartesian(r, theta, phi):

    x = r* sin(theta)* cos(phi)
    y = r* sin(theta)* sin(phi)
    z = r* cos(theta)
    
    return x, y, z

def Asso_Leg(l, m, x):
    
    try:
        if m == 0:
            P = Legendre_Poly(l, x)
            
        elif m > 0:
            P = (1/ sqrt(1 - x**2))* ((l-m+1)* x* Asso_Leg(l, m-1, x) \
                                    - (l+m-1)* Asso_Leg(l-1, m-1, x) )
                                
        
            
    except ZeroDivisionError:
        P = 0
    
    return P
l = int(input('Enter n:'))
m = int(input('Enter m:'))
phi = linspace(0, 2* pi, 100)
tht = linspace(0, pi, 100)

Phi, Tht = meshgrid(phi, tht)
p, q = shape(Phi)
P_plot = zeros([p, q])
for i in range(0 + 1, p - 1):
    for j in range(0 + 1, q - 1):
            P_plot[i, j] = Asso_Leg(l, m, Phi[i,j])
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
