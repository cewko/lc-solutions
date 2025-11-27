def convert(s, numRows):
    if numRows <= 1:
        return s

    characters = []

    for row in range(numRows):
        step = (numRows - 1) * 2
        for i in range(row, len(s), step):
            characters.append(s[i])
            if 0 < row < numRows - 1 and i + step - 2 * row < len(s):
                characters.append(s[i + step - 2 * row])

    return "".join(characters)


test_cases = [
    ("PAYPALISHIRING", 3),
    ("PAYPALISHIRING", 4),
    ("PAYPALISHIRING", 1)
]
test_results = [
    "PAHNAPLSIIGYIR",
    "PINALSIGYAHRPI",
    "PAYPALISHIRING"
]

for (strn, rows), expected in zip(test_cases, test_results):
    print(convert(strn, rows) == expected)
