import numpy as np
from scipy.signal import butter, lfilter, freqz
from scipy import interpolate



def add_missing_value(a, y):
    x=list(a)
    i = len(x)
    j=0
    while True:
            """         try: """
            if(y[j]=="NaN"):
                if j == 0:
                    add = y[j+1]
                    y[j]=add
                elif y[j-1] == "NaN":
                    add = (y[j-2]+y[j+1])/2
                    y[j] =add
                elif y[j+1] == "NaN":
                    add = (y[j-1]+y[j+2])/2
                    y[j]= add
                else:
                    add = (y[j-1]+y[j+1])/2
                    y[j]=add
            elif j == len(x)-1:
                return x, y
            if x[j+1]-x[j]>1:
                x.insert((j+1), (x[j]+1))
                add = (y[j]+y[j+1])/2
                y.insert((j+1),add)
                i = i + 1
            """         except:pass """
            if (j==i):
                return x, y
            j+=1

def splinning(data_to_spline):
    n = len(data_to_spline)
    x = range(0, n)
    tck = interpolate.splrep(x, data_to_spline, s=0)
    xfit = np.arange(0, n-1, np.pi/50)
    yfit = interpolate.splev(xfit, tck, der=0)
    return xfit, yfit





 



