#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sp import read_sp,spectrum_convert

plt.figure(0)
#plt.yscale('log')
plt.xscale('log')
plt.ylim([1.2,2.0])
plt.xlim([1,1000.0])

#plt.xlabel('cube size')
#plt.ylabel('largest length of continuous scaling with deviation %.2f'%(err*2))
#plt.title('based on 3d spectrum')

ppoint=['ro-','go-','bo-']*2
plegend=['1024^3','2048^3','4096^3']*2

i=0 #i=3 normal diff, i=0 4th order diff
sp_type="1d" # or 3d or par
  
for j in range(i,i+3):   
#for j in range(0,6):   
    (kk,sp)=read_sp(j)
    (sp1,sp_par)=spectrum_convert(kk,sp)
    if sp_type=="1d": sp=sp1
    if sp_type=="par": sp=sp_par
    slope=np.full(kk.size,np.nan)
    for i in range(1,kk.size-2):
        slope[i]=-np.log(sp[i+1]/sp[i])/np.log(kk[i+1]/kk[i])
    plt.plot(kk+0.5,slope,ppoint[j],label=plegend[j])


plt.legend(loc='upper right')    
#plt.plot(ll[0],'r-',ll[1],'g-',ll[2],'b-', )

#plt.figure(1)


plt.show()            

#   k*=eta[j]
#   sp=sp0*coeff*0.5*k**ind
#   plt.plot(k_interp,ev_interp,"b-",k_interp,ev_interp,"r-")

#plt.plot(kval[0],spval[0],"b-",kval[1],spval[1],"g-",kval[2],spval[2],"r-")
#plt.yscale('log')
#plt.xscale('log')
#plt.show()
    
