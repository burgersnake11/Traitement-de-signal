# importing required modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from controller import time_distance, distance, latitude, longitude



# create a figure, axis and plot element
fig = plt.figure()
#ax = plt.axes(xlim=(4.319, 4.320), ylim=(50.5945, 50.5947))
ax = plt.axes(xlim=(4.285, 4.32), ylim=(50.595, 50.625))
line, = ax.plot([], [], lw=2)

print("latitude")
print(latitude)
print("================================================================================")
print("longitude")
print(longitude)
# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,
  
# lists to store x and y axis points
xdata, ydata = [], []
  
# animation function
def animate(i):
    #I prendra toutes les valeurs, c'est une boucle mais jusque quelle valeur?
    abscisse = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0] #X
    ordonnée = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0] #Y
    xdata.append(longitude[i]) #Y
    ydata.append(latitude[i]) #X

    # set/update the x and y axes data
    line.set_data(xdata, ydata)
      
    # return line object
    return line,
      
plt.title('Ordonnée en fonction des abscisses')
plt.axis('on')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
  
# call the animator    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=5000, interval=120, blit=True)

# show the plot
plt.show()