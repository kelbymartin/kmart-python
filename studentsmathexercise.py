def minimum_points(thresh, points):
    solve = 0
    first = points[0]
    i = 0
    while i < len(points) - 1:
        if i < len(points) - 2:
            one = points[i + 1] - first
            two = points[i + 2] - first
            if one >= thresh and one < two:
                solve = one
                i += 1
                # print("Choose +1, solve:", solve)
            else:
                solve = two
                i += 2
                # print("Choose +2, solve:", solve)
        else:
            one = points[i + 1] - first
            solve = one
            i += 1
        if solve >= thresh:
            return solve
    return solve
        

print("Test 1:", minimum_points(2, [1, 2, 3]))
print("Test 2:", minimum_points(4, [1, 2, 3, 4, 5]))
print("Test 3:", minimum_points(4, [1, 2, 3, 5, 8]))
print("Test 4:", minimum_points(12, [1, 2, 3, 5, 8, 13, 14, 15, 18]))
print("Test 5:", minimum_points(100, [1]))