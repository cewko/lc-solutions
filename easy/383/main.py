def can_construct(ransomNote, magazine):
    maga = {}

    for character in magazine:
        if character in maga:
            maga[character] += 1
        else:
            maga[character] = 1

    for character in ransomNote:
        if character in maga and maga[character] > 0:
            maga[character] -= 1
        else:
            return False

    return True


test_cases = [
    ("a", "b"), 
    ("aa", "ab"),
    ("aa", "aab")
]
test_results = [
    False, False, True
]

for strings, expected in zip(test_cases, test_results):
    print(can_construct(*strings) == expected)
