import math


# an object that stores a set of 2D points in horizontal order and in vertical order,
# and also the two closest neighbors in the set
class SortedPoints:
    # THERE ARE MANY CONDITIONS ON THE INPUT THAT WE MUST CHECK
    def __init__(self, x_sort, y_sort, n1, n2):
        assert len(x_sort) == len(y_sort)
        self.size = len(x_sort)
        self.x_sort = x_sort
        self.y_sort = y_sort
        self.n1 = n1
        self.n2 = n2


def squared_dist(p1, p2):
    return (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])


# input is a SortedPoints object, output is a list of two SortedPoints objects
def split(sorted_points):
    # the vertical line x = thresh splits the points in half
    # (assuming no two points have the same x-coordinate)
    mid = sorted_points.size // 2
    thresh = (sorted_points.x_sort[mid-1][0] + sorted_points.x_sort[mid][0]) / 2
    # create the horizontal half orderings
    lx_sort = []
    rx_sort = []
    for p in sorted_points.x_sort:
        if p[0] < thresh: lx_sort.append(p)
        else: rx_sort.append(p)
    # create the vertical half orderings
    ly_sort = []
    ry_sort = []
    for p in sorted_points.y_sort:
        if p[0] < thresh: ly_sort.append(p)
        else: ry_sort.append(p)
    # return a list of two SortedPoints objects
    return [SortedPoints(lx_sort, ly_sort, None, None), SortedPoints(rx_sort, ry_sort, None, None)]


# input is two SortedPoints objects, output is a single SortedPoints object
def merge(left_points, right_points):

    # find the dimensions of the strip
    left_squared_dist = squared_dist(left_points.n1, left_points.n2)
    right_squared_dist = squared_dist(right_points.n1, right_points.n2)
    squared_strip_radius = min(left_squared_dist, right_squared_dist)
    strip_center = (left_points.x_sort[-1][0] + right_points.x_sort[0][0]) / 2

    # make y-sorted lists of left and right points in the strip
    left_strip = []
    for p in left_points.y_sort:
        if (strip_center-p[0]) * (strip_center-p[0]) < squared_strip_radius:
            left_strip.append(p)
    right_strip = []
    for p in right_points.y_sort:
        if (p[0]-strip_center) * (p[0]-strip_center) < squared_strip_radius:
            right_strip.append(p)

    # merge left_strip and right_strip
    strip = []
    lindex = 0
    rindex = 0
    while len(strip) < len(left_strip) + len(right_strip):
        if lindex == len(left_strip):
            strip.append(right_strip[rindex])
            rindex += 1
        elif rindex == len(right_strip):
            strip.append(left_strip[lindex])
            lindex += 1
        elif left_strip[lindex][1] < right_strip[rindex][1]:
            strip.append(left_strip[lindex])
            lindex += 1
        else:
            strip.append(right_strip[rindex])
            rindex += 1

    # check at most O(n) distances
    min_pair = None
    min_squared_dist = squared_strip_radius
    for i in range (1, len(strip)):
        j = i - 1
        vert = strip[i][1] - strip[j][1]
        while j >= 0 and vert * vert < squared_strip_radius:
            if squared_dist(strip[i], strip[j]) < squared_strip_radius:
                min_pair = [strip[i], strip[j]]
                min_squared_dist = squared_dist(strip[i], strip[j])

    return merged_points


# input is a list of points (ordered pairs), output is a list of
# the two ordered pairs that are the closest neighbors
def closest_neighbors(points_list):

    # input is a SortedPoints object with unknown closest neighbors,
    # output is a SortedPoints object but with closest neighbors identified
    def recur(sorted_points):
        # recursion ends
        if sorted_points.size == 1:
            return sorted_points
        # recur on half-ranges
        else:
            [left_points, right_points] = split(sorted_points)
            return merge(recur(left_points), recur(right_points))

    x_sort = sorted(points_list, key=lambda p: p[0])
    y_sort = sorted(points_list, key=lambda p: p[1])
    sorted_points = SortedPoints(x_sort, y_sort, None, None)
    sorted_points = recur(sorted_points)

    return [sorted_points.n1, sorted_points.n2]
