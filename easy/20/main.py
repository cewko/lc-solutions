def isValid(characters):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for char in characters:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0


test_cases = [
    "()", "()[]{}", "(]", "([])", "([)]"
]
test_results = [
    True, True, False, True, False
]

for characters, expected_output in zip(test_cases, test_results):
    print(isValid(characters) == expected_output)