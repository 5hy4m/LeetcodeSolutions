class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        self.rowMat = len(mat)
        self.colMat = len(mat[0])
        self.currentPosition = [0,0]
        
        if self.rowMat * self.colMat != r * c:
            return mat
        
        res = []
        for i in range(r):
            res.append([])
            for j in range(c):
                res[-1].append(
                    mat[self.currentPosition[0]][self.currentPosition[1]]
                )
                self.updateNextPosition()
            
        return res
    
    def updateNextPosition(self):
        if self.currentPosition[1] < self.colMat - 1:
            self.currentPosition[1] += 1
        elif self.currentPosition[0] < self.rowMat - 1:
            self.currentPosition[0] += 1
            self.currentPosition[1] = 0
            