def length_of_last_word(s):
    length = 0
    counting = False

    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            length += 1
            counting = True
        elif counting:
            break

    return length


test_cases = [
    "Hello World", 
    "   fly me   to   the moon  ", 
    "luffy is still joyboy"
]
test_results = [5, 4, 6]

for string_, expected in zip(test_cases, test_results):
    print(f"{length_of_last_word(string_) == expected}")