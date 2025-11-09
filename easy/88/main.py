def merge(nums1, m, nums2, n):
    m_ptr, n_ptr = m - 1, n - 1
    i_ptr = m + n - 1

    while n_ptr >= 0:
        if m_ptr < 0 or nums1[m_ptr] < nums2[n_ptr]:
            nums1[i_ptr] = nums2[n_ptr]
            n_ptr -= 1
        else:
            nums1[i_ptr] = nums1[m_ptr]
            m_ptr -= 1

        i_ptr -= 1

    return nums1


test_cases = [
    ([1,2,3,0,0,0], 3, [2,5,6], 3),
    ([1], 1, [], 0),
    ([0], 0, [1], 1),
]
test_results = [
    [1,2,2,3,5,6],
    [1],
    [1]
]

for collection, expected in zip(test_cases, test_results):
    print(merge(*collection) == expected)
