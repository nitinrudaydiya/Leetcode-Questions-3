class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import copy 
        m = copy.deepcopy(matrix[:])
        for i in range(len(m)):
            for j in range(len(m[i])):
                matrix[i][j]=m[len(m[j])-1-j][i]
        return matrix