class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        keys = list(map.keys())
        values = list(map.values())
        ans = []
        for i in range(k):
            
            ans.append(keys[values.index(max(values))])
            keys.pop(values.index(max(values)))
            values.pop(values.index(max(values)))
        return ans

