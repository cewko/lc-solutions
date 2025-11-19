def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1

        elif numbers[left] + numbers[right] < target:
            left += 1

        else:
            return [left + 1, right + 1]


test_cases = [
    ([2,7,11,15], 9),
    ([2,3,4], 6),
    ([-1,0], -1)
]
test_results = [
    [1,2], [1,3], [1,2]
]

for (array, target), expected in zip(test_cases, test_results):
    print(twoSum(array, target) == expected)