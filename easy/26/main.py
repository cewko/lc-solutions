def remove_duplicates(nums):
    k = 0

    for i in range(1, len(nums)):
        if nums[k] != nums[i]:
            k += 1
            nums[k] = nums[i]

    return k + 1

test_cases = [
    [0,0,1,1,1,2,2,3,3,4], 
    [1,1,2], 
]
test_results = [
    5, 2
]

for array, expected_output in zip(test_cases, test_results):
    print(remove_duplicates(array) == expected_output)