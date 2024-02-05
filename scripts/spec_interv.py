#!/usr/bin/python
import sys
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange
import matplotlib.pyplot as plt
from read_sp import read_sp,spectrum_convert
          
# find maximum interval of the spectrum sp
def max_interval(kk,s,ind,rel_error):       
   sp=s*kk**ind  # compensate by k^ind
   interv=[]    # all intervals 
   for k in range(1,sp.size-2):
     kmin=k
     kmax=k
     while ((abs(np.log(sp[kmin]/sp[k]))<rel_error) and kmin>1): kmin-=1
     kmin+=1
     while ((abs(np.log(sp[kmax]/sp[k]))<rel_error) and kmax<sp.size-1): kmax+=1
     kmax-=1
     interv.append((1.0*kmax)/kmin)
   return max(interv)

err=0.025

h53=[];h15=[];h53_1=[];h53_p=[];h15_1=[];h15_p=[];
for j in range(0,3):   
    (kk,sp)=read_sp(j)
    h53.append(max_interval(kk,sp,5.0/3,err))
    h15.append(max_interval(kk,sp,1.5,err))
    (sp1,sp2)=spectrum_convert(kk,sp)
    h53_1.append(max_interval(kk,sp1,5.0/3,err))
    h15_1.append(max_interval(kk,sp1,1.5,err))
    h53_p.append(max_interval(kk,sp2,5.0/3,err))
    h15_p.append(max_interval(kk,sp2,1.5,err))
    

n53=[];n15=[];n53_1=[];n53_p=[];n15_1=[];n15_p=[];
for j in range(3,6):
    (kk,sp)=read_sp(j)   
    n53.append(max_interval(kk,sp,5.0/3,err))
    n15.append(max_interval(kk,sp,1.5,err))
    (sp1,sp2)=spectrum_convert(kk,sp)
    n53_1.append(max_interval(kk,sp1,5.0/3,err))
    n15_1.append(max_interval(kk,sp1,1.5,err))
    n53_p.append(max_interval(kk,sp2,5.0/3,err))
    n15_p.append(max_interval(kk,sp2,1.5,err))
      

xx1=np.array([1024.,2048.,4096.])
xx=[1024.,2048.,4096.]
 
plt.figure(0)
plt.yscale('log')
plt.xscale('log')
plt.xlim([700,5000])
plt.xlabel('cube size')
plt.ylabel('largest length of continuous scaling with deviation %.2f'%(err*2))
plt.title('based on 3d spectrum')


plt.plot(xx,h53,'go-',label='5/3 4th order')
plt.plot(xx,n53,'gs--',label='5/3 2nd order')
plt.plot(xx,h15,'ro-',label='3/2 4th order')
plt.plot(xx,n15,'rs--',label='3/2 2nd order')
plt.plot(xx1,2*xx1/1000,"b-")
plt.plot(xx1,2*(xx1/1000)**(8.0/9),"b-",label='theory')
plt.legend(loc='lower right')    
#plt.plot(ll[0],'r-',ll[1],'g-',ll[2],'b-', )

plt.figure(1)
plt.yscale('log')
plt.xscale('log')
plt.xlim([700,5000])
plt.xlabel('cube size')
plt.ylabel('largest length of continuous scaling with deviation %.2f'%(err*2))
plt.title('based on 1d spectrum')

plt.plot(xx,h53_1,'go-',label='5/3 4th order')
plt.plot(xx,n53_1,'gs--',label='5/3 2nd order')
plt.plot(xx,h15_1,'ro-',label='3/2 4th order')
plt.plot(xx,n15_1,'rs--',label='3/2 2nd order')
plt.plot(xx1,2*xx1/1000,"b-")
plt.plot(xx1,2*(xx1/1000)**(8.0/9),"b-",label='theory')

plt.legend(loc='lower right')    

plt.figure(2)
plt.yscale('log')
plt.xscale('log')
plt.xlim([700,5000])
plt.xlabel('cube size')
plt.ylabel('largest length of continuous scaling with deviation %.2f'%(err*2))
plt.title('based on 1d parallel spectrum')

plt.plot(xx,h53_p,'go-',label='5/3 4th order')
plt.plot(xx,n53_p,'gs--',label='5/3 2nd order')
plt.plot(xx,h15_p,'ro-',label='3/2 4th order')
plt.plot(xx,n15_p,'rs--',label='3/2 2nd order')
plt.plot(xx1,2*xx1/1000,"b-")
plt.plot(xx1,2*(xx1/1000)**(8.0/9),"b-",label='theory')

plt.legend(loc='lower right')    



plt.show()            

#   k*=eta[j]
#   sp=sp0*coeff*0.5*k**ind
#   plt.plot(k_interp,ev_interp,"b-",k_interp,ev_interp,"r-")

#plt.plot(kval[0],spval[0],"b-",kval[1],spval[1],"g-",kval[2],spval[2],"r-")
#plt.yscale('log')
#plt.xscale('log')
#plt.show()
    
