class SortedPoints:
    # THERE ARE MANY CONDITIONS ON THE INPUT THAT WE MUST CHECK
    def __init__(self, x_sort, y_sort, n1, n2):
        assert len(x_sort) == len(y_sort)
        self.size = len(x_sort)
        self.x_sort = x_sort
        self.y_sort = y_sort
        self.n1 = n1
        self.n2 = n2

# input is a list of ordered pairs, output is a list of
# the two ordered pairs that are the closest neighbors
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

    def merge(left_range, right_range):

        # more thought is needed here

        return merged_range

    full_range = recur(0, len(points) - 1)
    return [x_sorted_points[full_range.n1], x_sorted_points[full_range.n2]]
