def max_profit(prices):
    max_prof = 0
    left = 0

    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            left = right
        else:
            profit = prices[right] - prices[left]
            max_prof = max(profit, max_prof)

    return max_prof


test_cases = [
    [7,1,5,3,6,4], 
    [7,6,4,3,1]
]
test_results = [5, 0]

for array, expected in zip(test_cases, test_results):
    print(f"{max_profit(array) == expected}")