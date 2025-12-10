def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits


test_cases = [
    [1,2,3],
    [4,3,2,1],
    [9]
]
test_results = [
    [1,2,4],
    [4,3,2,2],
    [1,0]
]

for string_, expected in zip(test_cases, test_results):
    print(f"{plusOne(string_) == expected}")