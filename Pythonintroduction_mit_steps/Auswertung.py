#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:27:43 2021

@author: koppe
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import scipy.interpolate

plt.rcParams.update({'font.size': 15})

deeg=np.array([-0.1,10,20,30,40,50,60,70,80,90])
lei=np.array([0,0,0.15,0.69,1.33,1.89,2.38,2.65,2.7,2.65])

y_interp = scipy.interpolate.interp1d(deeg, lei)





def func(x,a,b,c,a1,b1,c1,a2,b2,c2,a3,b3,c3,a4,b4,c4,a5,b5,c5):
    return a*np.exp(-((x-c)/b)**2)+a1*np.exp(-0.5*((x-c1)/b1)**2)+a2*np.exp(-0.5*((x-c2)/b2)**2)+a3*np.exp(-0.5*((x-c3)/b3)**2)+a4*np.exp(-0.5*((x-c4)/b4)**2)+a5*np.exp(-0.5*((x-c5)/b5)**2)

def funcone(x,a,b,c):
    return a*np.exp(-((x-c)/b)**2)
            
x00=855
positions=[0,20,35,55,70,85]
shiftsteigung=10/1300
xbondaxis=5
sizex=10
sizey=10
msize=6
scale=0.001

tempeee=np.array(0)
INASpos1=np.array(0)
INASpos2=np.array(0)
INASpos3=np.array(0)
INASpos3fel=np.array(0)
INASpos4=np.array(0)
INASpos5=np.array(0)
INASpos6=np.array(0)

INASamp1=np.array(0)
INASamp2=np.array(0)
INASamp3=np.array(0)
INASamp4=np.array(0)
INASamp5=np.array(0)
INASamp6=np.array(0)


INASleipos1=np.array(0)
INASleipos2=np.array(0)
INASleipos3=np.array(0)
INASleipos4=np.array(0)
INASleipos5=np.array(0)
INASleipos6=np.array(0)

INASleiamp1=np.array(0)
INASleiamp2=np.array(0)
INASleiamp3=np.array(0)
INASleiamp4=np.array(0)
INASleiamp5=np.array(0)
INASleiamp6=np.array(0)


deggg=np.array(0)


figinas1, axs =plt.subplots(1,2,gridspec_kw=dict(wspace=0.3,hspace=0.3))
figinas1.set_figheight(sizey)
figinas1.set_figwidth(sizex)

