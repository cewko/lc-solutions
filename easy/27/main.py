def remove_element(nums, value):
    left = 0

    for right in range(len(nums)):
        if nums[right] != value:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return left


test_cases = [
    ([3,2,2,3], 3),
    ([0,1,2,2,3,0,4,2], 2)
]
test_results = [
    [2,2],
    [0,1,3,0,4]
]


for (nums, value), expected in zip(test_cases, test_results):
    print(nums[:remove_element(nums, value)] == expected)