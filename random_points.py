import matplotlib.pyplot as plt
import numpy as np
import sys

num_points = int(sys.argv[1])
x = list(np.around(np.random.random(num_points), decimals=3))
y = list(np.around(np.random.random(num_points), decimals=3))
points = list(zip(x, y))

ax = plt.gca().set_aspect('equal', 'datalim')
plt.plot(x, y, 'k.')
plt.show()

save = input('Type J to save points to ' + sys.argv[2] + ': ')
if save == 'J':
    txt_file = open(sys.argv[2], 'a')
    txt_file.write(str(points))
    txt_file.close()
