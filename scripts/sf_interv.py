#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sf import read_sf
          
# find maximum interval of the spectrum sp
def max_interval_sf(rr,sf,ind,rel_error):       
   sp=sf*rr**(-ind)  # compensate by k^-ind
   interv=[]    # all intervals 
   for k in range(1,sp.size-2):
     kmin=k
     kmax=k
     while ((abs(np.log(sp[kmin]/sp[k]))<rel_error) and kmin>1): kmin-=1
     kmin+=1
     while ((abs(np.log(sp[kmax]/sp[k]))<rel_error) and kmax<sp.size-1): kmax+=1
     kmax-=1
     interv.append(rr[kmax]/rr[kmin])
   return max(interv)

err=0.025

h53=[];h15=[];
for j in range(0,3):   
    (rr,sf)=read_sf(j)
    h53.append(max_interval_sf(rr,sf,0.667,err))
    h15.append(max_interval_sf(rr,sf,0.500,err))    

n53=[];n15=[];
for j in range(3,6):
    (rr,sf)=read_sf(j)
    n53.append(max_interval_sf(rr,sf,0.667,err))
    n15.append(max_interval_sf(rr,sf,0.500,err))    
      

xx1=np.array([1024.,2048.,4096.])
xx=[1024.,2048.,4096.]
 
plt.figure(0)
plt.yscale('log')
plt.xscale('log')
plt.xlim([700,5000])
plt.xlabel('cube size')
plt.ylabel('largest length of continuous scaling with deviation %.2f'%(err*2))
plt.title('based on 2nd order structure function')

plt.plot(xx,h53,'go-',label='5/3 4th order')
plt.plot(xx,n53,'gs--',label='5/3 2nd order')
plt.plot(xx,h15,'ro-',label='3/2 4th order')
plt.plot(xx,n15,'rs--',label='3/2 2nd order')
plt.plot(xx1,2*xx1/1000,"b-")
plt.plot(xx1,2*(xx1/1000)**(8.0/9),"b-",label='theory')
plt.legend(loc='lower right')    

plt.show()            

   
