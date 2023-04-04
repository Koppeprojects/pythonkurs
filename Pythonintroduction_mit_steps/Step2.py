#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:29:55 2021

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
        
        
        