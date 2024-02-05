#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sp import read_sp
          
kmh=[];kmn=[];
emh=[];emn=[];
for j in range(0,3):   
    (kk,sp)=read_sp(j)
    kmax=np.argmax(sp*kk**3)
    kmh.append(kmax)
    emh.append(sp[kmax])    

for j in range(3,6):
    (kk,sp)=read_sp(j)
    kmax=np.argmax(sp*kk**3)
    kmn.append(kmax)
    emn.append(sp[kmax])    
    
xx=[1024.,2048.,4096.]
xx1=np.array(xx)

plt.figure(0)
plt.yscale('log')
plt.xscale('log')
plt.xlim([700,5000])
plt.ylim([70,800])

#order=np.array([4,4,4,2,2,2])
#nu=np.array([1.6E-9,1.6E-10,1.6E-11,1.75E-4,7E-5,2.78E-5])

nu_h=np.array([1.6E-9,1.6E-10,1.6E-11])
nu_n=np.array([1.75E-4,7E-5,2.78E-5])

# Kolmogorov scale for theory with scaling v~l^a (e.g. a=1/3 for classic)
def eta(n,eps,nu,a):
    return ((nu**3.)/eps)**(1./3./(n-2.*a))
    
# Kolmogorov velocity    
def v_eta(n,eps,nu,a,L):
    ind=n-2.*a
    return eps**((n-3*a)/3/ind)*nu**(a/ind)*L**(1./3-a)    


plt.xlabel('cube size')
plt.ylabel('k at maximum of E(k)*k^3')

plt.plot(xx,kmh,'go',label='4th order')
plt.plot(xx,kmn,'gs',label='2nd order')

#plt.plot(xx1,178*xx1/1000,"y-",label='5/3 theory')
#plt.plot(xx1,178*(xx1/1000)**(8.0/9),"y--",label='3/2 theory')

plt.plot(xx1,0.26/eta(2.0,0.06,nu_n,1.0/3),"y-",label='5/3 theory')
plt.plot(xx1,0.49/eta(2.0,0.06,nu_n,1.0/4),"y--",label='3/2 theory')

plt.plot(xx1,0.56/eta(4.0,0.06,nu_h,1.0/3),"y-")
plt.plot(xx1,0.72/eta(4.0,0.06,nu_h,1.0/4),"y--")
plt.legend(loc='lower right')    

plt.figure(1)
plt.yscale('log')
plt.xscale('log')
plt.xlim([700,5000])
plt.ylim([1e-5,5e-4])

plt.xlabel('cube size')
plt.ylabel('E(k) at maximum of E(k)*k^3')

plt.plot(xx,emh,'go',label='4th order')
plt.plot(xx,emn,'gs',label='2nd order')

#plt.plot(xx1,20*xx1**(-5.0/3),"y-",label='5/3 theory')

plt.plot(xx1,4.1*eta(2.0,0.06,nu_n,1.0/3)**(5./3),"y-",label='5/3 theory')
plt.plot(xx1,.6*eta(2.0,0.06,nu_n,1.0/4)**(3./2),"y--",label='3/2 theory')

plt.plot(xx1,1.95*eta(4.0,0.06,nu_h,1.0/3)**(5./3),"y-")
plt.plot(xx1,.5*eta(4.0,0.06,nu_h,1.0/4)**(3./2),"y--")

plt.legend(loc='upper right')    



plt.show()            
    
