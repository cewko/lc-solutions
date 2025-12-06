def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    overlapping = [sorted_intervals[0]]

    for i in range(1, len(sorted_intervals)):
        if overlapping[-1][1] >= sorted_intervals[i][0]:
            overlapping[-1] = [
                    min(overlapping[-1][0], sorted_intervals[i][0]), 
                    max(overlapping[-1][1], sorted_intervals[i][1])
                ]
        else:
            overlapping.append(sorted_intervals[i])

    return overlapping
            

test_cases = [
    [[1,3],[2,6],[8,10],[15,18]], 
    [[1,4],[4,5]],
    [[4,7],[1,4]]
]
test_results = [
    [[1,6],[8,10],[15,18]],
    [[1,5]],
    [[1,7]]
]

for array, expected in zip(test_cases, test_results):
    print(merge(array) == expected)