class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for j in range(n):
            l = 0 
            r = n - 1
            while l < r:
                temp = matrix[l][j]
                matrix[l][j] = matrix[r][j]
                matrix[r][j] = temp
                l += 1
                r -= 1
        
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


