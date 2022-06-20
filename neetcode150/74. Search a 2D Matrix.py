class Solution:
    #log(m*n), 1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0]) 
        top, btm = 0, len(matrix) - 1 #top and bottom pointers for vertical srch
        
        #searching for appropriate row
        while top <= btm: #note it's equal and smaller. Not just smaller
            mid = (top + btm) // 2
            if target < matrix[mid][0]:
                btm = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else: #target lies in mid row
                #binary search in this row
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid2 = (l + r) // 2
                    if target > matrix[mid][mid2]:
                        l = mid2 + 1
                    elif target < matrix[mid][mid2]:
                        r = mid2 - 1
                    else:
                        return True
                return False
        return
                