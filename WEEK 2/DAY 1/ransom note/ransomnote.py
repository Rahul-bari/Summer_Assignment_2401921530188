class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        
        for char in magazine:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
                
        for char in ransomNote:
            if char not in letters or letters[char] == 0:
                return False
            letters[char] -= 1
            
        return True