import os
import math
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

start = 0
stop = 30/60
interval = 2/60/60

phase_a = np.arange(start,stop,interval, dtype = np.double)
phase_b = np.arange(start,stop,interval, dtype = np.double)
phase_c = np.arange(start,stop,interval, dtype = np.double)

for k in range(len(phase_a)):
    phase_a[k] = 120*math.sqrt(2)*math.sin(2*math.pi*phase_a[k]*60)
    phase_b[k] = 120*math.sqrt(2)*math.sin(2*math.pi*phase_b[k]*60+120/360*2*math.pi)
    phase_c[k] = 120*math.sqrt(2)*math.sin(2*math.pi*phase_c[k]*60-120/360*2*math.pi)

for j in range(int(stop/interval/4)):
    plt.plot(phase_a[:j])
    plt.plot(phase_b[:j])
    plt.plot(phase_c[:j])
    plt.ylim(-180,180)

filenames = []
for i in range(int(stop/interval/4),len(phase_a),1):
    # plot the line chart
    plt.plot(phase_a[:i])
    plt.plot(phase_b[:i])
    plt.plot(phase_c[:i])
    plt.ylim(-180,180)
    plt.xlim(i - 100, i + 100)
    
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
