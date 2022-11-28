from tcxreader.tcxreader import TCXReader, TCXTrackPoint
import matplotlib.pyplot as plt
import numpy as np
from main import add_missing_value, splinning, filter, replace_NaN, filter_big_mistake, calcul_acceleration
import os
import matplotlib.animation as animation

tcx_reader = TCXReader()
dir = "files"
fig, grph = plt.subplots(5)

for path in os.listdir(dir):
    path="files/"+path
    data: TCXTrackPoint = tcx_reader.read(path)
    latitude = []
    longitude = []
    time = []
    elevation = []
    distance = []
    vitesse = []
    acceleration = []
    heures=0
    minutes=0
    secondes=0
    for i in data.trackpoints :
        a=str(i).split()
        try:
            latitude.append(float(a[a.index("Latitude:")+1])) 
        except:
            latitude.append("NaN")
        try:
            longitude.append(float(a[a.index("Longitude:")+1]))
        except:
            longitude.append("NaN")
        try:
            elevation.append(float(a[a.index("Elevation:")+1]))
        except:
            elevation.append("NaN")
        try:
            distance.append(float(a[a.index("Distance:")+1]))
        except:
            distance.append("NaN")

        c=i.tpx_ext
        if c == {}:
            vitesse.append("NaN")
        else:
            vitesse.append(float(c["Speed"]))
            
        b=a[1].split(":")
        heures=int(b[0])*60*60
        minutes=int(b[1])*60
        secondes=int(b[2])
        time.append(heures+minutes+secondes)
        try:
            acceleration.append((vitesse[np.size(vitesse)-1]-vitesse[np.size(vitesse)-2])/float(time[np.size(time)-1]-time[np.size(time)-2]))
        except: 
            acceleration.append(0)
    time = tuple(time)
    vitesse = replace_NaN(vitesse) 
    vitesse = filter_big_mistake(vitesse)
    vitesse = filter(vitesse) 


    time_vitesse, vitesse = add_missing_value(time, vitesse)
    time_acceleration, acceleration = add_missing_value(time, acceleration)
    time_elevation, elevation = add_missing_value(time, elevation)
    time_distance, distance = add_missing_value(time, distance) 
    time_elevation, elevation = splinning(elevation)
    time_distance, distance = splinning(distance)
    time_vitesse, vitesse = splinning(vitesse) 
    
    grph[0].plot(time_elevation,elevation)
    grph[0].set_title("Élévation en fonction du temps")
    print(latitude)
    grph[1].plot(latitude,longitude)
    grph[1].set_title("Carte")
    grph[2].plot(time_distance,distance)
    grph[2].set_title("Distance en fonction du temps")
    grph[3].plot(time_vitesse,vitesse)
    grph[3].set_title("Vitesse en fonction du temps")
    grph[4].plot(time_acceleration, acceleration)
    grph[4].set_title("Accélération en fonction du temps") 

plt.show()