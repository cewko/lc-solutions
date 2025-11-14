def two_sum(nums, target):
    seen = {}

    for index, number in enumerate(nums):
        value = target - number

        if value in seen:
            return [seen[value], index]

        seen[number] = index


test_cases = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6)
]
test_results = [
    [0,1], [1,2], [0,1]
]

for args, expected in zip(test_cases, test_results):
    print(two_sum(*args) == expected)