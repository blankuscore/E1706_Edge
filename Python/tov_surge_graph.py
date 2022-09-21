from cProfile import label
import os
import math
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# Generate random events over 'past 30 days'
rng = np.random.default_rng(123)
tov_events = rng.integers(low=0, high=2, size=30)
surge_events = rng.integers(low=0, high=2, size=30)
days = np.arange(len(surge_events))

# Apply a magnitude to the events that occurred
magnitude_1 = rng.integers(low=0, high=6, size=30)
magnitude_2 = rng.integers(low=0, high=6, size=30)
tov_events = tov_events * magnitude_1
surge_events = surge_events * magnitude_2

# Plot the events
plt.bar(days, tov_events, label = "Surge Events")
plt.bar(days, surge_events, label = "TOV Events")
plt.legend(loc = "upper left")
plt.xlabel("Day")
plt.ylabel("Events")
plt.show()