class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        creates a new string which can be inneficient for
        very large strings > 50000
        """

        curr = ''
        largest = 0

        if not s:
            return 0
        if len(s) == 1:
            return 1

        for c in s:
            if c in curr:
                curr = curr[curr.index(c) + 1:]
                curr += c
            else:
                curr += c
            
            largest = max(largest, len(curr))

        return largest