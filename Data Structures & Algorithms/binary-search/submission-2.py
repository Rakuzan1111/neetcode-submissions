class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index_0 = 0
        index_1 = len(nums) - 1

        while index_0 <= index_1:
            midpoint = index_0 + (index_1 - index_0) // 2
            midpoint_value = nums[midpoint]
            
            if midpoint_value == target:
                return midpoint
            elif midpoint_value < target:
                index_0 = midpoint + 1
            else:
                index_1 = midpoint - 1
            
        return -1