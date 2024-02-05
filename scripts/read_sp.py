#!/usr/bin/python
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange

dir='../'
#ndirs=6
dirs=['b1024h','b2048h','b4096h','b1024n','b2048n','b4096n']
resol=np.array([1024,2048,4096,1024,2048,4096])
order=np.array([4,4,4,2,2,2]) #np.array([4]*3+[2]*3)
nu=np.array([1.6E-9,1.6E-10,1.6E-11,1.75E-4,7E-5,2.78E-5])
eps=0.06
#alpha=-0.05 # corresponds to slope of -1.7 slope=-5/3+2/3*alpha
#eta=((nu**3.0)/eps)**(1.0/(3.*order-2+2.*alpha))
#alpha=0.25 # corresponds to slope of -1.5
#eta_b=((nu**3.0)/eps)**(1.0/(3.*order-2+2.*alpha))
coeff=eps**(-2.0/3)

# returns an array of dissipation scales eta from array of nu, eps
# and as a function of spectral index
def eta_index(index):
    return ((nu**3.0)/eps)**(1.0/3./(order+index+1))

# converts 3d spectrum into 1d spectrum and 1d parallel spectrum
#        p1(k) = \int_k^inf p(x) dx/x
#    p1_par(k) = \int_k^inf p(x) (1-k^2/x^2) dx/x
# uses trapezoid in log-space, fails at spectral indexes of 0 and 2
def spectrum_convert(kk,sp):
    sp1=zeros(sp.size)
    sp_par=zeros(sp.size)
    for i in range(sp.size-2,0,-1):
        alpha=np.log(sp[i+1]/sp[i])/np.log(kk[i+1]/kk[i])
        sp1[i]=sp1[i+1]+(sp[i+1]-sp[i])/alpha
        sp_par[i]=sp_par[i+1]+(sp[i+1]/kk[i+1]**2-sp[i]/kk[i]**2)/(alpha-2.)
    for i in range(1, sp.size-1):
        sp_par[i]=sp1[i]-sp_par[i]*kk[i]**2        
    return (sp1,sp_par)    
        
# reads 3d total energy spectrum from file, based on index j
# returns array of wavenumbers kk and array of spectrum sp 
def read_sp(j):
   a=loadtxt(dir+dirs[j]+'/avr_spec.txt',comments='#')
   kk=a[:,0]
   sp=a[:,1]+a[:,2]
   return (kk,sp)
                    
# reads 3d total energy spectrum from file, based on index j
# returns array of wavenumbers kk and array of spectrum sp 
def read_spvb(j):
   a=loadtxt(dir+dirs[j]+'/avr_spec.txt',comments='#')
   kk=a[:,0]
   spv=a[:,1]
   spb=a[:,2]
   return (kk,spv,spb)
          

