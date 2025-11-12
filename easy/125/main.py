import string


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    sl = s.lower()

    while left < right:
        if not sl[left].isalnum():
            left += 1
            continue

        if not sl[right].isalnum():
            right -= 1
            continue

        if sl[left] != sl[right]:
            return False

        left += 1
        right -= 1

    return True


test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
]
test_results = [
    True, False, True
]

for string_, expected in zip(test_cases, test_results):
    print(is_palindrome(string_) == expected)

        
        