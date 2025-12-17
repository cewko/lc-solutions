def reverseBits(n):
    result = 0

    for _ in range(32):
        # extract rightmost bit, 1101 & 1 = 1
        bit = n & 1
        # shift result left to make room for the new bit
        # 1101 << 1 = 1010
        result = result << 1
        # add extracted bit to result, 1010 | 1 = 1011
        result = result | bit
        # shift n for next iteration, 1101 >> 1 = 0110
        n = n >> 1

    return result


test_cases = [
    43261596,
    2147483644
]
test_results = [
    964176192, 1073741822
]

for n, expected in zip(test_cases, test_results):
    print(reverseBits(n) == expected)