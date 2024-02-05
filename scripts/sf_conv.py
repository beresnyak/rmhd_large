#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sf import read_sf
from read_sp import eta_index,resol

# Convergence study with 2nd order SF

ppoint=['r-','g-','b-']*2
plegend=['1024^3','2048^3','4096^3']*2
xlim1=[.3,1e3]

def plot_prepare(ind,ymin):
    plt.figure(ind)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylim([ymin,ymin*20])
    plt.xlim(xlim1)
    plt.axes().set_aspect('equal')
    plt.xlabel('r/eta')
    plt.title('second order sf, n=2')



plot_prepare(1,2)
eta=eta_index(-5.0/3)
print eta, eta*resol/3.
plt.ylabel('SF*r^-2/3')

i1=3 # normal diff

for j in range(i1,i1+3):   
    (rr,sf)=read_sf(j)
    plt.plot(rr/eta[j],sf*rr**(-2.0/3),ppoint[j],label=plegend[j])

plt.plot(xlim1,[10,10],'k-')
plt.legend(loc='upper left')    

plot_prepare(0,1.)
eta=eta_index(-1.5)
print eta, eta*resol/3.
plt.ylabel('SF*r^-1/2')

for j in range(i1,i1+3):   
    (rr,sf)=read_sf(j)
    plt.plot(rr/eta[j],sf*rr**(-0.5),ppoint[j],label=plegend[j])

plt.plot(xlim1,[5,5],'k-')
plt.legend(loc='upper left')    


plt.show()            

   
