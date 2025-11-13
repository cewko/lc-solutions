def is_subsequence(s, t):
    # boolean = False
    
    # for i in range(len(t)):
    #     for j in range(len(s)):
    #         if j == len(s) - 1 and boolean:
    #             return True
    #         elif t[i] == s[j]:
    #             boolean = True
    #         else:
    #             boolean = False

    # return False
    
    left = 0
    right = 0

    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        
        right += 1
    
    return left == len(s)


test_cases = [
    ("abc", "ahbgdc"),
    ("axc", "ahbgdc")
]
test_results = [
    True, False
]

for strings, expected in zip(test_cases, test_results):
    print(is_subsequence(*strings) == expected)
