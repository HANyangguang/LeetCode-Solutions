'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        flag = True #suppose all <= 0
        for num in nums:
            if num > 0:
                flag = False
        if flag:
            return max(nums)
        
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            curSum += num
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum 