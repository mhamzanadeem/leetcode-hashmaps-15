
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = collections.defaultdict(list)
        res=[]

        for s in strs:
            sorted_s = tuple(sorted(s))
            hashmap[sorted_s].append(s)

        for value in hashmap.values():
            res.append(value)
        
        return res