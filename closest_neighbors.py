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
    # return a list of two SotredPoints objects
    return [SortedPoints(lx_sort, ly_sort, None, None), SortedPoints(rx_sort, ry_sort, None, None)]


# input is two SortedPoints objects, output is a single SortedPoints object
def merge(left_points, right_points):
    # some thought is needed here
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
