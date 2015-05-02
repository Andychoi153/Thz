#THz Time trace data manipulation, fourier transform of THz time trace, and
#index, conductance calculation program (originally based on A. J. Adam`s program) 

#%%%%%%%%%%%%%%%%%%%% File input %%%%%%%%%%%%%%%%%%%%%%%%%%%

import numpy as np
import matplotlib.pyplot as plt

def import_data(filename='Scan01.dat',\
 working_dir='C:\\Users\\sec\\Desktop\\scan'):
    f = working_dir+'\\'+filename
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
    
    return yf, xf
 
def fermi_function (x,y) :
    Tstart=x[60]+8
    Tfinal=x[8]+8.5
    deltafermistart=0.1 
    deltafermifinal=0.2
    fermi=1/(1+np.exp((x-Tfinal)/deltafermifinal))*\
    1/(1+np.exp(-(x-Tstart)/deltafermistart))
    
    return fermi 
    

def main():
    
    x, y = import_data()
           
    plt.subplot(2,1,1)
    plt.plot(x,y)
    plt.title('Thz data/FFT')
    plt.xlabel('Time (ps)')    
    plt.ylabel('Amplitude (arb. units)')
        
#    x, y = adding_up_zeros(x, y)    
    fermi = fermi_function(x,y)
    yf, xf = fft(x,y, fermi)    
    plt.subplot(2,1,2)    
    plt.plot(xf[0:(xf.size/2)], abs(yf[0:(yf.size/2)]))
    plt.xlabel('Furie frequency(Hz)')    
    plt.show()
    

    
if __name__ == '__main__':
    main()