class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            h = min(heights[left], heights[right])
            max_water = max(max_water, h * (right - left))
            
            # Advance left pointer past any bars <= current height h
            while left < right and heights[left] <= h:
                left += 1
                
            # Advance right pointer past any bars <= current height h
            while left < right and heights[right] <= h:
                right -= 1
                
        return max_water

