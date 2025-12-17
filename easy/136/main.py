def singleNumber(nums):
    unique = 0

    for n in nums:
        unique ^= n

    return unique
    

test_cases = [
    [2,2,1],
    [4,1,2,1,2],
    [1]
]
test_results = [
    1, 4, 1
]

for n, expected in zip(test_cases, test_results):
    print(singleNumber(n) == expected)