#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sp import read_sp,spectrum_convert

#just plot some spectra

#resol=np.array([1024,2048,4096,1024,2048,4096])
#order=np.array([4,4,4,2,2,2])
#nu=np.array([1.6E-9,1.6E-10,1.6E-11,1.75E-4,7E-5,2.78E-5])
#eps=0.06
#alpha=0.25
#eta=((nu**3.0)/eps)**(1.0/(3.*order-2+2.*alpha))
#alpha=0.25
#eta_b=((nu**3.0)/eps)**(1.0/(3.*order-2+2.*alpha))

#ind=5.0/3
#ind=1.5
#coeff=eps**(-2.0/3)

#fig, ax = plt.subplots()

(kk,sp)=read_sp(0)
plt.plot(kk,sp*kk**1.5,'r-',label='1024^3')

(kk,sp)=read_sp(1)
plt.plot(kk,sp*kk**1.5,'g-',label='2048^3')

(kk,sp)=read_sp(2)
plt.plot(kk,sp*kk**1.5,'b-',label='4096^3')
plt.legend(loc='lower right')    


(kk,sp)=read_sp(0)
(sp1,sp2)=spectrum_convert(kk,sp)
plt.plot(kk,sp1*kk**1.5,'r-')#,label='1024 1d')
plt.plot(kk,sp2*kk**1.5,'r-')#,label='1024 1d par')

(kk,sp)=read_sp(1)
(sp1,sp2)=spectrum_convert(kk,sp)
plt.plot(kk,sp1*kk**1.5,'g-')#,label='2048 1d')
plt.plot(kk,sp2*kk**1.5,'g-')#,label='2048 1d par')

(kk,sp)=read_sp(2)
(sp1,sp2)=spectrum_convert(kk,sp)
plt.plot(kk,sp1*kk**1.5,'b-')#,label='4096 1d')
plt.plot(kk,sp2*kk**1.5,'b-')#,label='4096 1d par')

plt.annotate('P_par1d',xy=(10.,0.16))
plt.annotate('P_1d',xy=(10.,0.4))
plt.annotate('P_3d',xy=(10.,0.7))
plt.title('three types of spectra')

plt.yscale('log')
plt.xscale('log')
plt.xlim([1,1024])
plt.ylim([.1,1])
plt.xlabel('k')
plt.ylabel('P(k)*k^1.5')
plt.show()            
   
