class Solution:
    def isValid(self, s: str) -> bool:
        #s = "([{}])"
        mapping = {']' : '[', '}' : '{', ')' : '('}
        result = []

        for char in s:
            if char in mapping: #know its a key
                if result and result[-1] == mapping[char]:
                    result.pop()
                else:
                    return False
                    
            else:
                result.append(char)

        return True if not result else False

