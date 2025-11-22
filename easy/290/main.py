def wordPattern(pattern, s):
    s = s.split()

    if len(pattern) != len(s):
        return False

    pattern_to_word = {}
    word_to_pattern = {}

    for i in range(len(pattern)):
        char = pattern[i]

        if char in pattern_to_word and pattern_to_word[char] != s[i]:
            return False

        if s[i] in word_to_pattern and word_to_pattern[s[i]] != char:
            return False

        pattern_to_word[char] = s[i] 
        word_to_pattern[s[i]] = char
        
    return True


test_cases = [
    ("abba", "dog cat cat dog"), 
    ("abba", "dog cat cat fish"),
    ("aaaa", "dog cat cat dog")
]
test_results = [
    True, False, False
]

for (pattern, s), expected in zip(test_cases, test_results):
    print(wordPattern(pattern, s) == expected)