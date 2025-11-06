def str_str(haystack, needle):
    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if len(needle) - 1 == j:
                return i

    return -1


test_cases = [
    ("sadbutsad", "sad"),
    ("leetcode", "leeto")
]
test_results = [
    0, -1
]

for string_, expected in zip(test_cases, test_results):
    print(str_str(*string_) == expected)