class Solution:
    def removeDuplicates(self, num: list[int]) -> int:
        if not num:
            return 0
        
        i = 0
        
        for j in range(1, len(num)):
            if num[j] != num[i]:
                i += 1
                num[i] = num[j]          
        
        return i + 1