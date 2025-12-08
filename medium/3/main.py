
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        character = s[right]

        while character in seen:
            seen.remove(s[left])
            left += 1

        seen.add(character)
        max_length = max(max_length, right - left + 1)
        
    return max_length


test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]
test_results = [
    3, 1, 3
]

for string_, expected in zip(test_cases, test_results):
    print(lengthOfLongestSubstring(string_) == expected)