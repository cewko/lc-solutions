
def mySqrt(x):
    answer = None
    left, right = 0, x

    while left <= right:
        half = left + ((right - left) // 2)

        if half * half > x:
            right = half - 1
        elif half * half < x:
            left = half + 1
            answer = half
        else:
            return half

    return answer

test_cases = [
    4, 8
]
test_results = [
    2, 2
]

for string_, expected in zip(test_cases, test_results):
    print(f"{mySqrt(string_) == expected}")
            