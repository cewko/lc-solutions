from collections import Counter


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    occurr = Counter(s)

    for c in t:
        if c in occurr and occurr[c] > 0:
            occurr[c] -= 1
        else:
            return False

    return True


test_cases = [
    ("anagram", "nagaram"), 
    ("rat", "car")
]
test_results = [
    True, False
]

for strings, expected in zip(test_cases, test_results):
    print(is_anagram(*strings) == expected)
    