class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
         
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in map:
                map[sortedS] = [s]
            else:
                map[sortedS].append(s)
        return list(map.values())

            
            
            

            
                