def longestConsecutive(nums):
    nums = set(nums)
    max_length = 0

    for num in nums:
        if num - 1 not in nums:
            length = 0

            while num in nums:
                length += 1
                num += 1

            if length > max_length:
                max_length = length

    return max_length


test_cases = [
    [100,4,200,1,3,2],
    [0,3,7,2,5,8,4,6,0,1],
    [1,0,1,2]
]
test_results = [
    4, 9, 3
]

for array, expected in zip(test_cases, test_results):
    print(longestConsecutive(array) == expected)
    