def jump(nums):
    if len(nums) == 1:
        return 0

    farthest = current_end = 0
    jumps = 0
    
    for i in range(len(nums)):
        farthest = max(farthest, nums[i] + i)

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                return jumps


test_cases = [
    [2,3,1,1,4],
    [2,3,0,1,4]
]
test_results = [
    2, 2
]

for array, expected in zip(test_cases, test_results):
    print(jump(array) == expected)