def maxProfit(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit
    

test_cases = [
    [7,1,5,3,6,4], 
    [1,2,3,4,5],
    [7,6,4,3,1]
]
test_results = [
    7, 4, 0
]

for array, expected in zip(test_cases, test_results):
    print(maxProfit(array) == expected)