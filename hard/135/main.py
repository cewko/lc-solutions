def candy(ratings):
    candies = [1] * len(ratings)
    
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for j in range(len(ratings) - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candies[j] = max(candies[j + 1] + 1, candies[j])

    return sum(candies)


test_cases = [
    [1,0,2], 
    [1,2,2]
]
test_results = [
    5, 4
]

for ratings, expected in zip(test_cases, test_results):
    print(candy(ratings) == expected)