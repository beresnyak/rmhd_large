#!/usr/bin/python
import numpy as np
from numpy import loadtxt,mean,ones,zeros,std,arange

dir='../'
#ndirs=6
dirs=['b1024h','b2048h','b4096h','b1024n','b2048n','b4096n']
resol=np.array([1024,2048,4096,1024,2048,4096])
#order=np.array([4,4,4,2,2,2])
#nu=np.array([1.6E-9,1.6E-10,1.6E-11,1.75E-4,7E-5,2.78E-5])
#eps=0.06
#alpha=0.0
#eta=((nu**3.0)/eps)**(1.0/(3.*order-2+2.*alpha))
#alpha=0.25
#eta_b=((nu**3.0)/eps)**(1.0/(3.*order-2+2.*alpha))
#coeff=eps**(-2.0/3)

        
def read_sf(j):
    nrecord=0
    while True:
       try: a=loadtxt(dir+dirs[j]+'/sf_var.%1d.txt'%(nrecord+1),comments='#')
       except: break
       nrecord+=1
       rr=a[:,0]
       sf=a[:,5]
       if(nrecord==1): sf_tot=sf.copy()
       else:  sf_tot+=sf    
       
    sf=sf_tot/nrecord   
    return (rr,sf)
          
