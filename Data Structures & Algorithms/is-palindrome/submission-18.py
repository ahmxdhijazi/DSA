class Solution:
    def isPalindrome(self, s: str) -> bool:
        queue = []
        for c in s:
            if c.isalnum():
                queue.append(c.lower())
            else:
                continue
        
        
        return True if queue == queue[::-1] else False