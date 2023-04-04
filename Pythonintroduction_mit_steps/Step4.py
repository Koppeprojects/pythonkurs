#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:36:59 2021

@author: koppe
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import scipy.interpolate



for subdir, dirs, files in os.walk(r'./Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")
        
        if "NaDline" in filepath:
            if filepath.endswith(".txt") and "NaDline" in filepath:
                data = np.genfromtxt(filepath)

                datax=data[:,0]
                datay=data[:,1]
                
                plt.plot(datax,datay,'-')
                plt.show() 
                



#Ich will sehen was passiert!

#nötig



#optional aber beim copy und paste von alten Auswertungen oder vom Internet kommt das immer gleich  mit
'''
plt.xlabel('$U_\mathrm{S}$ in V')
plt.ylabel('$I_\mathrm{S}$ in $10^{-6}\,$A')
plt.grid()
plt.savefig("NaDline.pdf", bbox_inches='tight')
'''             
                
        
        