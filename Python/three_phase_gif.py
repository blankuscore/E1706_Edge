import os
import math
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

phase_a = np.arange(0,120/60,2/60/60, dtype = np.double)
phase_b = np.arange(0,120/60,2/60/60, dtype = np.double)
phase_c = np.arange(0,120/60,2/60/60, dtype = np.double)

for k in range(len(phase_a)):
    phase_a[k] = 120*math.sqrt(2)*math.sin(2*math.pi*phase_a[k]*60)
    phase_b[k] = 120*math.sqrt(2)*math.sin(2*math.pi*phase_b[k]*60+120/360*2*math.pi)
    phase_c[k] = 120*math.sqrt(2)*math.sin(2*math.pi*phase_c[k]*60-120/360*2*math.pi)


filenames = []
for i in range(len(phase_a)):
    # plot the line chart
    plt.plot(phase_a[:i])
    plt.plot(phase_b[:i])
    plt.plot(phase_c[:i])
    plt.ylim(-180,180)
    
    # create file name and append it to a list
    filename = f'{i}.png'
    filenames.append(filename)
    
    # save frame
    plt.savefig(filename)
    plt.close()

# build gif
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename) 
