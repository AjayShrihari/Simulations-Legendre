#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:32:24 2020

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
def Legendre_Poly(n, x):

    if n == 0:
        P = 1
        
    elif n == 1:
        P = x
        
    else:
        P = (1/n)* ((2*n - 1)* x* Legendre_Poly(n-1, x) - (n - 1)* Legendre_Poly(n-2, x))

    return P
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

if l < 0:
    print('n cannot be negative')

m = int(input('Enter m: '))

if m > l or m < (-l):
    print('m must me between -n and +n')



#K = sqrt( ((2*l + 1)* factorial(l - abs(m)))/ (4* pi* factorial(l + abs(m))) )

phi = linspace(0, 2* pi, 100)
tht = linspace(0, pi, 100)

Phi, Tht = meshgrid(phi, tht)

p, q = shape(Phi)
Y    = zeros([p, q])

for i in range(0 + 1, p - 1):
    for j in range(0 + 1, q - 1):

        if m > 0:
        
            Y[i, j] = cos(m* Phi[i, j])* Asso_Leg(l, m, cos(Tht[i, j]))
        
        elif m == 0:
        
            Y[i, j] = Legendre_Poly(l, cos(Tht[i, j]))

p, q = shape(Y)

for i in range(0, p):
    for j in range(0, q):

        if Y[i, j] < 0:
            Tht[i, j] = Tht[i, j] + pi
x, y, z = Spherical2Cartesian(Y, Tht, Phi)
fig = plt.figure('Harmonics')
ax = fig.add_subplot( 111 , projection='3d')
ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = 'k')
plt.title('Spherical Harmonics', fontsize = 14, fontweight = 'bold')
ax.set_xlabel('X', fontsize = 12, fontweight = 'bold')
ax.set_ylabel('Y', fontsize = 12, fontweight = 'bold')
ax.set_zlabel('Z', fontsize = 12, fontweight = 'bold')
plt.show()
