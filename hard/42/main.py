def trap(height):
    if not len(height):
        return 0

    left_max = [0] * len(height)
    right_max = [0] * len(height)

    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(height[i], left_max[i - 1])

    right_max[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(height[i], right_max[i + 1])

    water = 0
    for i in range(len(height)):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


test_cases = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5]
]
test_results = [
    6, 9
]

for array, expected in zip(test_cases, test_results):
    print(trap(array) == expected)