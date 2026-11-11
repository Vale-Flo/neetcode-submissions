class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # if I haven t the conditions mentionned at the subject, I'd use
        # matrix.sort()
        # print(matrix)

        #each row is sorted in non-decreasing order.
        #The first integer of every row is greater than the last integer of the previous row.
        y_max = len(matrix) - 1
        x_max = len(matrix[0]) - 1


        #search in the col of matrix, the target (so the "row"):
        start_col = 0
        end_col = y_max
        row_f = []
        while start_col <= end_col:
            row = (start_col+end_col)//2
            #last elem from the row
            if matrix[row][-1] < target:
                start_col = row + 1
            #first elem from the row
            elif matrix[row][0] > target:
                end_col = row - 1
            else:
                row_f = matrix[row]
                break
        
        if not row_f:
            return False

        #search in the row of matrix, the target
        start = 0
        end = x_max
        while start <= end:
            found = (start+end)//2
            if row_f[found] == target:
                return True
            elif row_f[found] < target:
                start = found + 1
            else:
                end = found - 1

        return False
        