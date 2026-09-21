class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using hashmap:
        d={}
        for i, n in enumerate(nums):
            if n in d:
                if i-d[n] <=k:
                    return True
                else:
                    d[n]=i
            else:
                d[n]=i
    
        return False