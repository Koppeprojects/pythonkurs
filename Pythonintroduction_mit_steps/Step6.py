#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:57:37 2021

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
            if filepath.endswith(".txt"):
                
                data = np.genfromtxt(filepath)
                datax=data[:,0]
                datay=data[:,1]





plt.plot(datax,datay,'-')
plt.xlabel(r'$\lambda$ in nm')
plt.ylabel(r'Intensity in counts')
plt.grid()
plt.xlim([585, 590])
plt.show()  



'''

plt.savefig("doubleprobe.pdf", bbox_inches='tight')
'''             
                
        
        