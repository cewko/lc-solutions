# 219. Contains Duplicate II

You are given an integer array nums and an integer k. Your task is to determine if there exist two distinct indices i and j in the array that satisfy both of the following conditions:

- The values at these indices are equal: nums[i] == nums[j]
- The absolute difference between the indices is at most k: abs(i - j) <= k

In other words, you need to find if there are any duplicate values in the array where the duplicates appear within a distance of at most k positions from each other.

Return true if such a pair of indices exists, otherwise return false.


**Example 1:**

    Input: nums = [1,2,3,1], k = 3
    Output: true

**Example 2:**

    Input: nums = [1,0,1,1], k = 1
    Output: true

**Example 3:**

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

**Constraints:**

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109
- 0 <= k <= 105
