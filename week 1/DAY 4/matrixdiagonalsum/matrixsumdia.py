class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            total_sum += mat[i][i]
            
            secondary_col = n - 1 - i
            if i != secondary_col:
                total_sum += mat[i][secondary_col]
                
        return total_sum