
def findMinArrowShots(points):
    sorted_intervals = sorted(points, key=lambda interval: interval[0])
    arrows = len(sorted_intervals)
    prev = sorted_intervals[0]

    for i in range(1, len(sorted_intervals)):
        curr = sorted_intervals[i]

        if prev[1] >= curr[0]:
            arrows -= 1
            prev = [curr[0], min(curr[1], prev[1])]
        else:
            prev = curr

    return arrows
        

test_cases = [
    [[10,16],[2,8],[1,6],[7,12]],
    [[1,2],[3,4],[5,6],[7,8]]
]
test_results = [
    2, 4
]

for array, expected in zip(test_cases, test_results):
    print(findMinArrowShots(array) == expected)
        