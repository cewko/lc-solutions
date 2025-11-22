def groupAnagrams(strs):
    if len(strs) <= 1:
        return [strs]

    hashmap = {}

    for word in strs:
        sorted_word = "".join(sorted(word))

        if sorted_word in hashmap:
            hashmap[sorted_word].append(word)

        else:
            hashmap[sorted_word] = [word]

    return hashmap.values()


test_cases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]
test_results = [
    [["bat"],["nat","tan"],["ate","eat","tea"]],
    [[""]], 
    [["a"]]
]


def compare(result, exptected):
    result_sorted = sorted([sorted(group) for group in result])
    expected_sorted = sorted([sorted(group) for group in expected])
    return result_sorted == expected_sorted

for array, expected in zip(test_cases, test_results):
    result = groupAnagrams(array)
    print(compare(result, expected))