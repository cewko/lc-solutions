def majority_element(nums):
    counter = 0
    candidate = None

    for num in nums:
        if counter == 0:
            candidate = num
        
        if candidate == num:
            counter += 1
        else:
            counter -= 1

    return candidate


test_cases = [
    [3,2,3], 
    [2,2,1,1,1,2,2]
]
test_results = [3, 2]

for array, expected in zip(test_cases, test_results):
    print(f"{majority_element(array) == expected}")