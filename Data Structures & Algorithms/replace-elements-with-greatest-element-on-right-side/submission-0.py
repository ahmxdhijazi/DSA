class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            big = 0
            for j in range(i+1, len(arr)):
                if arr[j] > big:
                    big = arr[j]
                arr[i] = big

        arr[-1] = -1
        return arr
                
