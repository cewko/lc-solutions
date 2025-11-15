def isHappy(n):
    seen = set()

    while n not in seen:
        seen.add(n)

        square_sum = 0
        
        while n:
            digit = n % 10
            square_sum += digit ** 2
            n //= 10
            
        n = square_sum

        if n == 1:
            return True

    return False


test_cases = [
    19, 2
]
test_results = [
    True, False
]

for number, expected in zip(test_cases, test_results):
    print(isHappy(number) == expected)