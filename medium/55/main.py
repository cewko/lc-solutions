def canJump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

        if farthest >= len(nums) - 1:
            return True

    return True
        

test_cases = [
    [2,3,1,1,4],
    [3,2,1,0,4]
]
test_results = [
    True, False
]

for array, expected in zip(test_cases, test_results):
    print(canJump(array) == expected)