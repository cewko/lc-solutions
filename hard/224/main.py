def calculate(s):
    curr_num, curr_res = 0, 0
    sign = 1
    stack = []

    for character in s:
        if character.isdigit():
            curr_num = curr_num * 10 + int(character)
        elif character in ("+", "-"):
            curr_res += sign * curr_num
            sign = 1 if character == "+" else -1
            curr_num = 0
        elif character == "(":
            stack.append(curr_res)
            stack.append(sign)
            sign = 1
            curr_res = 0
        elif character == ")":
            curr_res += sign * curr_num
            curr_res *= stack.pop()
            curr_res += stack.pop()
            curr_num = 0

    return curr_res + sign * curr_num


test_cases = [
    "1 + 1", 
    " 2-1 + 2 ",
    "(1+(4+5+2)-3)+(6+8)"
]
test_results = [
    2, 3, 23
]

for strings, expected in zip(test_cases, test_results):
    print(calculate(strings) == expected)