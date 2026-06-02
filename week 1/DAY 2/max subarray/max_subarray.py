class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = nums[0]
        cs = 0 
        
        for r in nums:
            cs += r
            maxsum = max(cs,maxsum)

            if cs< 0:
                cs = 0

        return maxsum

      

        





        