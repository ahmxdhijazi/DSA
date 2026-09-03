class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string_list = []
        for word in strs:
            encoded_string_list.append(str(len(word)))
            encoded_string_list.append("#")
            encoded_string_list.append(word)
        return "".join(encoded_string_list)

    def decode(self, s: str) -> List[str]:
        decoded_string_list = []
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
            decoded_string_list.append(word)
            
            #Move pointer to the start of the next length indicator
            i = i + length
            
        return decoded_string_list