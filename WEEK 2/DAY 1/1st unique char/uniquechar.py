class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = {}
        
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
                
        for index, char in enumerate(s):
            if char_freq[char] == 1:
                return index
                
        return -1