for subdir, dirs, files in os.walk(r'/Users/koppe/Documents/uni/Apversuche/ansirepo/FP/Quantenpunkte/Photolumineszenz_von_Quantenpunkten/Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r") 
        if "InAs" in filepath:
            if filepath.endswith(".asc") and "temp" in filepath:
                #print(filepath.find("mm"))
                temp=int(filepath[filepath.find("temp")+4:filepath.find("temp")+8])
                tempeee=np.append(tempeee,temp)
                data = np.genfromtxt(filepath)
                datax=data[:,0]
                datay=data[:,1]
                
                popt, pcov = curve_fit(func, datax, datay, p0=[2000-temp,5,x00+positions[0]+temp*shiftsteigung,2000-temp,5,x00+positions[1]+temp*shiftsteigung,2000-temp,5,x00+positions[2]+temp*shiftsteigung,2000-temp,5,x00+positions[3]+temp*shiftsteigung,2000-temp,5,x00+positions[4]+temp*shiftsteigung,2000-temp,5,x00+positions[5]+temp*shiftsteigung],\
                                       bounds=([0,1,x00+positions[0]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[1]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[2]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[3]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[4]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[5]+temp*shiftsteigung-xbondaxis],\
                                               [10000,10,x00+positions[0]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[1]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[2]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[3]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[4]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[5]+temp*shiftsteigung+xbondaxis]))
                INASpos1=np.append(INASpos1,popt[2])
                INASpos2=np.append(INASpos2,popt[5])
                INASpos3=np.append(INASpos3,popt[8])
                INASpos3fel=np.append(INASpos3fel,popt[7])
                INASpos4=np.append(INASpos4,popt[11])
                INASpos5=np.append(INASpos5,popt[14])
                INASpos6=np.append(INASpos6,popt[17])
                
                INASamp1=np.append(INASamp1,popt[0])
                INASamp2=np.append(INASamp2,popt[3])
                INASamp3=np.append(INASamp3,popt[6])
                INASamp4=np.append(INASamp4,popt[9])
                INASamp5=np.append(INASamp5,popt[12])
                INASamp6=np.append(INASamp6,popt[15])
                
                #perr = np.sqrt(np.diag(pcov))
                
                
                axs[0].plot(datax,(datay+temp*20)*scale,'k-', linewidth=3, alpha=0.7)
                axs[0].plot(datax,(func(datax,*popt)+temp*20)*scale,'r-')
                axs[0].plot(datax,(np.zeros_like(datax)+temp*20)*scale,'k--',alpha=0.7)
                axs[0].text(835, ((temp)*20+800)*scale, str(int(temp*0.1))+"K") 



axs[0].plot(INASpos1[1:],(INASamp1[1:]+tempeee[1:]*20)*scale,'o',color='xkcd:nasty green', markersize=msize)               
axs[0].plot(INASpos2[1:],(INASamp2[1:]+tempeee[1:]*20)*scale,'o',color='xkcd:squash', markersize=msize)              
axs[0].plot(INASpos3[1:],(INASamp3[1:]+tempeee[1:]*20)*scale,'o',color='xkcd:baby purple', markersize=msize)              
axs[0].plot(INASpos4[1:],(INASamp4[1:]+tempeee[1:]*20)*scale,'o',color='xkcd:dandelion', markersize=msize)              
axs[0].plot(INASpos5[1:],(INASamp5[1:]+tempeee[1:]*20)*scale,'o',color='xkcd:leather', markersize=msize)             
axs[0].plot(INASpos6[1:],(INASamp6[1:]+tempeee[1:]*20)*scale,'o',color='xkcd:sky blue', markersize=msize)  
           
axs[0].text(980, (38000)*scale, "InAs") 
axs[0].legend(['Messwerte','Gauss-Fit'],loc="upper right")
axs[0].set_xlabel(r'$\lambda$ in nm')
axs[0].set_ylabel(r'Intensität $n$ in $10^3$')
axs[0].grid()
axs[0].set_xlim([825,965])




axs[1].plot(tempeee*0.1,INASamp1*scale,'o',color='xkcd:nasty green', markersize= msize)               
axs[1].plot(tempeee*0.1,INASamp2*scale,'o',color='xkcd:squash', markersize=msize)              
axs[1].plot(tempeee*0.1,INASamp3*scale,'o',color='xkcd:baby purple', markersize=msize)              
axs[1].plot(tempeee*0.1,INASamp4*scale,'o',color='xkcd:dandelion', markersize=msize)              
axs[1].plot(tempeee*0.1,INASamp5*scale,'o',color='xkcd:leather', markersize=msize)             
axs[1].plot(tempeee*0.1,INASamp6*scale,'o',color='xkcd:sky blue', markersize=msize) 

axs[1].set_xlim([0,200]) 
axs[1].set_ylim([0, 8]) 
axs[1].set_xlabel(r'T in K')
axs[1].set_ylabel(r'Intensität $n$ in $10^3$')

axs[1].grid()
alter=np.linspace(0,8,9)
axs[1].set_yticks(alter) 
plt.show


plt.show
plt.savefig("inastemp.pdf", bbox_inches='tight')
'''
'''
fig=plt.figure(figsize=[3, 7])
for  j in range(0,len(tempeee[1:])):
    i=j+1              
    plt.plot(tempeee[i]*0.1,INASpos1[i],'o',color='xkcd:nasty green', markersize=msize)               
    plt.plot(tempeee[i]*0.1,INASpos2[i],'o',color='xkcd:squash', markersize=msize)              
    plt.plot(tempeee[i]*0.1,INASpos3[i],'o',color='xkcd:baby purple', markersize=msize)              
    plt.plot(tempeee[i]*0.1,INASpos4[i],'o',color='xkcd:dandelion', markersize=msize)              
    plt.plot(tempeee[i]*0.1,INASpos5[i],'o',color='xkcd:leather', markersize=msize)             
    plt.plot(tempeee[i]*0.1,INASpos6[i],'o',color='xkcd:sky blue', markersize=msize) 
plt.text(5,890,'f')
plt.text(5,870, 'g')
plt.text(5,908,'d') 
plt.text(5,930,'p') 
plt.text(5,945,'s')     
plt.xlim([0,200]) 
plt.ylim([850, 960]) 
plt.xlabel(r'T in K')
plt.ylabel(r'$\lambda$ in nm')

plt.grid() 
plt.savefig("inastempverlauf.pdf", bbox_inches='tight')

plt.show






figinas2, axs =plt.subplots(1,2,gridspec_kw=dict(wspace=0.3,hspace=0.4))
figinas2.set_figheight(sizey)
figinas2.set_figwidth(sizex)
temp=0

for subdir, dirs, files in os.walk(r'/Users/koppe/Documents/uni/Apversuche/ansirepo/FP/Quantenpunkte/Photolumineszenz_von_Quantenpunkten/Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r") 
        if "InAs" in filepath:
            if filepath.endswith(".asc") and "deg" in filepath:
                #print(filepath.find("mm"))
                deg=int(filepath[filepath.find("deg")-2:filepath.find("deg")])
                deggg=np.append(deggg, deg)
                data = np.genfromtxt(filepath)
                datax=data[:,0]
                datay=data[:,1]
                
                popt, pcov = curve_fit(func, datax, datay, p0=[2000-temp,5,x00+positions[0]+temp*shiftsteigung,2000-temp,5,x00+positions[1]+temp*shiftsteigung,2000-temp,5,x00+positions[2]+temp*shiftsteigung,2000-temp,5,x00+positions[3]+temp*shiftsteigung,2000-temp,5,x00+positions[4]+temp*shiftsteigung,2000-temp,5,x00+positions[5]+temp*shiftsteigung],\
                                       bounds=([0,1,x00+positions[0]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[1]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[2]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[3]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[4]+temp*shiftsteigung-xbondaxis,0,1,x00+positions[5]+temp*shiftsteigung-xbondaxis],\
                                               [10000,10,x00+positions[0]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[1]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[2]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[3]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[4]+temp*shiftsteigung+xbondaxis,10000,10,x00+positions[5]+temp*shiftsteigung+xbondaxis]))
                #perr = np.sqrt(np.diag(pcov))
                INASleipos1=np.append(INASleipos1,popt[2])
                INASleipos2=np.append(INASleipos2,popt[5])
                INASleipos3=np.append(INASleipos3,popt[8])
                INASleipos4=np.append(INASleipos4,popt[11])
                INASleipos5=np.append(INASleipos5,popt[14])
                INASleipos6=np.append(INASleipos6,popt[17])
                
                INASleiamp1=np.append(INASleiamp1,popt[0])
                INASleiamp2=np.append(INASleiamp2,popt[3])
                INASleiamp3=np.append(INASleiamp3,popt[6])
                INASleiamp4=np.append(INASleiamp4,popt[9])
                INASleiamp5=np.append(INASleiamp5,popt[12])
                INASleiamp6=np.append(INASleiamp6,popt[15])
                
                
                axs[0].plot(datax,(datay+deg*200)*scale,'k-', linewidth=3, alpha=0.7)
                axs[0].plot(datax,(func(datax,*popt)+deg*200)*scale,'r-')
                axs[0].plot(datax,(np.zeros_like(datax)+deg*200)*scale,'k--',alpha=0.7)
                
                if deg< 21:
                    axs[0].text(805, (deg*200+300)*scale, '{:3.2f}'.format(y_interp(deg))+"mW") 
                else:
                    axs[0].text(805, (deg*200+800)*scale, '{:3.2f}'.format(y_interp(deg))+"mW") 



axs[0].plot(INASleipos1[1:],(INASleiamp1[1:]+deggg[1:]*200)*scale,'o',color='xkcd:nasty green', markersize=msize)               
axs[0].plot(INASleipos2[1:],(INASleiamp2[1:]+deggg[1:]*200)*scale,'o',color='xkcd:squash', markersize=msize)              
axs[0].plot(INASleipos3[1:],(INASleiamp3[1:]+deggg[1:]*200)*scale,'o',color='xkcd:baby purple', markersize=msize)              
axs[0].plot(INASleipos4[1:],(INASleiamp4[1:]+deggg[1:]*200)*scale,'o',color='xkcd:dandelion', markersize=msize)              
axs[0].plot(INASleipos5[1:],(INASleiamp5[1:]+deggg[1:]*200)*scale,'o',color='xkcd:leather', markersize=msize)             
axs[0].plot(INASleipos6[1:],(INASleiamp6[1:]+deggg[1:]*200)*scale,'o',color='xkcd:sky blue', markersize=msize) 
axs[0].text(885, -1, 'f')
axs[0].text(900, -1, 'd') 
axs[0].text(920, -1, 'p') 
axs[0].text(940, -1, 's') 
axs[0].text(865, -1, 'g')
 
                
axs[0].text(970, (25000)*scale, "InAs") 
axs[0].grid()
axs[0].set_xlim([800,965])
axs[0].legend(['Messwerte','Gauss-Fit'],loc="upper left")
axs[0].set_xlabel(r'$\lambda$ in nm')
axs[0].set_ylabel(r'Intensität $n$ in $10^3$')



axs[1].plot(y_interp(deggg),INASleiamp1*scale,'o',color='xkcd:nasty green', markersize= msize)               
axs[1].plot(y_interp(deggg),INASleiamp2*scale,'o',color='xkcd:squash', markersize=msize)              
axs[1].plot(y_interp(deggg),INASleiamp3*scale,'o',color='xkcd:baby purple', markersize=msize)              
axs[1].plot(y_interp(deggg),INASleiamp4*scale,'o',color='xkcd:dandelion', markersize=msize)              
axs[1].plot(y_interp(deggg),INASleiamp5*scale,'o',color='xkcd:leather', markersize=msize)             
axs[1].plot(y_interp(deggg),INASleiamp6*scale,'o',color='xkcd:sky blue', markersize=msize) 

#axs[1].set_xlim([-20,130]) 
axs[1].set_ylim([0, 8]) 
axs[1].set_xlabel(r'Anregungsleistung $P_{L}$ in mW')
axs[1].set_ylabel(r'Intensität $n$ in $10^3$')

axs[1].grid()
alter=np.linspace(0,8,9)
axs[1].set_yticks(alter) 
plt.show
plt.savefig("inaslei.pdf", bbox_inches='tight') 

#############################################################################################InP
tempeee=np.array(0)
deggg=np.array(0)


xlimm=1300
yscaling=0.001
figinp1spezial = plt.figure(figsize=(sizex,sizey)) 
for subdir, dirs, files in os.walk(r'/Users/koppe/Documents/uni/Apversuche/ansirepo/FP/Quantenpunkte/Photolumineszenz_von_Quantenpunkten/Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")                
        if "InP" in filepath:
            if filepath.endswith(".asc") and "temp" in filepath:
                #print(filepath.find("mm"))
                temp=int(filepath[filepath.find("temp")+4:filepath.find("temp")+8])
                if temp==37:
                    data = np.genfromtxt(filepath)
                    datax=data[:,0]
                    datay=data[:,1]
                    plt.plot(datax[:xlimm],datay[:xlimm]*yscaling,'k.', linewidth=3, alpha=0.7)
                    plt.plot(datax[:xlimm],np.zeros_like(datax[:xlimm])*yscaling,'b--',alpha=0.7)
                     
                    


plt.text(820, 17500*yscaling, "InP")   
plt.grid() 
plt.xlabel(r'$\lambda$ in nm')
plt.ylabel(r'Intensität $n$ in $10^3$')          
#plt.plot(x00+positions[5]+tempeee*shiftsteigung,tempeee*20) 
plt.show  
plt.savefig("inP.pdf", bbox_inches='tight')






INPamptemp=np.array(0)
INPpostemp=np.array(0)





figinptemp, axs =plt.subplots(1,4,gridspec_kw=dict(wspace=0.3,hspace=0.4))
figinptemp.set_figheight(sizey-1)
figinptemp.set_figwidth(sizex+2) 
axs[0] = plt.subplot2grid((1, 4), (0, 0), colspan=2)      

for subdir, dirs, files in os.walk(r'/Users/koppe/Documents/uni/Apversuche/ansirepo/FP/Quantenpunkte/Photolumineszenz_von_Quantenpunkten/Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")                
        if "InP" in filepath:
            if filepath.endswith(".asc") and "temp" in filepath:
                #print(filepath.find("mm"))
                temp=int(filepath[filepath.find("temp")+4:filepath.find("temp")+8])
                tempeee=np.append(tempeee,temp)
                data = np.genfromtxt(filepath)
                datax=data[:,0]
                datay=data[:,1]
                   #def funcone(x,a,b,c): return a*np.exp(-((x-c)/b)**2)
    
                popt, pcov = curve_fit(funcone, datax[:700], datay[:700], p0=[2000,10,760],bounds=([0,4,740],[5000,30,775]))
                INPamptemp=np.append(INPamptemp,popt[0])
                INPpostemp=np.append(INPpostemp,popt[2])
                
                #perr = np.sqrt(np.diag(pcov))
                print(popt[1])
                axs[0].plot(datax[:xlimm],datay[:xlimm]*yscaling+np.sqrt(temp)*200*yscaling,'k.', linewidth=3, alpha=0.7)
                axs[0].plot(datax[:700],funcone(datax[:700],*popt)*yscaling+np.sqrt(temp)*200*yscaling,'r-')
                axs[0].plot(datax[:xlimm],np.zeros_like(datax[:xlimm])*yscaling+np.sqrt(temp)*200*yscaling,'b--',alpha=0.7)
                axs[0].text(732, np.sqrt(temp)*200*yscaling+200*yscaling, str(int(temp*0.1))+"K")
                axs[0].plot(popt[2],funcone(popt[2],*popt)*yscaling+np.sqrt(temp)*200*yscaling,'o',color='xkcd:nasty green', markersize= msize)
                
                
                    

             
 
axs[0].text(765, 9500*yscaling, "InP")   
axs[0].grid() 
axs[0].set_xlabel(r'$\lambda$ in nm')
axs[0].set_ylabel(r'Intensität $n$ in $10^3$')  
axs[0].set_xlim([730, 780])
axs[0].set_ylim([1, 10])          
#plt.plot(x00+positions[5]+tempeee*shiftsteigung,tempeee*20) 
axs[1] = plt.subplot2grid((1, 4), (0, 2))

axs[1].plot(tempeee*0.1,INPamptemp*scale,'o',color='xkcd:nasty green', markersize= msize)               


axs[1].set_xlim([0,200]) 
axs[1].set_ylim([0, 1.5]) 
axs[1].set_xlabel(r'T in K')
axs[1].set_ylabel(r'Intensität $n$ in $10^3$')

axs[1].grid()



axs[2] = plt.subplot2grid((1, 4), (0, 3))
axs[2].plot(tempeee*0.1,INPpostemp,'o',color='xkcd:nasty green', markersize= msize)               


axs[2].set_xlim([0,200]) 
axs[2].set_ylim([700, 800]) 
axs[2].set_xlabel(r'T in K')
axs[2].set_ylabel(r'$\lambda$ in nm')

axs[2].grid()





plt.tight_layout()
plt.show  
plt.savefig("inptemp.pdf", bbox_inches='tight')

xlimm=1450



INPamplei=np.array(0)



 
figinplei, axs =plt.subplots(1,2,gridspec_kw=dict(wspace=0.3,hspace=0.4))
figinplei.set_figheight(sizey)
figinplei.set_figwidth(sizex)         

for subdir, dirs, files in os.walk(r'/Users/koppe/Documents/uni/Apversuche/ansirepo/FP/Quantenpunkte/Photolumineszenz_von_Quantenpunkten/Messwerte'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        filenames = open(filepath,"r")                
        if "InP" in filepath:
            if filepath.endswith(".asc") and "deg" in filepath:
                #print(filepath.find("mm"))
                deg=int(filepath[filepath.find("deg")-2:filepath.find("deg")])
                deggg=np.append(deggg, deg)
                data = np.genfromtxt(filepath)
                datax=data[:,0]
                datay=data[:,1]
                
                popt, pcov = curve_fit(funcone, datax[:700], datay[:700], p0=[2000,10,760],bounds=([0,4,740],[5000,30,775]))
                INPamplei=np.append(INPamplei,popt[0])
                #perr = np.sqrt(np.diag(pcov))

                axs[0].plot(datax[:xlimm],datay[:xlimm]*yscaling+deg*50*yscaling,'k.', linewidth=3,alpha=0.7)
                axs[0].plot(datax[:700],funcone(datax[:700],*popt)*yscaling+deg*50*yscaling,'r-')
                axs[0].plot(popt[2],funcone(popt[2],*popt)*yscaling+deg*50*yscaling,'o',color='xkcd:nasty green', markersize= msize)
                axs[0].plot(datax[:xlimm],np.zeros_like(datax[:xlimm])*yscaling+deg*50*yscaling,'b--',alpha=0.7)
                if deg>19:
                    axs[0].text(732, deg*50*yscaling+150*yscaling, '{:3.2f}'.format(y_interp(deg))+"mW") 
                else:
                    axs[0].text(732, deg*50*yscaling+40*yscaling, '{:3.2f}'.format(y_interp(deg))+"mW") 
                

                

axs[0].text(765, 6000*yscaling, "InP") 
axs[0].grid()
axs[0].set_xlabel(r'$\lambda$ in nm')
axs[0].set_ylabel(r'Intensität $n$ in $10^3$')
axs[0].set_ylim([-0.2, 7]) 
axs[0].set_xlim([730, 770])  
#plt.plot(x00+positions[5]+tempeee*shiftsteigung,tempeee*20) 


axs[1].plot(y_interp(deggg),INPamplei*scale,'o',color='xkcd:nasty green', markersize= msize)               


#axs[1].set_xlim([-20,130]) 
axs[1].set_ylim([0, 8]) 
axs[1].set_xlabel(r'Anregungsleistung $P_{L}$ in mW')
axs[1].set_ylabel(r'Intensität $n$ in $10^3$')

axs[1].grid()
alter=np.linspace(0,8,9)
axs[1].set_yticks(alter) 







plt.show               
plt.savefig("inplei.pdf", bbox_inches='tight')
 
    
''' 
fig2, axs =plt.subplots(3,2,gridspec_kw=dict(wspace=0.4,hspace=0.4),)


fig2.set_figheight(6)
fig2.set_figwidth(6)
axs[0,0].plot(1,1,'r') 
axs[0,0].set_frame_on(False)
axs[0,0].set_xticks([])
axs[0,0].set_yticks([])
axs[0,0].set_title('helium',y=0.5)
#plt.figure(figsize=(sizex,sizey))        
axs[0,1].errorbar(pressureeehelium[1:],Teeehelium[1:]*10**(-3),yerr=Teeeheliumerr[1:]*10**(-3),xerr=pressureeehelium[1:]*0.1,ls='')
axs[0,1].grid()
axs[0,1].set_xlabel(r'$p$ in mbar')
axs[0,1].set_ylabel(r' $T$ in $10^3\,$K')
axs[0,1].set_ylim([0,1800])
#plt.xlim([-60, 60])
#plt.ylim([0, 1.5])
#plt.savefig("dat2.pdf", bbox_inches='tight')
 
#plt.figure(figsize=(sizex,sizey))  
axs[1,0].errorbar(pressureeehelium[1:],neeehelium[1:]*10**(-15),yerr=neeeheliumerr[1:]*10**(-15),xerr=pressureeehelium[1:]*0.1,ls='')
axs[1,0].grid()
axs[1,0].set_xlabel(r'$p$ in mbar')
axs[1,0].set_ylabel(r' $n$ in $10^{15}\,$m$^3$')
axs[1,0].set_ylim([1,5])
#plt.xlim([-60, 60])
#plt.ylim([0, 1.5])
#plt.savefig("dat2.pdf", bbox_inches='tight')

axs[1,1].errorbar(pressureeehelium[1:],deblenhelium*10**(3),yerr=deblenheliumerr*10**(3),xerr=pressureeehelium[1:]*0.1,ls='')
axs[1,1].grid()
axs[1,1].set_xlabel(r'$p$ in mbar')
axs[1,1].set_ylabel(r' $\lambda_\mathrm{D}$ in $\mu m$')
axs[1,1].set_ylim([0,3])
#plt.xlim([-60, 60])
#plt.ylim([0, 1.5])
#plt.savefig("dat2.pdf", bbox_inches='tight')
 
#plt.figure(figsize=(sizex,sizey))  
axs[2,0].errorbar(pressureeehelium[1:],omegaphelium*10**(-9),yerr=omegapheliumerr*10**(-9),xerr=pressureeehelium[1:]*0.1,ls='')
axs[2,0].grid()
axs[2,0].set_xlabel(r'$p$ in mbar')
axs[2,0].set_ylabel(r' $\omega_\mathrm{P}$ in GHz')
axs[2,0].set_ylim([1,5])
#plt.xlim([-60, 60])
#plt.ylim([0, 1.5])
#plt.savefig("dat2.pdf", bbox_inches='tight')

axs[2,1].errorbar(pressureeehelium[1:],iondeghelium*10**(9),yerr=iondegheliumerr*10**(9),xerr=pressureeehelium[1:]*0.1,ls='')
axs[2,1].grid()
axs[2,1].set_xlabel(r'$p$ in mbar')
axs[2,1].set_ylabel(r' $\alpha$ in $10^{-9}$')
axs[2,1].set_ylim([0,700])
#plt.xlim([-60, 60])
#plt.ylim([0, 1.5])
plt.savefig("Teil3helium.pdf", bbox_inches='tight')
 

plt.show()              
'''