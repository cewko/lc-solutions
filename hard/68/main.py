def fullJustify(words, maxWidth):
    justified = []
    current_line = []
    current_length = 0
    i = 0

    while i < len(words):
        if current_length + len(current_line) + len(words[i]) > maxWidth:
            space_left = maxWidth - current_length
            spaces = space_left // max(1, len(current_line) - 1)
            remaining = space_left % max(1, len(current_line) - 1)

            for j in range(max(1, len(current_line) - 1)):
                current_line[j] += " " * spaces

                if remaining:
                    current_line[j] += " "
                    remaining -= 1

            justified.append("".join(current_line))
            current_line = []
            current_length = 0

        current_line.append(words[i])
        current_length += len(words[i])
        i += 1

    last_line = " ".join(current_line)
    trailing_spaces = maxWidth - len(last_line)
    justified.append(last_line + " " * trailing_spaces)

    return justified
        

test_cases = [
    (["This", "is", "an", "example", "of", "text", "justification."], 16), 
    (["What","must","be","acknowledgment","shall","be"], 16),
    (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
]
test_results = [
    [
        "This    is    an",
        "example  of text",
        "justification.  "
    ],
    [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ],
    [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
]

for (array, max_width), expected in zip(test_cases, test_results):
    print(fullJustify(array, max_width) == expected)