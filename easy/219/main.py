def contains_duplicate(nums, k):
    seen = {}

    for i in range(len(nums)):
        if nums[i] in seen:
            if i - seen[nums[i]] <= k:
                return True

        seen[nums[i]] = i

    return False


test_cases = [
    ([1,2,3,1], 3), 
    ([1,0,1,1], 1),
    ([1,2,3,1,2,3], 2)
]
test_results = [
    True, True, False
]

for (nums, k), expected in zip(test_cases, test_results):
    print(contains_duplicate(nums, k) == expected)