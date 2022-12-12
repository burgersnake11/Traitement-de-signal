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
    xdata.append(longitude[i]) #Y
    ydata.append(latitude[i]) #X

    # set/update the x and y axes data
    line.set_data(xdata, ydata)

    # return line object
    return line,

plt.title('Parcours du coureur')
plt.axis('on')
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=5000, interval=120, blit=True)

# show the plot
plt.show()