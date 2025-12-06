
def insert(intervals, newInterval):
    answer = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            answer.append(newInterval)
            return answer + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            answer.append(intervals[i])
        else:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
            ]

    answer.append(newInterval)
    return answer


test_cases = [
    ([[1,3],[6,9]], [2,5]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
]
test_results = [
    [[1,5],[6,9]],
    [[1,2],[3,10],[12,16]]
]

for (intervals, new_interval), expected in zip(test_cases, test_results):
    print(insert(intervals, new_interval) == expected)