class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we can check the last element of each nested list, if its larger than we know we are in that list, then we can binary search for the target
        for arr in matrix:
            compare = len(arr)-1
            if arr[0] <= target <= arr[-1]:
                return self.search(arr, target)
            else:
                continue
        return False
    

    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            if target == nums[0]:
                return True
            else:
                return False
        
        L, R = 0, len(nums)-1
        while L<=R:
            M = (R+L)//2

            if nums[M] > target:
                R = M-1
            elif nums[M] < target:
                L = M+1
            else:
                return True

        return False