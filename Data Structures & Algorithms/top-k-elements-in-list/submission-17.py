class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [] #Integers with highest frequencies appended

        #First lets get all the frequencies
        frequncies = defaultdict(int)
        for num in nums:
            frequncies[num] += 1

        #Finally we return the k amount of largest frequencies
        while k>0:
            max_key = max(frequncies, key=frequncies.get)
            result.append(max_key)
            frequncies.pop(max_key)
            k-=1

        return result