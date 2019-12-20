"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,j in enumerate(nums):
            if i!=j:
                return i
        return len(nums)

"""
FirstCommit:
Runtime: 152 ms, faster than 58.91% of Python3 online submissions for Missing Number.
Memory Usage: 14 MB, less than 83.87% of Python3 online submissions for Missing Number.
"""
