class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows > 1:
            for _ in range(numRows-1):
                pascal_row = self.build_row(result[-1])
                result.append(pascal_row)
        return result
        
    def build_row(self,arr):
        p1 = 0
        p2 = 1
        res = [1]
        length = len(arr)
        
        while p2 < length:
            res.append(arr[p1]+arr[p2])
            p1+=1
            p2+=1
        res.append(1)
        return res