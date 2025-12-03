
def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        else:
            stack.append(int(token))

    return stack[-1]


test_cases = [
    ["2","1","+","3","*"], 
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
]
test_results = [
    9, 6, 22
]

for tokens, expected in zip(test_cases, test_results):
    print(evalRPN(tokens) == expected)