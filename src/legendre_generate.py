#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 01:44:34 2020


"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def legendre_plot(legendre):
    '''
    Function to plot based on the list of legendre polynomials
    '''
    fig = plt.figure(1)
    x = np.linspace(-1,1,100)
    plt.plot(x, legendre[0,:], 'r-', label = 'P_0')
    plt.plot(x, legendre[1,:], 'k-', label = 'P_1')
    plt.plot(x, legendre[2,:], 'g-', label = 'P_2')
    plt.plot(x, legendre[3,:], 'b-', label = 'P_3')
    plt.plot(x, legendre[4,:], 'c-', label = 'P_4')
    plt.plot(x, legendre[5,:], 'm-', label = 'P_5')
    plt.plot(x, legendre[6,:], 'y-', label = 'P_6')
#    plt.legend(handles=[plot1, plot2, plot3, plot4, plot5, plot6, plot7], loc=4)
    plt.title("Legendre polynomial")
    plt.legend()
#    plt.legend(framealpha=1, frameon = True)
    plt.savefig("Legendre_polynomial.png")
#    plt.imshow(fig)
    plt.close(fig)
def even_plot(legendre):
    fig = plt.figure(1)
    x = np.linspace(-1,1,100)
    plt.plot(x, legendre[0,:], 'r-', label = 'P_0')
    plt.plot(x, legendre[2,:], 'g-', label = 'P_2')
    plt.plot(x, legendre[4,:], 'c-', label = 'P_4')
    plt.plot(x, legendre[6,:], 'b-', label = 'P_6')
#    plt.legend(handles=[plot1, plot3,  plot5, plot7])
#    plt.legend(framealpha=1, frameon = True)
    plt.title("Even Legendre Polynomial")
    plt.legend()
    plt.savefig("Legendre_polynomial_even.png")
#    plt.imshow(fig)
    plt.close(fig)

def odd_plot(legendre):
    fig = plt.figure(1)
    x = np.linspace(-1,1,100)
    plt.plot(x, legendre[1,:], 'k-', label = 'P_1')
    plt.plot(x, legendre[3,:], 'b-', label = 'P_3')
    plt.plot(x, legendre[5,:], 'c-', label = 'P_5')
#    plt.legend(handles=[plot1, plot3,  plot5], loc=4)
#    plt.legend(framealpha=1, frameon = True)
    plt.title("Odd Legendre Polynomial")
    plt.legend()
    plt.savefig("Legendre_polynomial_odd.png")
    plt.close(fig)
    
def legendre_generate(num_index = 7):
    x = np.linspace(-1,1,100)
    legendre_list = []
    for i in range(num_index):
        y = np.array([])
        for j  in x:
            sum1 = 0
            if i%2 != 0:
                m = (i - 1)/2
            else:
                m = i/2
            a = 0
            while a <= m:
                sum1 += (-1)**a * factorial(2 * i - 2 * a) / (factorial(a) * factorial(i - a) * factorial(i - 2 * a)) * j**(i - 2 * a)
                a = a + 1
            y = np.append(y, 1 / 2 ** i * sum1)
        legendre_list.append(y)
    return np.asarray(legendre_list)
legendre_list = legendre_generate()
legendre_plot(legendre_list)
even_plot(legendre_list)
odd_plot(legendre_list)

    