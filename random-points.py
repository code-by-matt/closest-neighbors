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

save = input('Type J to save points to test-sets.txt: ')
if save == 'J':
    txt_file = open('test-sets.txt', 'a')
    txt_file.write(str(points))
    txt_file.close()
