def simplifyPath(path):
    stack = []
    
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)
    
    return "/" + "/".join(stack)


test_cases = [
    "/home//foo/", 
    "/home/user/Documents/../Pictures",
    "/.../a/../b/c/../d/./"
]
test_results = [
    "/home/foo",
    "/home/user/Pictures",
    "/.../b/d"
]

for path, expected in zip(test_cases, test_results):
    print(simplifyPath(path) == expected)