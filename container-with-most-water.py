# Problem - Container with most water.
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

#Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = height[-1]
        left = height[0]
        max_area = 0
        for i in range(0,len(height)-1):
            left = height[i]
            for j in range(len(height)-1,i,-1):
                right = height[j]
                h = min(left,right)
                max_area = max(max_area,h*(j-i))
        
        return max_area
