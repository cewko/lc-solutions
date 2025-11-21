def productExceptSelf(nums):
    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = nums[i - 1] * left[i - 1]

    for j in range(len(nums) - 2, -1, -1):
        right[j] = nums[j + 1] * right[j + 1]

    return [a * b for a, b in zip(left, right)]

test_cases = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]
test_results = [
    [24,12,8,6],
    [0,0,9,0,0]
]

for array, expected in zip(test_cases, test_results):
    print(productExceptSelf(array) == expected)