import matplotlib.pyplot as plt
import numpy as np
class fft_analysis :

    def import_data(self, filename, working_dir) :
        
        self.f = working_dir+'\\'+ filename
        x,y = np.loadtxt(self.f, delimiter='\t',usecols=(0,1),unpack =True)
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

    def fft(self,x,y, fermi, num_zeros=8) :
    
        timewidth = (x[-1] - x[1]) #for frequency
        freq=(x.size*num_zeros/2)/(timewidth*num_zeros)    
        yf = np.fft.fft(y*fermi,y.size*num_zeros)
        xf = np.linspace(0, freq*yf.size, yf.size)
    
        return yf, xf
 
    def fermi_function (self,x,y) :
        Tstart=x[60]+8
        Tfinal=x[8]+8.5
        deltafermistart=0.1 
        deltafermifinal=0.2
        fermi=1/(1+np.exp((x-Tfinal)/deltafermifinal))*\
        1/(1+np.exp(-(x-Tstart)/deltafermistart))
    
        return fermi 

    

def main():
    scan01= fft_analysis()
    x, y = scan01.import_data('scan01.dat','C:\\Users\\sec\\Desktop\\scan')
           
    plt.subplot(2,1,1)
    plt.plot(x,y)
    plt.title('Thz data/FFT')
    plt.xlabel('Time (ps)')    
    plt.ylabel('Amplitude (arb. units)')
        
#    x, y = adding_up_zeros(x, y)    
    fermi = scan01.fermi_function(x,y)
    yf, xf = scan01.fft(x,y, fermi)    
    plt.subplot(2,1,2)    
    plt.plot(xf[0:(xf.size/2)], abs(yf[0:(yf.size/2)]))
    plt.xlabel('Furie frequency(Hz)')    
    plt.show()

    

    
if __name__ == '__main__':
    main()
