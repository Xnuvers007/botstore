# add module matplotlib
from matplotlib import pyplot as plt
# add module numpy
import numpy as np

# Create love In python
teta = np.arange(0, 2*np.pi, 0.01)

x = 16 * (np.sin(teta)**3)
y = 13 * np.cos(teta) - 5 * np.cos(2*teta) - 2 * np.cos(3*teta) - np.cos(4*teta)

plt.plot(x, y)
plt.title(" Love ")
plt.show()