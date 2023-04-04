#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:22:00 2021

@author: koppe
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import scipy.interpolate


d=np.array(0)
for subdir, dirs, files in os.walk(r'./Messwerte'):
   for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")
        
        if "NaDline" in filepath and filepath.endswith(".txt") :
            d=int(filepath[filepath.find("spalt")+5:filepath.find("spalt")+8]) # Mikrometer
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
                
        
        