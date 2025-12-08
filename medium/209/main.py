def minSubArrayLen(nums, target):
    min_length = float("inf")
    total_sum = left = 0

    for right in range(len(nums)):
        total_sum += nums[right]

        while total_sum >= target:
            min_length = min(min_length, right - left + 1)
            total_sum -= nums[left]
            left += 1

    return min_length if min_length != float("inf") else 0
  

test_cases = [
    ([2,3,1,2,4,3], 7),
    ([1,4,4], 4),
    ([1,1,1,1,1,1,1,1], 11)
]
test_results = [
    2, 1, 0
]

for (array, k), expected in zip(test_cases, test_results):
    print(minSubArrayLen(array, k) == expected)