import matplotlib.pyplot as plt
import sys

ax = plt.gca().set_aspect('equal', 'datalim')
points = plt.ginput(int(sys.argv[1]), show_clicks=True)

save = input('Type J to save points to test-sets.txt: ')
if save == 'J':
    txt_file = open('test-sets.txt', 'a')
    txt_file.write(str(points))
    txt_file.close()
