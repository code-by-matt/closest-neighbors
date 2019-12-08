import closest_neighbors as cn
import ast

lines = [line.rstrip('\n') for line in open('split_tests.txt')]
for i in range(8, len(lines), 8):

    name = lines[i]
    x_sort = ast.literal_eval(lines[i+1])
    y_sort = ast.literal_eval(lines[i+2])
    lx_sort = ast.literal_eval(lines[i+3])
    ly_sort = ast.literal_eval(lines[i+4])
    rx_sort = ast.literal_eval(lines[i+5])
    ry_sort = ast.literal_eval(lines[i+6])

    test_case = cn.SortedPoints(x_sort, y_sort, None, None)
    [left_result, right_result] = cn.split(test_case)
    assert left_result.x_sort == lx_sort, name
    assert left_result.y_sort == ly_sort, name
    assert right_result.x_sort == rx_sort, name
    assert right_result.y_sort == ry_sort, name

print('All test cases passed!')
