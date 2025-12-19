def searchInsert(nums, target):
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle

    return left


test_cases = [
    ([1,3,5,6], 5),
    ([1,3,5,6], 2),
    ([1,3,5,6], 7)

]
test_results = [
    2, 1, 4
]

for (nums, target), expected in zip(test_cases, test_results):
    print(searchInsert(nums, target) == expected)
