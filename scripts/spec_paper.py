#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sp import read_spvb,eta_index,coeff

# This reproduces all 6 plots from ApJ 784:L20

ppoint=['r-','g-','b-']*2
plegend=['1024^3','2048^3','4096^3']*2

def plot_prepare(ind,ymin):
    plt.figure(ind)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylim([ymin,ymin*12])
    plt.xlim([2e-4,1.0])
    plt.axes().set_aspect('equal')

# plot energy spectrum in dimensionless units corresponding to k^index theory
# from directories in the range [i1,i2]; sign=1-- total energy sign=-1 residual energy
def plot_bunch(i1,i2,index,sign):
    eta=eta_index(index)
    for j in range(i1,i2):   
        (kk,spv,spb)=read_spvb(j)
        plt.plot(kk*eta[j],0.5*coeff*(spb+sign*spv)*kk**(-index),ppoint[j],label=plegend[j])
    plt.legend(loc='upper left')    

    
plot_prepare(0,0.4)
plt.title('total energy, -5/3 scaling, n=4')
plot_bunch(0,3,-5./3,1)
plot_prepare(1,0.4)
plt.title('total energy, -5/3 scaling, n=2')
plot_bunch(3,6,-5./3,1)

plot_prepare(2,0.4)
plt.title('total energy, -1.5 scaling, n=4')
plot_bunch(0,3,-1.5,1)
plot_prepare(3,0.4)
plt.title('total energy, -1.5 scaling, n=2')
plot_bunch(3,6,-1.5,1)

plot_prepare(4,0.1)
plt.title('residual energy, -1.7 scaling, n=4')
plot_bunch(0,3,-1.7,-1)
plot_prepare(5,0.1)
plt.title('residual energy, -1.7 scaling, n=2')
plot_bunch(3,6,-1.7,-1)


plt.show()            


