def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for x, y in zip(s, t):
        if x in s_to_t and s_to_t[x] != y:
            return False

        if y in t_to_s and t_to_s[y] != x:
            return False

        s_to_t[x] = y
        t_to_s[y] = x

    return True


test_cases = [
    ("egg", "add"), 
    ("foo", "bar"),
    ("paper", "title")
]
test_results = [
    True, False, True
]

for (s, t), expected in zip(test_cases, test_results):
    print(isIsomorphic(s, t) == expected)