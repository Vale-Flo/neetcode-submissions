class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # if I haven t the conditions mentionned at the subject, I'd use
        # matrix.sort()
        # print(matrix)

        #each row is sorted in non-decreasing order.
        #The first integer of every row is greater than the last integer of the previous row.

        for row in matrix:
            start = 0
            end = len(row) - 1
            while start <= end:
                found = (start+end)//2
                if row[found] == target:
                    return True
                elif row[found] < target:
                    start = found + 1
                else:
                    end = found - 1

        return False
