
def summaryRanges(nums):
    intervals = []
    start = 0

    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
            if start == i:
                intervals.append(str(nums[i]))
            else:
                intervals.append("{0}->{1}".format(nums[start], nums[i]))
            start = i + 1

    return intervals


test_cases = [
    [0,1,2,4,5,7], 
    [0,2,3,4,6,8,9]
]
test_results = [
    ["0->2","4->5","7"],
    ["0","2->4","6","8->9"]
]

for array, expected in zip(test_cases, test_results):
    print(summaryRanges(array) == expected)