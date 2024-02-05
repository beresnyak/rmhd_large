#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sf import read_sf

#plot 2nd order SFs compensated by r*-0.58

plt.figure(0)

(kk,sp)=read_sf(0)
plt.plot(kk,sp*kk**-.58,'r-',label='1024^3')

(kk,sp)=read_sf(1)
plt.plot(kk,sp*kk**-.58,'g-',label='2048^3')

(kk,sp)=read_sf(2)
plt.plot(kk,sp*kk**-.58,'b-',label='4096^3')

plt.plot(kk,12*kk**0.087,'y--',label='r^+0.087')
plt.plot(kk,12*kk**0.00,'y-')
plt.plot(kk,12*kk**-0.08,'y-.',label='r^-0.08')


plt.legend(loc='lower right')    


plt.yscale('log')
plt.xscale('log')
#plt.xlim([1,20])
plt.ylim([1,1e2])
plt.xlabel('r')
plt.ylabel('SF(r)*r^-.58')

plt.figure(1)

(kk,sp)=read_sf(3)
plt.plot(kk,sp*kk**-.58,'r-',label='1024^3')

(kk,sp)=read_sf(4)
plt.plot(kk,sp*kk**-.58,'g-',label='2048^3')

(kk,sp)=read_sf(5)
plt.plot(kk,sp*kk**-.58,'b-',label='4096^3')

plt.plot(kk,12*kk**0.087,'y--',label='r^+0.087')
plt.plot(kk,12*kk**0.00,'y-')
plt.plot(kk,12*kk**-0.08,'y-.',label='r^-0.08')


plt.legend(loc='lower right')    


plt.yscale('log')
plt.xscale('log')
#plt.xlim([1,20])
plt.ylim([1,1e2])
plt.xlabel('r')
plt.ylabel('SF(r)*r^-.58')



plt.show()            
   
