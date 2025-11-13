def max_area(height):
    # amount = 0

    # for i in range(len(height)):
    #     for j in range(i + 1, len(height)):
    #         current_amount = (j - i) * min(height[i], height[j])
    #         if current_amount > amount:
    #             amount = current_amount

    # return amount

    amount = 0
    left = 0
    right = len(height) - 1

    while right > left:
        current_amount = (right - left) * min(height[left], height[right])
        if current_amount > amount:
            amount = current_amount
        
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return amount

test_cases = [
    [1,8,6,2,5,4,8,3,7], 
    [1,1]
]
test_results = [
    49, 1
]

for array, expected in zip(test_cases, test_results):
    print(max_area(array) == expected)



        