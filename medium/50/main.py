
def myPow(x, n):
    negative = n < 0
    n = abs(n)
    mapping = {}

    answer = calculate_pow(x, n, mapping)

    return 1 / answer if negative else answer

def calculate_pow(x, n, mapping):
    if n in mapping:
        return mapping[n]

    if n == 0:
        return 1
    if n == 1:
        return x

    mapping[n] = calculate_pow(x, n // 2, mapping) * \
        calculate_pow(x, n // 2, mapping) * (x if n % 2 else 1)

    return mapping[n]
    

test_cases = [
    (2.00000, 10),
    (2.10000, 3),
    (2.00000, -2),
]
test_results = [
    1024.00000, 9.26100, 0.25000
]

for (x, n), expected in zip(test_cases, test_results):
    print(round(myPow(x, n), 4) == round(expected, 4))