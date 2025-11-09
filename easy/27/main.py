def reverse_words(stdin):
    words = []
    word = ""
    reversed_string = ""

    for i in range(len(stdin)):
        if stdin[i] == " ":
            if word != "":
                words.append(word)
                word = ""
        else:
            word += stdin[i]

    if word != "":
        words.append(word)

    for i in range(len(words) - 1, -1, -1):
        reversed_string += words[i]

        if i > 0:
            reversed_string += " "

    return reversed_string


test_cases = [
    "the sky is blue", 
    "  hello world  ", 
    "a good   example"
]
test_results = [
    "blue is sky the",
    "world hello",
    "example good a"
]

for string_, expected in zip(test_cases, test_results):
    print(reverse_words(string_) == expected)