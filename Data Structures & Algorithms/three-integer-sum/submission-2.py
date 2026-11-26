class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            pointer_1 = i
            pointer_2 = i + 1
            pointer_3 = (len(nums)-1)
            while pointer_2 < pointer_3:
                if nums[pointer_1] + nums[pointer_2] + nums[pointer_3] < 0:
                    pointer_2 += 1
                    continue
                if nums[pointer_1] + nums[pointer_2] + nums[pointer_3] > 0:
                    pointer_3 -= 1
                    continue
                else:
                    answer.append(tuple([nums[pointer_1], nums[pointer_2], nums[pointer_3]]))
                    pointer_3 -= 1
        


        map = {}
        for element in answer:
            if element not in map:
                map[element] = 0
    
        return list(map.keys())
                

