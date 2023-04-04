#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:05:19 2021

@author: koppe
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import scipy.interpolate
from matplotlib.ticker import MultipleLocator

def func(x,a,b,c,a1,b1,c1):
    return a*np.exp(-0.5*((x-c)/b)**2)+a1*np.exp(-0.5*((x-c1)/b1)**2)

def funcone(x,a,b,c):
    return a*np.exp(-0.5*((x-c)/b)**2)

fig=plt.figure(figsize=[7, 7])
shifthoch=150*20

arrayd=np.array(0)
d1=np.array(0)
d2=np.array(0)

for subdir, dirs, files in os.walk(r'./Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")
        
        if "NaDline" in filepath and filepath.endswith(".txt") and not (filepath.endswith("600mum.txt")) and not (filepath.endswith("550mum.txt")) :# 
            d=int(filepath[filepath.find("spalt")+5:filepath.find("spalt")+8])
            arrayd=np.append(arrayd,d)
            data = np.genfromtxt(filepath)
            datax=data[:,0]
            datay=data[:,1]
            popt, pcov = curve_fit(func, datax, datay, p0=[3000,1,587,2000,1,588])
            print(popt[5]-popt[2])
            
            
            d1=np.append(d1,popt[2])
            d2=np.append(d2,popt[5])
                
        if "NaDline" in filepath and filepath.endswith(".txt") and not (filepath.endswith("600mum.txt")) and  (filepath.endswith("550mum.txt")) :# 
            d=int(filepath[filepath.find("spalt")+5:filepath.find("spalt")+8])
            arrayd=np.append(arrayd,d)
            data = np.genfromtxt(filepath)
            datax=data[:,0]
            datay=data[:,1]
            popt555, pcov = curve_fit(funcone, datax, datay, p0=[3000,1,587])
                                       
            #plt.plot(datax-popt555[2]+587.6,funcone(datax,*popt555)+22*d+shifthoch,'r-')    
            #plt.plot(datax-popt555[2]+587.6,datay+22*d+shifthoch,'k.')
            #plt.text(585.5,22*d+20+shifthoch, str(int(d))+r' $\mu$m')
            
                
meanposd1=np.mean(d1[1:])
meanposd2=np.mean(d2[1:])
meanshift=(588.9950+589.5924)/2-(meanposd1+meanposd2)/2
shiftrueber=meanshift
scale=0.001
for subdir, dirs, files in os.walk(r'./Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")
        
        if "NaDline" in filepath and filepath.endswith(".txt") and not (filepath.endswith("600mum.txt")) and not (filepath.endswith("550mum.txt")) :# 
            d=int(filepath[filepath.find("spalt")+5:filepath.find("spalt")+8])
            arrayd=np.append(arrayd,d)
            data = np.genfromtxt(filepath)
            datax=data[:,0]
            datay=data[:,1]
            popt, pcov = curve_fit(func, datax, datay, p0=[3000,1,587,2000,1,588])
            if d<100:                           
                plt.plot(datax+shiftrueber,func(datax,*popt)*scale+2.5*20*d*scale,'r-')    
                plt.plot(datax+shiftrueber,datay*scale+2.5*20*d*scale,'k.')
                plt.text(586+shiftrueber,2.5*20*d*scale+100*scale, str(int(d))+r' $\mu$m')
                plt.plot(datax+shiftrueber,np.zeros_like(datax)*scale+2.5*20*d*scale,'b--',alpha=0.7)
            elif d>=100:
                plt.plot(datax+shiftrueber,func(datax,*popt)*scale+20*d*scale+shifthoch*scale,'r-')    
                plt.plot(datax+shiftrueber,datay*scale+20*d*scale+shifthoch*scale,'k.')
                plt.text(586+shiftrueber,20*d*scale+100*scale+shifthoch*scale, str(int(d))+r' $\mu$m')
                plt.plot(datax+shiftrueber,np.zeros_like(datax)+20*d*scale+shifthoch*scale,'b--',alpha=0.7)
            
            
            d1=np.append(d1,popt[2])
            d2=np.append(d2,popt[5])
                
        if "NaDline" in filepath and filepath.endswith(".txt") and not (filepath.endswith("600mum.txt")) and  (filepath.endswith("550mum.txt")) :# 
            d=int(filepath[filepath.find("spalt")+5:filepath.find("spalt")+8])
            arrayd=np.append(arrayd,d)
            data = np.genfromtxt(filepath)
            datax=data[:,0]
            datay=data[:,1]
            popt555, pcov = curve_fit(funcone, datax, datay, p0=[3000,1,587])
                                       
            plt.plot(datax+shiftrueber-popt555[2]+587.6,funcone(datax,*popt555)*scale+22*d*scale+shifthoch*scale,'r-')    
            plt.plot(datax+shiftrueber-popt555[2]+587.6,datay*scale+22*d*scale+shifthoch*scale,'k.')
            plt.text(586+shiftrueber,22*d*scale+100*scale+shifthoch*scale, str(int(d))+r' $\mu$m')
            plt.plot(datax+shiftrueber,np.zeros_like(datax)+22*d*scale+shifthoch*scale,'b--',alpha=0.7)
            




plt.xlabel(r'$\lambda$ in nm')
plt.ylabel(r'Intensität $n$ in $10^3$')

plt.grid()
plt.xlim([587.5, 590.5])
plt.show()  

#plt.savefig("NaDLinie.pdf", bbox_inches='tight')  # .pdf dann in Latex einfügen mit includegraphix....



#
            
       