def h_index(citations):
    # length = len(citations)

    # for h in range(length, -1, -1):
    #     count = 0

    #     for citation in citations:
    #         if citation >= h:
    #             count += 1

    #     if count >= h:
    #         return h

    length = len(citations)
    paper_count = [0] * (length + 1)

    for citation in citations:
        paper_count[min(length, citation)] += 1

    h = length
    papers = paper_count[h]

    while papers < h:
        h -= 1
        papers += paper_count[h]

    return h


test_cases = [
    [3,0,6,1,5],
    [1,3,1]
]
test_results = [
    3,
    1
]

for array, expected in zip(test_cases, test_results):
    print(h_index(array) == expected)
        
        