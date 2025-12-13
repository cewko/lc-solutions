def trailingZeroes(n):
    zeros = 0

    while n >= 5:
        n //= 5
        zeros += n

    return zeros


test_cases = [
    3, 5, 0
]
test_results = [
    0, 1, 0
]

for n, expected in zip(test_cases, test_results):
    print(trailingZeroes(n) == expected)