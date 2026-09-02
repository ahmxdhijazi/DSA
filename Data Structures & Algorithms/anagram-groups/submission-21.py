class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            key = ''.join(sorted(word)) # sorted puts each character in a list
            #handling a key not seen before
            if key not in my_dict:
                my_dict[key] = []
            #after, whether seen or not (since we handled that) we append it
            my_dict[key].append(word)
        return list(my_dict.values())
