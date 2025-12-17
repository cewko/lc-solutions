def hammingWeight(n):
    count = 0
    
    while n > 0:
        count += n & 1
        n >>= 1

    return count


test_cases = [
    11,
    128,
    2147483645
]
test_results = [
    3, 1, 30
]

for n, expected in zip(test_cases, test_results):
    print(hammingWeight(n) == expected)