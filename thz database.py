#Thz data base for frequency of maximum's time
import numpy as np
import matplotlib.pyplot as plt
import os

def first_import_data (u) :
    k=np.array(['start'])
    
    for filename in os.listdir(u):
        if filename.split()[0]=='E' :
            k = np.append(k,filename)
        else : 
            k = np.append(k,[u+'\\'+filename])
            
        
            
    k= np.delete(k,0)
    return k

def make_array() :

    x=np.array(['data_start'])
    z=np.array(['dir_start'])
    x=np.delete(x,0)

    return x,z
    

def find_dir(k,x,z) :


    for i in k : 
        if os.path.isfile(i)==True :
            x = np.append( x ,[i])
        else :
            z = np.append(z, [i])
    

    return x, z

#in here distinction file or dir and, if file stroage in x or in z

def x_remove(x):
    z = np.array(['throw'])
    k = np.array([0])
    k = np.delete(k,0)
    for i in x :
        if i.split('.')[-1] == 'dat' :
            if i.split('.')[-2][-1] == 's' :
                z = np.append (z, [i])
            else : 
                k = np.append(k,[i])
    x=k
    return x
 


def reading_data_ext_data(f):
    x_max = np.array([0])
    y_max = np.array([0])
    x_mmgap = np.array([0])
    y_mmgap = np.array([0])
    for i in f:
        x, y = np.loadtxt(i, delimiter='\t',usecols=(0,1),unpack =True)
        x_max = np.append(x_max,[x[np.argmax(y)]])
        y_max = np.append(y_max,[np.amax(y)])
        x_mmgap = np.append(x_mmgap, [x[np.argmax(y)] - x[np.argmin(y)]])
        y_mmgap = np.append(y_mmgap, [np.amax(y)-np.amin(y)])
    np.delete(x_max,0)
    np.delete(y_max,0)
    np.delete(x_mmgap,0)
    np.delete(y_mmgap,0)
    x_max*=20/3
    x_mmgap*=20/3    
    return x_max, y_max, x_mmgap, y_mmgap

def main():
    
    u = 'E:'
    k = first_import_data(u)
    
    x, z = make_array()
    
    i, j = find_dir (k, x ,z)
    
    j = np.delete(j,0)
    
    k = np.array('dir_start')
    for w in j:
        k=np.append(k,first_import_data(w))
    k = np.delete(k,0)
    
   
    k = x_remove(k)
    
    
    
    
    x_max, y_max, x_mmgap, y_mmgap = reading_data_ext_data(k) 
           
    plt.subplot(2,1,1)
    plt.plot(np.linspace(0, 1*x_max.size ,x_max.size), x_max) #linspace 추가할것
    plt.title('Thz time-max frq/time gap')
    plt.xlabel('Time (ps)')    
    plt.ylabel('Amplitude (arb. units)')
            
    plt.subplot(2,1,2)    
    plt.plot( np.linspace(0, 1*x_mmgap.size, x_mmgap.size), x_mmgap)
    plt.xlabel('time gap dt(ps)')    
    plt.show()
    

    
if __name__ == '__main__':
    main()
    
    
