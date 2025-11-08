def rotate(nums, k):
    # solution #1
    # for _ in range(k):
    #     num = nums.pop()
    #     nums.insert(0, num)

    # solution #2
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    
    # solution #3
    # k = k % len(nums)

    # def reverse(start, end):
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1

    # reverse(0, len(nums) - 1)
    # reverse(0, k - 1)
    # reverse(k, len(nums) - 1)

    return nums


test_cases = [
    ([1,2,3,4,5,6,7], 3),
    ([-1,-100,3,99], 2)
]
test_results = [
    [5,6,7,1,2,3,4],
    [3,99,-1,-100]
]

for (array, k), expected in zip(test_cases, test_results):
    print(rotate(array, k) == expected)