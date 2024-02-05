#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sf import read_sf
from read_sp import eta_index,resol

plt.figure(0)
#plt.yscale('log')
plt.xscale('log')
xlim1=[4e-3,4e-1]
plt.ylim([0.2,0.9])
plt.xlim(xlim1)

plt.xlabel('r')

ppoint=['ro-','go-','bo-']*2
plegend=['1024^3','2048^3','4096^3']*2

for j in range(3,6):   
    (rr,sf)=read_sf(j)
    slope=np.full(rr.size,np.nan)
    for i in range(1,rr.size-1):
        slope[i]=np.log(sf[i+1]/sf[i])/np.log(rr[i+1]/rr[i])
    plt.plot(rr,slope,ppoint[j],label=plegend[j])

plt.legend(loc='upper right')    
plt.plot(xlim1,[2.0/3]*2,'k-')
plt.plot(xlim1,[0.5]*2,'k-')
plt.title('second order sf slope, n=2')

plt.show()            

   
