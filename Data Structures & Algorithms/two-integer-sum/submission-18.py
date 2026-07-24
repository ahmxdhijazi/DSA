
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevdict = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevdict:
                return [prevdict[diff], i]
            
            prevdict[n] = i

        return False
                


