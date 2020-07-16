'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxArea = 0
        while p1 < p2:
            maxArea = max(maxArea, (p2 - p1) * min(height[p1], height[p2]))
            if height[p1] > height[p2]:
                p2 -= 1
            else: 
                p1 += 1 
        return maxArea


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxArea = 0
        while p1 < p2:
            maxArea = max(maxArea, (p2 - p1) * min(height[p1], height[p2]))
            if height[p1] > height[p2]:
                h2 = height[p2]
                while(height[p2] <= h2 and p1 < p2):
                    p2 -= 1
            else:
                h1 = height[p1]
                while(height[p1] <= h1 and p1 < p2):
                    p1 += 1 
        return maxArea