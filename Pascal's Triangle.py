class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [1]
        for _ in numRows:
            pascal_row = build_row(result[-1])
            result.append(pascal_row)
        return result
        
    def build_row(arr):
        p1 = -1
        p2 = 0
        len = len(arr)
        
        if p2 == len+1:
            return arr
        
        arr.
