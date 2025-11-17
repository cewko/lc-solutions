def intToRoman(num):
    value_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    roman = ""

    for value, symbol in value_map:
        count = num // value
        
        if count:
            roman += symbol * count
            num -= value * count

    return roman


test_cases = [
    3749, 
    58,
    1994,
]
test_results = [
    "MMMDCCXLIX",
    "LVIII",
    "MCMXCIV"
]

for num, expected in zip(test_cases, test_results):
    print(intToRoman(num) == expected)