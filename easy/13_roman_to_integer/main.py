def roman_to_int(stdint):
    romans = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000,
    }

    value = 0

    for i in range(len(stdint)):
        if i + 1 < len(stdint) and romans[stdint[i]] < romans[stdint[i + 1]]:
            value -= romans[stdint[i]]
        else:
            value += romans[stdint[i]]
    
    return value
        

test_cases = ["III", "LVIII", "MCMXCIV"]
test_results = [3, 58, 1994]

for roman, expected in zip(test_cases, test_results):
    print(f"{roman_to_int(roman) == expected}")
