def isPalindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False 

    number = x
    reversed_number = 0

    while number:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10

    return reversed_number == x


test_cases = [
    121, -121, 10
]
test_results = [True, False, False]

for string_, expected in zip(test_cases, test_results):
    print(f"{isPalindrome(string_) == expected}")

    