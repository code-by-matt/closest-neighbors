import matplotlib.pyplot as plt
import sys

ax = plt.gca().set_aspect('equal', 'datalim')
points = plt.ginput(int(sys.argv[1]), show_clicks=True)
print(points)
