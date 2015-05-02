#THz Time trace data manipulation, fourier transform of THz time trace, and
#index, conductance calculation program (originally based on A. J. Adam`s program) 

#%%%%%%%%%%%%%%%%%%%% File input %%%%%%%%%%%%%%%%%%%%%%%%%%%

import numpy as np

def import_data(f):

    x,y = np.loadtxt(f, delimiter='\t',usecols=(0,1),unpack =True)
    x-=x[np.argmax(y)]
    x*=20/3
    return x, y

#def adding_up_zeros(x, y, num_zeros=8):
#    x_step=(x[-1]-x[0])/(x.size-1)
#    RspectrumT=np.arange(x[-1],x[-1]+x_step*x.size*num_zeros,x_step)
#    RspectrumV=np.zeros(y.size*num_zeros)
#    x=np.append(x, RspectrumT)
#    y=np.append(y, RspectrumV)
#    return x, y
# fft 함수 생성 이후 필요 없어진 함수

def fft(x,y, fermi, num_zeros=8) :
    
    timewidth = (x[-1] - x[1]) #for frequency
    freq=(x.size*num_zeros/2)/(timewidth*num_zeros)    
    yf = np.fft.fft(y*fermi,y.size*num_zeros)
    xf = np.linspace(0, freq*yf.size, yf.size)
    n = np.arange(0,0,yf.size/3)
    yf = np.append(n, yf)
    
    return yf, xf
 
def fermi_function (x,y) :
    Tstart=x[60]+8
    Tfinal=x[8]+8.5
    deltafermistart=0.1 
    deltafermifinal=0.2
    fermi=1/(1+np.exp((x-Tfinal)/deltafermifinal))*\
    1/(1+np.exp(-(x-Tstart)/deltafermistart))
    
    return fermi 

    


    

