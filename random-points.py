import matplotlib.pyplot as plt
import numpy as np
import sys

num_points = int(sys.argv[1])
x = list(np.random.random(num_points))
y = list(np.random.random(num_points))
points = list(zip(x, y))

ax = plt.gca().set_aspect('equal', 'datalim')
plt.plot(x, y, 'k.')
plt.show()
