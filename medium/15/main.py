def threeSum(nums):
    output = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1]:
            continue

        left, right = index + 1, len(nums) - 1

        while left < right:
            tsum = value + nums[left] + nums[right]

            if tsum > 0:
                right -= 1
            elif tsum < 0:
                left += 1
            else:
                output.append([value, nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return output


test_cases = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0]
]
test_results = [
    [[-1,-1,2],[-1,0,1]],
    [],
    [[0,0,0]]
]

for array, expected in zip(test_cases, test_results):
    print(threeSum(array) == expected)