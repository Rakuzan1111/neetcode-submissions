class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dedup = []
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
                    if tuple([nums[pointer_1], nums[pointer_2], nums[pointer_3]]) not in dedup:
                        dedup.append(tuple([nums[pointer_1], nums[pointer_2], nums[pointer_3]]))
                        answer.append([nums[pointer_1], nums[pointer_2], nums[pointer_3]])
                    pointer_3 -= 1
        


         
    
        return answer
                

