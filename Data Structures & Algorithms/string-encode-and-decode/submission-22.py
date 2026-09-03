class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded = str(len(word)) + "#" + word
            encoded_string+=encoded
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
    
        while i < len(s):
            #Find where the '#' is to get the full number
            j = i
            while s[j] != '#':
                j += 1
            
            #Length of our word and move pointer past the '#'
            length = int(s[i:j])
            i = j + 1
            
            #Read exactly 'length' characters
            word = s[i : i + length]
            res.append(word)
            
            #Move pointer to the start of the next length indicator
            i = i + length
            
        return res