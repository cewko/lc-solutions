def climbStairs(n):
    one = two = 1

    for _ in range(n - 1):
        one, two = one + two, one

    return one
    

test_cases = [
    2, 3, 5
]
test_results = [
    2, 3, 8
]

for n, expected in zip(test_cases, test_results):
    print(climbStairs(n) == expected)