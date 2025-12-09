
def findSubstring(line, words):
    freq_map = {}

    for word in words:
        freq_map[word] = freq_map.get(word, 0) + 1

    word_size = len(words[-1])
    answer = []

    for i in range(word_size):
        left = i
        right = i
        count = 0
        seen = {}

        while right + word_size <= len(line):
            word = line[right:right + word_size]
            right += word_size

            if word in freq_map:
                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > freq_map[word]:
                    left_word = line[left:left + word_size]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_size

                if count == len(words):
                    answer.append(left)

            else:
                seen.clear()
                count = 0
                left = right

    return answer
            

test_cases = [
    ("barfoothefoobarman", ["foo","bar"]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"]),
    ("barfoofoobarthefoobarman", ["bar","foo","the"])
]
test_results = [
    [0,9], [], [6,9,12]
]

for (array, max_width), expected in zip(test_cases, test_results):
    print(findSubstring(array, max_width) == expected)