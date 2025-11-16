def removeDuplicates(nums):
    left, right = 0, 0

    while right < len(nums):
        streak = 1

        while right + 1 < len(nums) and nums[right] == nums[right + 1]:
            streak += 1
            right += 1

        for i in range(min(2, streak)):
            nums[left] = nums[right]
            left += 1

        right += 1

    return left


test_cases = [
    [1,1,1,2,2,3], 
    [0,0,1,1,1,1,2,3,3],
]
test_results = [
    5, 7
]

for array, expected in zip(test_cases, test_results):
    print(removeDuplicates(array) == expected)