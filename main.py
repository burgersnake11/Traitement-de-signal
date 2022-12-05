import numpy as np
from scipy.signal import butter, lfilter, freqz
from scipy import interpolate

def add_missing_value(a, y):
    x=list(a)
    i = len(x)
    j=0
    while True:
            if (j==i-1):
                return x, y
            if x[j+1]-x[j]>1:
                x.insert((j+1), (x[j]+1))
                add = (y[j]+y[j+1])/2
                y.insert((j+1),add)
                i = i + 1

            j+=1

def splinning(data_to_spline):
    n = len(data_to_spline)
    x = range(0, n)
    tck = interpolate.splrep(x, data_to_spline, s=0)
    xfit = np.arange(0, n-1, np.pi/50)
    yfit = interpolate.splev(xfit, tck, der=0)
    return xfit, yfit

def filter(data_to_filter):
    data_cleaned=[]
    for i in range(len(data_to_filter)):
        if i==0:
            data_cleaned.append((data_to_filter[i]+data_to_filter[i+1])/2)
        elif i==len(data_to_filter)-1:
            data_cleaned.append((data_cleaned[i-1]+data_to_filter[i])/2)
        else:
            data_cleaned.append((data_cleaned[i-1]+data_to_filter[i]+data_to_filter[i+1])/3)

    return data_cleaned

def replace_NaN(data_to_clean):
    data_cleaned=[]
    for i in range(len(data_to_clean)):
        if(data_to_clean[i]=="NaN"):
                    if i == 0:
                        add = data_to_clean[i+1]
                        data_cleaned.append(add)
                    elif data_to_clean[i-1] == "NaN":
                        add = (data_to_clean[i-2]+data_to_clean[i+1])/2
                        data_cleaned.append(add)
                    elif data_to_clean[i+1] == "NaN":
                        add = (data_to_clean[i-1]+data_to_clean[i+2])/2
                        data_cleaned.append(add)
                    else:
                        add = (data_to_clean[i-1]+data_to_clean[i+1])/2
                        data_cleaned.append(add)
        else:
            data_cleaned.append(data_to_clean[i])
    return data_cleaned
 
def filter_high_peak(data_to_clean):
    data_cleaned=[]
    max=0
    max=sum(data_to_clean)
    moyenne=max/len(data_to_clean)
    for i in range(len(data_to_clean)):
        if data_to_clean[i] > moyenne*15/10:
            try:
                data_cleaned.append((data_to_clean[-7]+data_to_clean[-8]+data_to_clean[i-6]+data_to_clean[i-5]+data_to_clean[i-4]+data_to_clean[i-3]+data_to_clean[i-2]+data_to_clean[i-1]+data_to_clean[i]+data_to_clean[i+1]+data_to_clean[i+2]+data_to_clean[i+3]+data_to_clean[i+4]+data_to_clean[i+5]+data_to_clean[i+6]+data_to_clean[+7]+data_to_clean[+8])/17)
            except:
                data_cleaned.append(moyenne)
        else:
            data_cleaned.append(data_to_clean[i])
    return data_cleaned

def filter_low_peak(data_to_clean):
    data_cleaned=[]
    for i in range(len(data_to_clean)):
        if data_to_clean[i] < 1:
            try:
                data_cleaned.append((data_to_clean[-7]+data_to_clean[-8]+data_to_clean[i-6]+data_to_clean[i-5]+data_to_clean[i-4]+data_to_clean[i-3]+data_to_clean[i-2]+data_to_clean[i-1]+data_to_clean[i]+data_to_clean[i+1]+data_to_clean[i+2]+data_to_clean[i+3]+data_to_clean[i+4]+data_to_clean[i+5]+data_to_clean[i+6]+data_to_clean[+7]+data_to_clean[+8])/17)
            except:
                data_cleaned.append(2)
        else:
            data_cleaned.append(data_to_clean[i])
    return data_cleaned

def calcul_acceleration(speed):
    acceleration=[]
    for i in range(len(speed)):
        if i == 0:
            acceleration.append(speed[i])
        elif i == len(speed)-1:
            acceleration.append(-speed[i])
        else: 
            acceleration.append(speed[i]-speed[i+1])
    return acceleration