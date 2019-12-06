# input is a list of ordered pairs,
# output is the same list and a second list of the closest neighbors
def closest_neighbors(points):

    x_sorted_points = sorted(points, key=lambda p: p[0])
    y_sorted_points = sorted(points, key=lambda p: p[1])

    # n1, n2 are the closest neighbors among x_sorted_points[lo:hi]
    class PointRange:
        def __init__(self, lo, hi, n1, n2):
            self.lo = lo
            self.hi = hi
            self.n1 = n1
            self.n2 = n2

    # output is a PointRange object corresponding to x_sorted_points[lo:hi]
    def recur(lo, hi):

        # recursion ends
        if hi == lo + 1:
            return PointRange(lo, hi, None, None)

        # recur on half-ranges
        else:
            mid = (lo + hi) // 2  # always strictly between lo and hi
            left_range = recur(lo, mid)
            right_range = recur(mid, hi)
            return merge(left_range, right_range)

    # each input a four-element list of the form described below
    def merge(left_range, right_range):

        # more thought is needed here

        return merged_range

    return recur(0, len(points) - 1)
