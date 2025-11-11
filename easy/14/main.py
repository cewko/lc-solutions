def longest_common_prefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        for word in strs[1:]:
            if i == len(word) or strs[0][i] != word[i]:
                return prefix
        prefix += strs[0][i]

    return prefix


test_cases = [
    ["flower","flow","flight"],
    ["dog","racecar","car"] 
]
test_results = [
    "fl", ""
]

for array, expected_output in zip(test_cases, test_results):
    print(longest_common_prefix(array) == expected_output)