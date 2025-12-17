def addBinary(a, b):
    answer = []
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        digit1 = int(a[i]) if i >= 0 else 0
        digit2 = int(b[j]) if j >= 0 else 0

        calculation = digit1 + digit2 + carry
        carry = calculation // 2

        answer.append(str(calculation % 2))

        i -= 1
        j -= 1

    return "".join(answer[::-1])


test_cases = [
    ("11", "1"),
    ("1010", "1011")
]
test_results = [
    "100", "10101"
]

for (a, b), expected in zip(test_cases, test_results):
    print(addBinary(a, b) == expected)